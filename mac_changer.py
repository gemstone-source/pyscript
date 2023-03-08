#!/usr/bin/env python3
# Author Hashghost
# Program that changes MAC Address

import subprocess
import optparse
import re

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
    # If statement condition for error control
    if not options.interface:
        parser.error("[-] Please specify interface, use --help for more information")
    elif not options.new_mac:
        parser.error("[-] Please specify mac_address, use --help for more information")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "up"])

def get_current_mac(interface):
    # Reading result
    interface_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_result.decode('utf-8'))

    # Checking if the interface has MAC address 
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Sorry Could not find MAC address")

# Calling all declared functions
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC is "+ str(current_mac))
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] The MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed")
