import pyshark

cap = pyshark.LiveCapture(interface='Wi-Fi', bpf_filter='udp port 53')

cap.sniff(packet_count=10)


def print_dns_info(pkt):
    if pkt.dns.qry_name:
        print(pkt.ip.src, pkt.dns.qry_name)
    elif pkt.dns.resp_name:
        print(pkt.ip.src, pkt.dns.resp_name)


cap.apply_on_packets(print_dns_info, timeout=100)
