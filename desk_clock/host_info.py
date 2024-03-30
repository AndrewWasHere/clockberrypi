import socket

def host_info():
    hostname = socket.gethostname()
    ipv4 = socket.gethostbyname(hostname)
    ipv6 = 'TBD'

    return f'hostname: {hostname}\nIPv4: {ipv4}\nIPv6: {ipv6}'
