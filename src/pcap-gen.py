from scapy.all import *
import random

packets = []

# Add some normal traffic
for i in range(10):
    pkt = IP(src="192.168.1.100", dst="10.0.0.1") / TCP(sport=random.randint(1000,5000), dport=80, flags="S") / Raw(load="Normal HTTP Request")
    packets.append(pkt)

# Add strong Attack traffic (SYN Flood + high error rate pattern)
for i in range(70):
    src_ip = f"172.16.{random.randint(1,255)}.{random.randint(1,255)}"
    pkt = IP(src=src_ip, dst="10.0.0.1", ttl=64) / TCP(sport=random.randint(10000,60000), dport=80, flags="S", seq=i*1000)
    packets.append(pkt)

wrpcap("strong_attack.pcap", packets)
print("✅ Created 'strong_attack.pcap'")
print("This has many SYN packets from different IPs - should trigger Attack more easily.")