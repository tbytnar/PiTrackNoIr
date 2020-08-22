#!/usr/bin/env python2

from time import sleep
from sys import argv, exit
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from struct import pack, unpack
import os

if os.name != 'nt':
    raise "only for Windows socket semantics"

# you can use the "pack" function
# cf. <https://docs.python.org/2/library/struct.html#format-characters>
YOUR_MESSAGE_TO_SEND = b'something'

# same as opentrack's port
#OUR_PORT = int(argv[3])

# the sender's udp bind address
TARGET_HOSTNAME = "127.0.0.1"
TARGET_PORT = 4242

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#sock.bind(("127.0.0.1", 4242))
while True:
    print("testing")
    sock.sendto(YOUR_MESSAGE_TO_SEND, (TARGET_HOSTNAME, TARGET_PORT))
    sleep(1)
sock.close()