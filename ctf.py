import os,subprocess 


def htbOpenVpn():
    # Start normal vpn hackthebox vpn
    path = os.path.expanduser("~/C7F5/htb/openvpn/hashghost.ovpn") # make it an arg
    subprocess.run(["sudo","openvpn",path])

def thmOpenVpn():
    path = os.path.expanduser("~/C7F5/tmh/hashghost.ovpn")
    subprocess.run(["sudo", "openvpn", path])
    
htbOpenVpn()