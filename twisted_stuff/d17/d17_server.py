from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.tcp import Port
from twisted.internet import reactor

MY_PORT = 40092

class MyConnection(LineReceiver):
    def __init__(self):
        """
        delimiter is the typical one we saw in class: \r\n\r\n
        """
        self.delimiter = "\r\n\r\n"
        self.addr = "nothing"

    def lineReceived(self,line):
        """
        This is called when the server receives data from the client, buffered
        by the delimiter. It prints it out for the user to see.
        """
        print "data received:",line,self.delimiter
    
    def connectionMade(self):
        """
        This is called when a new connection is made
        """
        print "connection received from", self.addr

    def connectionLost(self, reason):
        """
        This is called when the connection is lost, for whatever reason. Even
        if the connection is terminated cleanly, it will state the reason and
        stop the reactor
        """
        print "connection lost from", self.addr
        reactor.stop()

class MyConnectionFactory(Factory):
    """
    Factory to handle any number of instances of connections
    """
    protocol = MyConnection

    def buildProtocol(self, addr):
        """
        Generates the protocol upon connection to spin up a MyConnection
        instance to handle the request
        """
        m = MyConnection()
        m.addr = addr
        return m

if __name__ == "__main__":
    reactor.listenTCP(MY_PORT, MyConnectionFactory())
    reactor.run()
