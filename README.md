# Multiple_DDos_ScriptS

## This repositories contains three python Denial of Service scripts.One DHCP exhaustion Script , one SYN flood script , and one ARP MAC Flood script 
Resources published from David Bombal , NerualNine and others were used in creating these scripts.Below are the explanation of the script.


## SYN Flood Script 

A session between a client and a server are created when they are communicating with each other.The protocol TCP uses a three-way handshake to 
establish the session.A device would send a SYN packet to the server , server would send a a SYN-ACK packet back to the client and wait for a response.
This script exploits this behavior by continuously sending SYN packets to the server but never sending back a response so that way a session is never created.
The server would be waiting for all the response from the SYN packet that will never come and it would cause the server to not able to function properly


## ARP MAC Flood Script

An ARP table stores information that is used to foward packets within a network.It maps ip addresses to MAC addresses.This attack would
flood the ARP table with these information until they fill up.When the ARP table is filled up , instead of the packet being send to the ip address
it was meant for , it would broadcast the packet.




## DHCP Exhaustion Script 

DHCP protocol used within a network to auto asign private IPs to devices that just joined the network.It has a pool of IP address to give out.
This script will use up all the ip addresses in the pool.By usuing up all the ip address in the pool , new devices joining the network would not
be connected to other devices because it did not get a ip address from the DHCP server.







