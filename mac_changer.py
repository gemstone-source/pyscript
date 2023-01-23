#!/usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface")
    parser.add_option("-m","--mac", dest = "new_mac")

    ''' return has been used so that the variable options and arguments to be accessed outside the function
        unless the code should be 
        (options, arguments ) = parser.parse_args()
    '''
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface,options.new_mac)