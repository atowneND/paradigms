# work.py
# Ashley Towne
# create a command connectino to home
# serves as a proxy

from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ClientFactory
from twisted.internet.tcp import Port
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue

HOME_HOST = "localhost"
HOME_COMM_PORT = 40092
HOME_DATA_PORT = 41092

SERVER_EXT = "student02.cse.nd.edu"
SERVER_PORT = 22

data_queue = DeferredQueue()
server_queue = DeferredQueue()

class SSHClient(Protocol):
    """
    Work connects to home - data
    """
    def __init__(self, data):
        self.data = data

    def dataReceived(self, returned_data):
        """
        This is called when the server sends data back to the proxy client. The
        returned data is put on the queue for the proxy server to handle.
        """
        data_queue.put(returned_data)

    def connectionMade(self):
        """
        This is called when the connection is made to the external server. It
        writes the data (to the external server) that the proxy server received
        from the external client.
        """
        print "new connection made from WORK.SSHClient to", HOME_HOST, "port", HOME_COMM_PORT
        def sendData(data):
            self.transport.write(data)
            server_queue.get().addCallback(sendData)
        server_queue.get().addCallback(sendData)

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        reactor.stop()

class DataClient(Protocol):
    """
    Work connects to home - data
    """
    def dataReceived(self, returned_data):
        """
        This is called when the server sends data back to the proxy client. The
        returned data is put on the queue for the proxy server to handle.
        """
        server_queue.put(returned_data)

    def connectionMade(self):
        """
        This is called when the connection is made to the external server. It
        writes the data (to the external server) that the proxy server received
        from the external client.
        """
        print "new connection made from WORK.DataClient to", HOME_HOST, "port", HOME_COMM_PORT
        def sendData(data):
            self.transport.write(data)
            data_queue.get().addCallback(sendData)
        data_queue.get().addCallback(sendData)

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        reactor.stop()

class CommandClient(Protocol):
    """
    Work connects to home - command
    """
    def __init__(self):
        pass

    def dataReceived(self, returned_data):
        """
        This is called when the server sends data back to the proxy client. The
        returned data is put on the queue for the proxy server to handle.
        """
        reactor.connectTCP(HOME_HOST,HOME_DATA_PORT,WorkClientFactory("Data"))
        reactor.connectTCP(SERVER_EXT,SERVER_PORT,WorkClientFactory("SSH"))

    def connectionMade(self):
        """
        This is called when the connection is made to the external server. It
        writes the data (to the external server) that the proxy server received
        from the external client.
        """
        print "new connection made from WORK.CommandClient to", HOME_HOST, "port", HOME_DATA_PORT

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        pass

class WorkClientFactory(ClientFactory):
    """
    Factory to handle any number of instances of connections
    """
    def __init__(self, protocol):
        self.protocol = protocol

    def buildProtocol(self, addr):
        """
        Generates the protocol upon connection to spin up a WorkClient
        instance to handle the request
        """
        data = "HI\r\n\r\n"
        if self.protocol == "Command":
            m = CommandClient()
        elif self.protocol == "Data":
            m = DataClient()
        elif self.protocol == "SSH":
            m = SSHClient(data)
        else:
            print "Unknown connection type"
        m.addr = addr
        return m

if __name__ == "__main__":
    reactor.connectTCP(HOME_HOST, HOME_COMM_PORT, WorkClientFactory("Command"))
#    reactor.listenTCP(MY_PORT, WorkServerFactory())
    reactor.run()
