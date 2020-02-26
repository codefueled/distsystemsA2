# Broker
from __future__ import unicode_literals
import zmq
import sys
import threading

class Broker:
    def __init__(self, ip_add):
        self.context = zmq.Context()
        self.sub_socket = context.socket(zmq.SUB)
        self.pub_socket = context.socket(zmq.PUB)
        self.current_topics = []
        full_add1 = "tcp://" + str(ip_add) + ":1234"
        full_add2 = "tcp://" + str(ip_add) + ":5556"

        # bind to ip/ports
        self.sub_socket.bind(full_add1)
        self.sub_socket.subscribe("")
        self.pub_socket.bind(full_add2)

    def run(self, stop=None):
        if stop:
            while (not stop.is_set()):
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
                        print("Received: %s" % message)
                        self.pub_socket.send_string(message)
                else:
                    if topic in self.current_topics:
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
                    print("Received: %s" % message)
                    self.pub_socket.send_string(message)
            else:
                if topic in self.current_topics:
                    print("Received: %s" % message)
                    self.pub_socket.send_string(message)
                else:
                    print("Please start over with a valid topic")

if __name__ == '__main__':
    ip_add = sys.argv[1]
    broker = Broker(ip_add)
    while True:
        broker.run()
