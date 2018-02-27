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

        if len(port.split('.')) != 4:
            print('Parameter Error')
            exit()
        host = int(host)
        
        if '-' in port:
            port = port.split('-')
        else:
            port = [port, port]
        return host, port


def scan():
    host, ports = get_args()
    for port in range(ports[0], ports[1]+1):
        socket = socket.socket()
        socket.settimeout(0.1)
        
        if socket.connect_ex(host, i) == 0:
            print(i, 'open')
        else:
            print(i, 'closed')
        socket.close()

if __name__ == '__main__':
    scan()
