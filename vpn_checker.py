import psutil

def check_vpn_connection(vpn_name):
    connections = psutil.net_if_addrs()
    return vpn_name in connections
