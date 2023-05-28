import argparse
from scapy.all import *

class Sniffer:
    def __init__(self, args):
        self.args = args

    def __call__(self, packet):
        if self.args.verbose:
            packet.show()
        else:
            print(packet.summary())

    def run_forever(self):
        sniff(iface=self.args.interface, prn=self, store=0)

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', default=False, action='store_true', help='be more talkative')
parser.add_argument('-i', '--interface', type=str, required=True, help='network interface name')
args = parser.parse_args()
sniffer = Sniffer(args)
sniffer.run_forever()

# Run with following command
# sudo python3 sniffer1.py -v -i wlp1s0
# sudo python3 sniffer1.py -v -i enp3s0
# You can change last network id -> wlp1s0
