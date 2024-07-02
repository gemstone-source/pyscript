import os,subprocess 


def htb_open_vpn():
    # Start normal vpn hackthebox vpn
    path = os.path.expanduser("~/C7F5/htb/openvpn/hashghost.ovpn") # make it an arg
    subprocess.run(["sudo","openvpn",path])

def thm_open_vpn():
    # New demo
    path = os.path.expanduser("~/C7F5/tmh/hashghost.ovpn")
    subprocess.run(["sudo", "openvpn", path])
    
htb_open_vpn()