#!/usr/bin/env pyhon3
# Author Gemstone Hashghost
# Network Scanner

import scapy.all as scapy

def scan(ip):
    ''' The first ARP will asks for only 0.0.0.0 but no specific ip'''
    # scapy.ls(scapy.ARP())
    # arp_request = scapy.ARP()
    # print(arp_request.summary())

    arp_request = scapy.ARP(pdst=ip) # Obtain the specific ip, "Who has this ip"
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Setting Broadcast MAC 
    arp_request_broadcast = broadcast/arp_request     # Generation new frame by combining both ip and mac
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        clients_dict = {"ip" : element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in result_list:
        print(client["ip"] +"\t\t"+ client["mac"])


scan_result = scan("192.168.43.1/24")
print_result(scan_result)

