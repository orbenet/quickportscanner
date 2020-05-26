from portscanner import scan_one_IP

from sys import argv

if __name__ == "__main__":
    #Print the IP being given in the CMD Argument
    print("SCANNING {}".format(argv[1]))
    #Print out the result once scanning is finished
    print("RESULT: {}".format(str(scan_one_IP(argv[1]))))
