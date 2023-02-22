#!/usr/bin/env python3 

import subprocess
import optparse


def get_user_arg():
    user_pass = optparse.OptionParser()
    user_pass.add_option("-i","--interface",dest="interface")
    user_pass.add_option("-m","--mac",dest="new_mac")

    (options, arguments) = user_pass.parse_args()
    if not options.interface:
        user_pass.error("[-] Please enter Mac address, or use --help for more info")
    elif not options.new_mac:
        user_pass.error("[-] Please specify MAC address, or use --help for more info")
    return options


def change_mac(interface,new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig",interface,"down"])

(options) = get_user_arg()
change_mac(options.interface, options.new_mac)