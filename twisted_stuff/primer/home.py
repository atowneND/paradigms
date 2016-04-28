from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ClientFactory
from twisted.internet.tcp import Port
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue

WORK_COMM_PORT = 40092
WORK_HOST = "localhost"
WORK_DATA_PORT = 41092
SSH_PORT = 9001

command_queue = DeferredQueue()
data_queue = DeferredQueue()
client_queue = DeferredQueue()

class DataServer(LineReceiver):
    def __init__(self):
        """
        HOME server; listens for connection from WORK
        """
        self.delimiter = "\r\n\r\n"
        self.addr = "nothing"

    def dataReceived(self,returned_data):
        """
        This is called when the proxy receives data from the client, buffered
        by the delimiter. It makes a connection with the external server and
        creates an instance of the client connection class
        """
        print "HOME.DataServer received:", returned_data,"from",self.addr
        client_queue.put(returned_data)

    def connectionMade(self):
        """
        This is called when a new connection is made from a client to the proxy
        server
        """
        print "connection to HOME.DataServer received from", self.addr
        def sendData(data):
            self.transport.write(data)
            data_queue.get().addCallback(sendData)
        data_queue.get().addCallback(sendData)

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        print "connection to HOME.DataServer lost from", self.addr

    def sendData2Client(self, data):
        """
        This sends data from the proxy to the client
        """
        self.transport.write(data)

class CommandServer(LineReceiver):
    def __init__(self):
        """
        HOME server; listens for connection from WORK
        """
        self.delimiter = "\r\n\r\n"
        self.addr = "nothing"

    def lineReceived(self,line):
        """
        This is called when the proxy receives data from the client, buffered
        by the delimiter. It makes a connection with the external server and
        creates an instance of the client connection class
        """
        pass

    def connectionMade(self):
        """
        This is called when a new connection is made from a client to the proxy
        server
        """
        print "connection to HOME.CommandServer received from", self.addr
        def sendData(data):
            self.transport.write(data)
            command_queue.get().addCallback(sendData)
        command_queue.get().addCallback(sendData)

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        print "connection to HOME.CommandServer lost from", self.addr

class ClientServer(LineReceiver):
    def __init__(self):
        """
        HOME server; listens for connection from CLIENT
        """
        self.addr = "nothing"

    def dataReceived(self,data):
        """
        This is called when the proxy receives data from the client, buffered
        by the delimiter. It makes a connection with the external server and
        creates an instance of the client connection class
        """
        print "HOME.ClientServer received:", data,"from",self.addr
        data_queue.put(data)

    def connectionMade(self):
        """
        This is called when a new connection is made from a client to the proxy
        server
        """
        def sendData(data):
            self.transport.write(data)
            client_queue.get().addCallback(sendData)
        client_queue.get().addCallback(sendData)
        reactor.listenTCP(WORK_DATA_PORT, HomeServerFactory("Data"))
        command_queue.put("merp")

    def connectionLost(self, reason):
        """
        This is called when the connection is lost
        """
        print "connection to HOME.ClientServer lost from", self.addr

    def sendData2Client(self, data):
        """
        This sends data from the proxy to the client
        """
        self.transport.write(data)

class HomeServerFactory(Factory):
    """
    Server Connection (LHS): creates instances of the server handler for any
    number of connections
    """
    def __init__(self, protocol):
        self.protocol = protocol

    def buildProtocol(self, addr):
        """
        Generates the protocol upon connection to spin up the appropriate HomeServer instance to handle the request
        """
        if self.protocol == "Command":
            m = CommandServer()
        elif self.protocol == "Client":
            m = ClientServer()
        elif self.protocol == "Data":
            m = DataServer()
        else:
            print "Unknown connection type"
        m.addr = addr
        return m

if __name__=="__main__":
    reactor.listenTCP(WORK_COMM_PORT, HomeServerFactory("Command"))
    reactor.listenTCP(SSH_PORT,HomeServerFactory("Client"))
    reactor.run()
