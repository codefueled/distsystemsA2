# Publisher
from __future__ import unicode_literals
import zmq
import time
import sys

class Publisher:
    # instantiate variables and connect to broker
    def __init__(self, ip_add):
        self.topic = "Default"
        self.full_add = "tcp://" + str(ip_add) + ":1234"
        ctx = zmq.Context()
        self.sock_pub = ctx.socket(zmq.PUB)
        self.sock_pub.connect(self.full_add)
        print("Publisher connected to the broker")

    # register a topic for this publisher
    def register_pub(self, topic):
        self.topic = topic
        msg = "REGISTER||" + str(self.topic)
        time.sleep(1)
        self.sock_pub.send_string(msg)
        return True

    # publish the given information for pre-registered topic
    def publish(self, info):
        # format for published string is "topic||info"
        msg = str(self.topic) + "||" + str(info)
        self.sock_pub.send_string(msg)
        return True


if __name__ == '__main__':
    # handle input
    if len(sys.argv) != 3:
        print("Please provide 2 arguments as specified in the readme")
    elif "||" in sys.argv[1]:
        print("Please re-run and remove any '||' found in the topic name")
    else:
        # process input arguments
        topic = sys.argv[1]
        ip_add = sys.argv[2]

        # create Publisher object
        pub = Publisher(ip_add)
        pub.register_pub(topic)

        # wait for inputted information to publish
        while True:
            info = input("Input information about your topic and press enter to publish!\n")
            pub.publish(info)
            print("Success!")