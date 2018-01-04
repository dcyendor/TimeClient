#!/usr/bin/env python3

"""Network time client"""

import sys
import socket

def get_time():
    """Returns the time string from the specified host:port"""
    buffersize = 1024
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((host, port))
    data = soc.recv(buffersize)
    soc.close()
    return 'Received:' + data.decode()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(get_time(sys.argv[1], sys.argv[2]))
    else:
        print(get_time())
