from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.tcp import Port
from twisted.internet import reactor

MY_PORT = 40092

class MyConnection(LineReceiver):
    def __init__(self):
        self.delimiter = "\r\n\r\n"
        self.addr = "nothing"

    def lineReceived(self,line):
        print "data received:",line
    
    def connectionMade(self):
        print "connection received from", self.addr

    def connectionLost(self, reason):
        print "lost connection to localhost port", MY_PORT
        print "    because:", reason

class MyConnectionFactory(Factory):
    def buildProtocol(self, addr):
        m = MyConnection()
        m.addr = addr
        return m

if __name__ == "__main__":
    reactor.listenTCP(MY_PORT, MyConnectionFactory())
    reactor.run()
