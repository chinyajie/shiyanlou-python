# /usr/bin/env python3

import sys
import socket

def get_args():
    if(len(sys.argv) != 5):
        print("Parameter Error")
        exit()
    try:
        host_index = sys.argv.index('--host')
        port_index = sys.argv.index('--port')

        host = sys.argv[host_index + 1]
        port = sys.argv[port_index + 1]
    except(ValueError, IndexError):
        print("Parameter Error")

    if len(host.split('.')) != 4:
        print('Parameter Error')
        exit()
        
    if '-' in port:
        port = port.split('-')
    else:
        port = [port, port]
    return host, port

def scan():
    host, ports = get_args()
    for port in range(int(ports[0]), int(ports[1])+1):
        sock = socket.socket()
        sock.settimeout(0.1)
        
        if sock.connect_ex((host, port)) == 0: #is (,)
            print(port, 'open')
        else:
            print(port, 'closed')
        sock.close()

if __name__ == '__main__':
    scan()
