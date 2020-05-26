#Create Empty Array to Store Threads
threads = []

#Import PortSweeper Class into portscanner Directory Init
from portscanner.PortSweeper import PortSweeper

#Import TCP_IP_CLASS Class into portscanner Directory Init
from portscanner.TCP_IP_CLASS import TCP_IP_CLASS

#Define a function that takes an IP address and creates a TCP_IP_CLASS - then runs get_open_ports function and returns the result
def scan_one_IP(ip_address):
    x = TCP_IP_CLASS(ip_address)
    x.get_open_ports_on_ip()
    return x.open_port_list