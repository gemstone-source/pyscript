#!/usr/bin/env python3
# Author Hashghost
# Program that changes MAC Address

import subprocess
import optparse

def get_arguments():
    # parser is used to autogenerate help message
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface")
    parser.add_option("-m","--mac", dest = "new_mac")

    ''' return has been used so that the variable options and arguments to be accessed outside the function
        unless the code should be 
        (options, arguments ) = parser.parse_args()
    '''
    
    (options, arguments) = parser.parse_args()
    if not options.interface:
        print("[-] Please specify interface, use --help for more information")
    elif not options.new_mac:
        print("[-] Please specify mac_address, use --help for more information")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface,options.new_mac)