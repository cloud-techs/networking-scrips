from scapy.all import *

packets = rdpcap('Lab 7_Identifying Packet Loss.pcapng')

# print(dir(packets))
# packets.nsummary()

# Filter packets with nsummary lambda tcp flags
data = packets.nsummary(
    lfilter=lambda packet: packet[TCP].flags == "S" or packet[TCP].flags == "SA")

print(data)
