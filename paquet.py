from scapy.all import *
import os

def generate_pcap(filename, vlan_id, vlan_prio, udp_dport):
    packets = []
    for i in range(10000):
        packet = Ether()/Dot1Q(vlan=vlan_id, prio=vlan_prio)/IP(src="10.0.0.2", dst="10.0.0.1")/UDP(sport=12345, dport=udp_dport)
        packets.append(packet)
    wrpcap(filename, packets)

os.makedirs("pcaps", exist_ok=True)
generate_pcap("pcaps/high_priority.pcap", 100, 7, 10000)  # VLAN ID 100, VLAN Prio 7, UDP dport 10000
generate_pcap("pcaps/medium_priority.pcap", 200, 4, 20000)  # VLAN ID 200, VLAN Prio 4, UDP dport 20000
generate_pcap("pcaps/low_priority.pcap", 300, 0, 30000)  # VLAN ID 300, VLAN Prio 0, UDP dport 30000

