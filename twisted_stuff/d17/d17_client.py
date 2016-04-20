from twisted.internet import reactor as reactor
from twisted.internet.protocol import ClientFactory, Protocol

host = "student02.cse.nd.edu"
port = 40092

class ClientConnection(Protocol):
    """
    Client Connection: for a single connection/request
    """
    def dataReceived(self, data):
        """
        This is called when the server sends data back to the client. It
        prints it out for the user to see.
        """
        print "received:", data

    def connectionMade(self):
        """
        This is called when the connection is made and executes the get request
        """
        print "new connection made to", host, "port", port
        self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n") # some get request

    def connectionLost(self, reason):
        """
        This is called when the connection is lost, for whatever reason. Even
        if the connection is terminated cleanly, it will state the reason and
        stop the reactor
        """
        print "connection to", host, "lost because", reason
        reactor.stop()

class ClientConnectionFactory(ClientFactory):
    """
    Factory to handle any number of instances of connections
    """
    protocol = ClientConnection
    def buildProtocol(self, addr):
        """
        Generates the protocol upon connection to spin up a ClientConnection
        instance to handle the request
        """
        print "Connected"
        return ClientConnection()

if __name__ == "__main__":
    reactor.connectTCP(host, port, ClientConnectionFactory())
    reactor.run()
