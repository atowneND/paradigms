from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ClientFactory
from twisted.internet.tcp import Port
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue

MY_HOST = "student02.cse.nd.edu"
MY_PORT = 40092
SERVER_PORT = 40001
queue = DeferredQueue()

class MyServer(LineReceiver):
    def __init__(self):
        """
        Server Connection (LHS): handles a connection with a client
        """
        self.delimiter = "\r\n\r\n"
        self.addr = "nothing"
        queue.get().addCallback(self.sendData2Client)

    def lineReceived(self,line):
        """
        This is called when the proxy receives data from the client, buffered
        by the delimiter. It makes a connection with the external server and
        creates an instance of the client connection class
        """
        reactor.connectTCP(MY_HOST, SERVER_PORT, ClientConnectionFactory(line+self.delimiter))
    
    def connectionMade(self):
        """
        This is called when a new connection is made from a client to the proxy
        server
        """
        print "connection received from", self.addr

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        print "connection lost from", self.addr

    def sendData2Client(self, data):
        """
        This sends data from the proxy to the client
        """
        self.transport.write(data)
    
class MyServerFactory(Factory):
    """
    Server Connection (LHS): creates instances of the server handler for any
    number of connections
    """
    protocol = MyServer

    def buildProtocol(self, addr):
        """
        Generates the protocol upon connection to spin up a MyServer
        instance to handle the request
        """
        m = MyServer()
        m.addr = addr
        return m

class ClientConnection(Protocol):
    """
    Client Connection (RHS): for a single connection to an external server
    """
    def __init__(self, data):
        self.data = data

    def dataReceived(self, returned_data):
        """
        This is called when the server sends data back to the proxy client. The
        returned data is put on the queue for the proxy server to handle.
        """
        queue.put(returned_data)

    def connectionMade(self):
        """
        This is called when the connection is made to the external server. It
        writes the data (to the external server) that the proxy server received
        from the external client.
        """
        print "new connection made to", MY_HOST, "port", SERVER_PORT
        self.transport.write(self.data)

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        reactor.stop()

class ClientConnectionFactory(ClientFactory):
    """
    Factory to handle any number of instances of connections
    """
    def __init__(self, data):
        self.data = data
        protocol = ClientConnection

    def buildProtocol(self, addr):
        """
        Generates the protocol upon connection to spin up a ClientConnection
        instance to handle the request
        """
        return ClientConnection(self.data)

if __name__ == "__main__":
    reactor.listenTCP(MY_PORT, MyServerFactory())
    reactor.run()
