from scapy.all import sniff, IP

# This function handles the data packets
def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Captured: Source {src_ip} --> Destination {dst_ip} | Protocol: {protocol}")

print("--- CodeAlpha Network Sniffer Starting ---")
print("Press Ctrl+C to stop.")

# This captures 20 packets
sniff(prn=process_packet, store=False, count=20)
