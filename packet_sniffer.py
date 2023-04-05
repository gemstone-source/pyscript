import scapy.all as scapy


def sniff(interface):
   scapy.sniff(iface=interface, store=False, prn=sniffed_packets)

def sniffed_packets(packet):
   print(packet)

sniff("wlan0")