from threading import Thread
import time
import threading
from server import Publisher
from client import Subscriber
from broker import Broker
import time
import zmq

def rapid_publish(publisher, info, stop):
    count = 0
    while (not stop.is_set()):
        publisher.publish(info)
        count = count + 1
    print("Published = ", count)

def publish1(publisher, info, stop):
    count = 0
    while count == 0:
        print("Time published: %.20f" % time.time())
        publisher.publish(info)
        count = count + 1
    print("Published = ", count)

def test1():
    ip_add = "127.0.0.1"
    # initialize
    broke1 = Broker(ip_add)
    sub1 = Subscriber(ip_add, 3)
    pub1 = Publisher(ip_add)

    # set up subscriber and publisher with broker
    stop = threading.Event()
    # subscriber
    sub1.register_sub("soccer, basketball") # subscribe -- need no threading
    # publishers/broker
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker for publisher to register with
    T2 = Thread(target=pub1.register_pub, args=("soccer",)) # publisher registers
    T1.start()
    T2.start()
    stop.set()
    T1.join()
    T2.join()

    # open up broker, subscriber for listening and start publishing rapidly.
    stop.clear()
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker
    T2 = Thread(target=sub1.notify, args=(stop,))
    T3 = Thread(target=rapid_publish, args=(pub1, "hello world", stop))

    T2.start()
    T1.start()
    T3.start()

    # 1 second wait
    time.sleep(1)
    stop.set()

    # Results
    print("Received: ", sub1.count)

def test2():
    ip_add = "127.0.0.1"
    # initialize
    broke1 = Broker(ip_add)
    sub1 = Subscriber(ip_add, 3)
    sub2 = Subscriber(ip_add, 3)
    sub3 = Subscriber(ip_add, 3)
    sub4 = Subscriber(ip_add, 3)
    sub5 = Subscriber(ip_add, 3)
    sub6 = Subscriber(ip_add, 3)
    sub7 = Subscriber(ip_add, 3)
    sub8 = Subscriber(ip_add, 3)
    sub9 = Subscriber(ip_add, 3)
    sub10 = Subscriber(ip_add, 3)

    pub1 = Publisher(ip_add)

    # set up subscriber and publisher with broker
    stop = threading.Event()
    # subscriber
    sub1.register_sub("soccer, basketball") # subscribe -- need no threading
    sub2.register_sub("soccer, basketball") # subscribe -- need no threading
    sub3.register_sub("soccer, basketball") # subscribe -- need no threading
    sub4.register_sub("soccer, basketball") # subscribe -- need no threading
    sub5.register_sub("soccer, basketball") # subscribe -- need no threading
    sub6.register_sub("soccer, basketball") # subscribe -- need no threading
    sub7.register_sub("soccer, basketball") # subscribe -- need no threading
    sub8.register_sub("soccer, basketball") # subscribe -- need no threading
    sub9.register_sub("soccer, basketball") # subscribe -- need no threading
    sub10.register_sub("soccer, basketball")  # subscribe -- need no threading

    # publishers/broker
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker for publisher to register with
    T2 = Thread(target=pub1.register_pub, args=("soccer",)) # publisher registers
    T1.start()
    T2.start()
    stop.set()
    T1.join()
    T2.join()

    # open up broker, subscriber for listening and start publishing rapidly.
    stop.clear()
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker
    T2 = Thread(target=sub1.notify, args=(stop,))
    T3 = Thread(target=sub2.notify, args=(stop,))
    T4 = Thread(target=sub3.notify, args=(stop,))
    T5 = Thread(target=sub4.notify, args=(stop,))
    T6 = Thread(target=sub5.notify, args=(stop,))
    T7 = Thread(target=sub6.notify, args=(stop,))
    T8 = Thread(target=sub7.notify, args=(stop,))
    T9 = Thread(target=sub8.notify, args=(stop,))
    T10 = Thread(target=sub9.notify, args=(stop,))
    T11 = Thread(target=sub10.notify, args=(stop,))
    T12 = Thread(target=rapid_publish, args=(pub1, "hello world", stop))

    T1.start()
    T2.start()
    T3.start()
    T4.start()
    T5.start()
    T6.start()
    T7.start()
    T8.start()
    T9.start()
    T10.start()
    T11.start()
    T12.start()

    # 1 second wait
    time.sleep(1)
    stop.set()

    # Results
    average = sub1.count + sub2.count + sub3.count + sub4.count + sub5.count + sub6.count + sub7.count + sub8.count + sub9.count + sub10.count
    average = average / 10
    print("AVERAGE = ", average)


def test3():
    ip_add = "127.0.0.1"
    # initialize
    broke1 = Broker(ip_add)
    sub1 = Subscriber(ip_add, 3)

    pub1 = Publisher(ip_add)
    pub2 = Publisher(ip_add)
    pub3 = Publisher(ip_add)
    pub4 = Publisher(ip_add)
    pub5 = Publisher(ip_add)
    pub6 = Publisher(ip_add)
    pub7 = Publisher(ip_add)
    pub8 = Publisher(ip_add)
    pub9 = Publisher(ip_add)
    pub10 = Publisher(ip_add)

    # set up subscriber and publisher with broker
    stop = threading.Event()
    # subscriber
    sub1.register_sub("soccer, basketball") # subscribe -- need no threading

    # publishers/broker
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker for publisher to register with
    T2 = Thread(target=pub1.register_pub, args=("soccer",)) # publisher registers
    T3 = Thread(target=pub2.register_pub, args=("soccer",))  # publisher registers
    T4 = Thread(target=pub3.register_pub, args=("soccer",))  # publisher registers
    T5 = Thread(target=pub4.register_pub, args=("soccer",))  # publisher registers
    T6 = Thread(target=pub5.register_pub, args=("soccer",))  # publisher registers
    T7 = Thread(target=pub6.register_pub, args=("soccer",))  # publisher registers
    T8 = Thread(target=pub7.register_pub, args=("soccer",))  # publisher registers
    T9 = Thread(target=pub8.register_pub, args=("soccer",))  # publisher registers
    T10 = Thread(target=pub9.register_pub, args=("soccer",))  # publisher registers
    T11 = Thread(target=pub10.register_pub, args=("soccer",))  # publisher registers

    T1.start()
    T2.start()
    T3.start()
    T4.start()
    T5.start()
    T6.start()
    T7.start()
    T8.start()
    T9.start()
    T10.start()

    time.sleep(2)
    T11.start()
    stop.set()

    T1.join()
    T2.join()
    T3.join()
    T4.join()
    T5.join()
    T6.join()
    T7.join()
    T8.join()
    T9.join()
    T10.join()
    T11.join()

    # open up broker, subscriber for listening and start publishing rapidly.
    stop.clear()
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker
    T2 = Thread(target=sub1.notify, args=(stop,))

    T3 = Thread(target=rapid_publish, args=(pub1, "hello world", stop))
    T4 = Thread(target=rapid_publish, args=(pub2, "hello world", stop))
    T5 = Thread(target=rapid_publish, args=(pub3, "hello world", stop))
    T6 = Thread(target=rapid_publish, args=(pub4, "hello world", stop))
    T7 = Thread(target=rapid_publish, args=(pub5, "hello world", stop))
    T8 = Thread(target=rapid_publish, args=(pub6, "hello world", stop))
    T9 = Thread(target=rapid_publish, args=(pub7, "hello world", stop))
    T10 = Thread(target=rapid_publish, args=(pub8, "hello world", stop))
    T11 = Thread(target=rapid_publish, args=(pub9, "hello world", stop))
    T12 = Thread(target=rapid_publish, args=(pub10, "hello world", stop))

    T1.start()
    T2.start()
    T3.start()
    T4.start()
    T5.start()
    T6.start()
    T7.start()
    T8.start()
    T9.start()
    T10.start()
    T11.start()
    T12.start()

    # 1 second wait
    time.sleep(1)
    stop.set()

    # Results
    print("Received = ", sub1.count)

def test4():
    ip_add = "127.0.0.1"
    # initialize
    broke1 = Broker(ip_add)
    sub1 = Subscriber(ip_add)
    pub1 = Publisher(ip_add)

    # set up subscriber and publisher with broker
    stop = threading.Event()
    # subscriber
    sub1.register_sub("soccer, basketball") # subscribe -- need no threading
    # publishers/broker
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker for publisher to register with
    T2 = Thread(target=pub1.register_pub, args=("soccer",)) # publisher registers
    T1.start()
    T2.start()
    stop.set()
    T1.join()
    T2.join()

    # open up broker, subscriber for listening and start publishing rapidly.
    stop.clear()
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker
    T2 = Thread(target=sub1.notify, args=(stop,))

    T1.start()
    T2.start()
    time.sleep(1)
    print("Time published: %.20f" % time.time())
    pub1.publish("hello world")
    # 1 second wait
    time.sleep(1)
    stop.set()

def test5():
    ip_add = "127.0.0.1"
    # initialize
    broke1 = Broker(ip_add)
    sub1 = Subscriber(ip_add, 3)
    sub2 = Subscriber(ip_add, 3)
    sub3 = Subscriber(ip_add, 3)
    sub4 = Subscriber(ip_add, 3)
    sub5 = Subscriber(ip_add, 3)
    sub6 = Subscriber(ip_add, 3)
    sub7 = Subscriber(ip_add, 3)
    sub8 = Subscriber(ip_add, 3)
    sub9 = Subscriber(ip_add, 3)
    sub10 = Subscriber(ip_add, 3)

    pub1 = Publisher(ip_add)

    # set up subscriber and publisher with broker
    stop = threading.Event()
    # subscriber
    sub1.register_sub("soccer, basketball") # subscribe -- need no threading
    sub2.register_sub("soccer, basketball") # subscribe -- need no threading
    sub3.register_sub("soccer, basketball") # subscribe -- need no threading
    sub4.register_sub("soccer, basketball") # subscribe -- need no threading
    sub5.register_sub("soccer, basketball") # subscribe -- need no threading
    sub6.register_sub("soccer, basketball") # subscribe -- need no threading
    sub7.register_sub("soccer, basketball") # subscribe -- need no threading
    sub8.register_sub("soccer, basketball") # subscribe -- need no threading
    sub9.register_sub("soccer, basketball") # subscribe -- need no threading
    sub10.register_sub("soccer, basketball")  # subscribe -- need no threading

    # publishers/broker
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker for publisher to register with
    T2 = Thread(target=pub1.register_pub, args=("soccer",)) # publisher registers
    T1.start()
    T2.start()
    stop.set()
    T1.join()
    T2.join()

    # open up broker, subscriber for listening and start publishing rapidly.
    stop.clear()
    T1 = Thread(target=broke1.run, args=(stop,)) # open up broker
    T2 = Thread(target=sub1.notify, args=(stop,))
    T3 = Thread(target=sub2.notify, args=(stop,))
    T4 = Thread(target=sub3.notify, args=(stop,))
    T5 = Thread(target=sub4.notify, args=(stop,))
    T6 = Thread(target=sub5.notify, args=(stop,))
    T7 = Thread(target=sub6.notify, args=(stop,))
    T8 = Thread(target=sub7.notify, args=(stop,))
    T9 = Thread(target=sub8.notify, args=(stop,))
    T10 = Thread(target=sub9.notify, args=(stop,))
    T11 = Thread(target=sub10.notify, args=(stop,))
    T12 = Thread(target=publish1, args=(pub1, "hello world", stop))

    T1.start()
    T2.start()
    T3.start()
    T4.start()
    T5.start()
    T6.start()
    T7.start()
    T8.start()
    T9.start()
    T10.start()
    T11.start()
    T12.start()

    # 1 second wait
    time.sleep(1)
    stop.set()


if __name__ == '__main__':
    # uncomment out tests to run.

    ### stress tests
    test1() # 1 publisher, 1 subscriber, 1 broker
    # test2() # 1 publisher, 10 subscribers, 1 broker
    # test3() # 10 publishers, 1 subscriber, 1 broker

    ### timing tests -- need to uncomment a line in client.py before running
    # test4() # 1 publisher, 1 subscriber, 1 broker
    # test5() # 1 publisher, 10 subscribers, 1 broker -- will need to scroll up past the exceptions to see results



