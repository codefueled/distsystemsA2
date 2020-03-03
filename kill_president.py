from kazoo.client import KazooClient
import logging

zk = KazooClient(hosts='127.0.0.1:2181')
logging.basicConfig()
zk.start()
print("Deleting the Broker.")
zk.delete("/president/pres")
