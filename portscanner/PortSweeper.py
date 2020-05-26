
#Get the Threads Variable from __init__
from portscanner import threads
#Import threading Module
import threading
#Import Socket Classes and Variables that are needed
from socket import socket,AF_INET,SOCK_STREAM

#Class portSweeper Inherits from Threading.Thread to allow multiple ports to be scanned at once
# and needs a port number and ip_address

class PortSweeper(threading.Thread):
    #Initialize Class with IP address, Port to be scanned, and the IP_PORT_CLASS that is creating it.
    def __init__(self,ip_address,port,ip_port_class):
        threading.Thread.__init__(self)
        self.ip_address = ip_address
        self.port = port
        self.IP_PORT_CLASS = ip_port_class

    #Run Routine that overrides threading.thread - allows async execution.
    def run(self):
        #Create a TCP socket
        a_socket = socket(AF_INET, SOCK_STREAM)
        #Network stuff likes to fail, so we are going to put everything in a Try-Catch. If port is open, everything will
        # work. Otherwise, we can assume port is closed.
        try:
            #set the socket timeout to a second.
            a_socket.settimeout(1)
            #If statement checks that connection was made, it then appends the port into an array within the IP_PORT_CLASS
            #That stores open ports
            if a_socket.connect_ex((self.ip_address, self.port)) == 0:
                self.IP_PORT_CLASS.open_port_list.append(self.port)
                print("Port {} on {} is open".format(self.port,self.ip_address))
            #socket then needs to close!!!
            a_socket.close()
        except Exception as e:
            #Print out whatever error happened
            print(e)
        #Close socket in case try-catch encounteded exception
        a_socket.close()
        #Remove thyself from thread array which is used to limit number of async threads to avoid "too many descriptors error"
        threads.remove(self)

