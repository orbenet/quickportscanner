from portscanner import threads,PortSweeper
import time


#CLASS to store all OPEN PORT info for a single IP
class TCP_IP_CLASS:
    def __init__(self,ip_address):
        self.ip_address = ip_address
        self.open_port_list = []
    def get_open_ports_on_ip(self):
        #Loop through all possible ports
        x = 0
        while x < 65535:
            #Make sure thread count is less than 1000
            while len(threads) < 1000:
                x +=1
                #create a portsweeper thread
                t = PortSweeper(self.ip_address,x,self)
                #add it to the threads list
                threads.append(t)
                #start the thread
                t.start()
                #exit while len(threads) <1000 loop every time it is executed.
                break
        #wait for connections to return result with 10 second timeout
        time.sleep(10)