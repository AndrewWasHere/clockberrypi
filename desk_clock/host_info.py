import socket
import subprocess

def host_info():
    hostname = socket.gethostname()
    ipv4 = get_ipv4()
    ipv6 = get_ipv6()
    ssid = get_ssid()
    other_info = get_other_info()

    return (
        f'hostname: {hostname} || IPv4: {ipv4} || IPv6: {ipv6}\n'
        f'SSID: {ssid}'
        f'{other_info}'
    )


def get_ipv4():
    cmd = ['ip', 'a']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return inet_addrs(result.stdout, 'inet', verboten='127')


def get_ipv6():
    cmd = ['ip', 'a']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return inet_addrs(result.stdout, 'inet6', verboten='::')


def get_ssid():
    cmd = ['iwgetid', '-r']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def get_other_info():
    try:
        with open('other_info.txt', 'r') as f:
            info = ''.join(f.readlines())
    except FileNotFoundError:
        info = ''

    return info


def inet_addrs(output, inet_token, verboten):
    tokens = output.split()
    inet_indexes = []
    for idx, token in enumerate(tokens):
        if token == inet_token:
            inet_indexes.append(idx + 1)

    ip_addrs = [
        tokens[idx].split('/')[0] 
        for idx in inet_indexes
        if not tokens[idx].startswith(verboten)
    ]

    return ', '.join(ip_addrs)

