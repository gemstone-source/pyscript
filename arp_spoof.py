import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.43.75", hwdst="fe80::a997:b298:85ac:cb12", psrc="192.168.43.1")