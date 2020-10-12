import pyshark

cap = pyshark.LiveCapture(interface='Wi-Fi', bpf_filter="host 192.168.29.176")


for packet in cap.sniff_continuously():
    print('Just arrived:', packet.layers)
    # print(dir(packet))
    # break
