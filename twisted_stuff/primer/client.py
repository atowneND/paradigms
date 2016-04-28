from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ClientFactory
from twisted.internet.tcp import Port
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue

SSH_PORT = 9001
SSH_HOST = "localhost"

class SSHClient(Protocol):
    """
    HOME connects to WORK
    """
    def __init__(self, data):
        self.data = data

    def dataReceived(self, returned_data):
        """
        This is called when the server sends data back to the proxy client. The
        returned data is put on the queue for the proxy server to handle.
        """
        print "CLIENT received:", returned_data
        #queue.put(returned_data)

    def connectionMade(self):
        """
        This is called when the connection is made to the external server. It
        writes the data (to the external server) that the proxy server received
        from the external client.
        """
        print "new connection made from CLIENT to", SSH_HOST, "port", SSH_PORT
        self.transport.write(self.data)

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        reactor.stop()

class SSHClientFactory(ClientFactory):
    """
    Factory to handle any number of instances of connections
    """
    def __init__(self, data):
        self.data = data
        protocol = SSHClient

    def buildProtocol(self, addr):
        """
        Generates the protocol upon connection to spin up a SSHClient
        instance to handle the request
        """
        return SSHClient(self.data)

if __name__=="__main__":
    data = "ssh plz \r\n\r\n"
    reactor.connectTCP(SSH_HOST, SSH_PORT, SSHClientFactory(data))
    reactor.run()
