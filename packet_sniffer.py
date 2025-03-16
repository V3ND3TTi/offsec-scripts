from scapy.all import sniff

# Function to process captured packets
def process_packet(packet):
    print(packet.summary())  # Prints basic packet details

# Start sniffing (capture 10 packets on all interfaces)
print("Sniffing network traffic... Press Ctrl+C to stop.")
sniff(prn=process_packet, count=10)
