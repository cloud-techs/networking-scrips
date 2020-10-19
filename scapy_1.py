from scapy.all import *

packets = rdpcap('Lab 7_Identifying Packet Loss.pcapng')

# print(dir(packets))
# packets.nsummary()

# Filter packets with nsummary lambda
# packets.nsummary(
#     lfilter=lambda packet: packet[TCP].sport == 51597 or packet[TCP].sport == 1)


for pac in packets[3:]:
    # pac.show()
    # print(dir(pac))
    print(pac[TCP].window, pac[TCP].sport, pac[TCP].dport)

    # print(pac[Raw].show())

    # print(dir(scapy.packet.Raw))
    # print(pac.haslayer(TCP))
    # print("test", pac.haslayer(Ether))
    # print(pac.summary())
    # print(pac.time)
    # break
