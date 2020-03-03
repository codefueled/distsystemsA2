#Zookeeper driver to handle broker allocation
#IMPORTS
from __future__ import unicode_literals
import zmq
from kazoo.client import KazooClient
import sys
import logging
logging.basicConfig()

class ZK_Driver:
    #CTOR
    def __init__(self, ip_add):
        context = zmq.Context()
        self.kill = False
        self.sub_socket = context.socket(zmq.SUB)
        self.pub_socket = context.socket(zmq.PUB)
        self.current_topics = []

        self.zk_driver = KazooClient(hosts='127.0.0.1:2181')
        self.zk_driver.start()

        #ROOT DIRECTORY FOR BROKERS
        self.home = '/brokers/'

        #CREATE ZNODE PATHS FOR BROKERS
        self.znode1 = self.home + 'bkr1'
        self.znode2 = self.home + 'brk2'
        self.znode3 = self.home + 'brk3'

        #ENSURE ROOT DIRECTORY IS CREATED
        self.zk_driver.ensure_path(self.home)

        #CREATE ZNODES WITH PUB + SUB PORT
        if not self.zk_driver.exists(self.znode1):
            self.zk_driver.create(self.znode1, b'1234:5556')
        if not self.zk_driver.exists(self.znode2):
            self.zk_driver.create(self.znode2, b'1235:5556')
        if not self.zk_driver.exists(self.znode3):
            self.zk_driver.create(self.znode3, b'1236:5556')

        #HOLD ELECTION TO GET PRESIDENT NODE
        self.election = self.zk_driver.Election(self.home, "president")
        contenders = self.election.contenders()
        self.president = contenders[-1].encode('latin-1') #REPRESENTS THE WINNING PUB/SUB PORT COMBO
        ports = self.president.decode('ASCII').split(":")

        #FULL BROKER PORT ADDRESSES
        self.full_add1 = "tcp://" + str(ip_add) + ":" + ports[0]
        self.full_add2 = "tcp://" + str(ip_add) + ":" + ports[1]

        #BIND TO ADDRESSES
        self.sub_socket.bind(self.full_add1)
        self.sub_socket.subscribe("")
        self.pub_socket.bind(self.full_add2)

        #SET UP WATCH DIRECTORY FOR PRESIDENT
        self.president_home = "/president/"
        self.pres_znode = "/president/pres"

        #CREATE OR UPDATE PRESIDENT ZNODE
        if not self.zk_driver.exists(self.pres_znode):
            self.zk_driver.ensure_path(self.president_home)
            self.zk_driver.create(self.pres_znode, ephemeral=True)
        self.zk_driver.set(self.pres_znode, self.president)

        # REMOVE PRESIDENT FROM FUTURE ELECTIONS
        if ports[0] == "1234":
            self.zk_driver.delete(self.znode1)
        elif ports[0] == "1235":
            self.zk_driver.delete(self.znode2)
        elif ports[0] == "1236":
            self.zk_driver.delete(self.znode3)
        else:
            print("No port recognized")

    def run(self, stop=None):
        @self.zk_driver.DataWatch(self.pres_znode)
        def watch_node(data, stat, event):
            if event is not None and event.type == "DELETED":
                if not self.kill:
                    # HOLD ELECTION TO GET PRESIDENT NODE
                    self.election = self.zk_driver.Election(self.home, "president")
                    contenders = self.election.contenders()
                    self.president = contenders[-1].encode('latin-1')  # REPRESENTS THE WINNING PUB/SUB PORT COMBO
                    ports = self.president.decode('ASCII').split(":")

                    # FULL BROKER PORT ADDRESSES
                    self.full_add1 = "tcp://" + str(ip_add) + ":" + ports[0]
                    self.full_add2 = "tcp://" + str(ip_add) + ":" + ports[1]
                    print("Updated Broker to: ", self.full_add1)

                    # BIND TO ADDRESSES
                    self.sub_socket.bind(self.full_add1)
                    self.sub_socket.subscribe("")
                    # self.pub_socket.bind(self.full_add2)

                    # UPDATE PRESIDENT ZNODE
                    if not self.zk_driver.exists(self.pres_znode):
                        self.zk_driver.ensure_path(self.president_home)
                        self.zk_driver.create(self.pres_znode, ephemeral=True)
                    self.zk_driver.set(self.pres_znode, self.president)

                    # DELETE FROM FUTURE ELECTIONS
                    if ports[0] == "1234":
                        self.zk_driver.delete(self.znode1)
                    elif ports[0] == "1235":
                        self.zk_driver.delete(self.znode2)
                    elif ports[0] == "1236":
                        self.zk_driver.delete(self.znode3)
                    else:
                        print("No port recognized")

                    if not self.kill:
                        self.kill = True

        if stop:
            while not stop.is_set():
                message = self.sub_socket.recv_string()
                topic, info = message.split("||")
                error_flag = False

                if topic == "REGISTER":
                    error = False
                    for curr_topic in self.current_topics:
                        if info.startswith(curr_topic) and info != curr_topic:
                            print("Topic is too similar to topic of another publisher, choose another")
                            error = True
                    if not error:
                        self.current_topics.append(info)
                        print("Addr ", self.full_add1, end=". ")
                        print("Received: %s" % message)
                        self.pub_socket.send_string(message)
                else:
                    if topic in self.current_topics:
                        print("Addr ", self.full_add1, end=". ")
                        print("Received: %s" % message)
                        self.pub_socket.send_string(message)
                    else:
                        print("Please start over with a valid topic")
        else:
            message = self.sub_socket.recv_string()
            topic, info = message.split("||")
            error_flag = False

            if topic == "REGISTER":
                error = False
                for curr_topic in self.current_topics:
                    if info.startswith(curr_topic) and info != curr_topic:
                        print("Topic is too similar to topic of another publisher, choose another")
                        error = True
                if not error:
                    self.current_topics.append(info)
                    print("Addr ", self.full_add1, end=". ")
                    print("Received: %s" % message)
                    self.pub_socket.send_string(message)
            else:
                if topic in self.current_topics:
                    print("Addr ", self.full_add1, end=". ")
                    print("Received: %s" % message)
                    self.pub_socket.send_string(message)
                else:
                    print("Please start over with a valid topic")


if __name__ == '__main__':
    ip_add = sys.argv[1]
    driver = ZK_Driver(ip_add)
    while True:
        driver.run()