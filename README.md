# Assignment 2 for distributed systems
The following assignment covers the pub-sub pattern with a multiples broker using ZMQ and Zookeeper, and it is compatible with mininet.

Please use the python environment used in assignment 1 for testing purposes.

In assignment 1, broker.py was used to launch the broker. For assignment 2, zookeeper.py is used instead, and it launches three brokers and holds an election to elect which broker should be used.

The following 3 unit tests demonstrate the functionality of our system. In addition, all the unit tests specified in assignment 1 also work (just substitute zookeeper.py for broker.py).

To launch the three brokers: python zookeeper.py 127.0.0.1 
To launch a subscriber: python client.py "sports" 127.0.0.1
To launch a publisher: python server.py "sports" 127.0.0.1

# Test 1
This test involves 3 brokers, 1 subscriber, and 1 publisher. It demonstrates that when the main broker is killed, a new election will automatically be held to elect a new broker (from the other two alive brokers) to be used as the main broker, and the system will continue as always.

![Test1](/ass2testing/test1.png)

In this test, a three brokers are launched, and an election is held to elect the main broker (that uses port 1236 for publishing). The publisher and subscriber are connected to this broker, and messages (Manchester United, Liverpool) are sent and received under the topic of sports. At this time, the script kill_president.py is run, which kills the main broker. As a result, a new election is held, and the broker that uses port 1234 for publishing is elected as the main broker. After this, more messages are exchanged (Manchester City, Everton) and the system functions as expected.

# Test 2
This test involves 3 brokers, 3 subscribers, and 1 publisher. It illustrates that subscriptions still work as expected in this system. The publsiher is registered for the topic of sports. Meanwhile, 2/3 subscribers are registered for the topic of sports while 1 subscriber is registered for the topic of fashion. The subscribers for sports receieve all published messages while the subscriber for fashion does not. This test can be conducted with the introduction of new subscribers at any time and also with the exit of subscribers at any time.

![Test2](/ass2testing/test2.png)

# Test 3
This test involves 3 brokers, 2 subscribers, and 2 publishers. 1 publisher and 1 subscriber are both registered for the topic of sports, while the other publisher and other subscriber are registered for the topic of fashion. In this instance, all messages sent by each publisher are received by the corresponding subscriber. This test can be conducted with the introduction of new subscribers or publishers at any time and also with the exit of subscribers or publishers at any time.

Finally, as mentioned earlier, all the unit tests specified in assignment 1 should also work (just substitute zookeeper.py for broker.py)

![Test3](/ass2testing/test3.png)

# Measurements

All raw measurements of this system's performance are available in the excel document measurements.xlsx, and they are summarized and analyzed in Measurements.docx.
