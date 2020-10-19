from scapy.all import *
from scapy.layers.http import HTTPRequest, HTTPResponse

packets = rdpcap("Lab 8_Identifying Congested Networks.pcapng")
for i in packets:
    with open("test.txt", "a+") as file:
        # check hTTP request and HTTp response
        if i.haslayer(HTTPResponse) or i.haslayer(HTTPRequest):
            # url = i[HTTPRequest].Host.decode() + i[HTTPRequest].Path.decode()
            # print(url)
            # file.writelines(url+"\n")
            print(i.summary())


for i in packets:
    with open("test.txt", "a+") as file:
        # check hTTP request and HTTp response
        if i.haslayer(HTTPRequest):
            url = i[HTTPRequest].Host.decode() + i[HTTPRequest].Path.decode()
            print(url)
            file.writelines(url+"\n")
            print(i.summary())
