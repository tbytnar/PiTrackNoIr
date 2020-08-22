import socket
import sys
from time import sleep  # import
from struct import *

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Bind the socket to the port
server_address = '0.0.0.0'
port = 4242
socket_bind = (server_address,port)
print('starting up on ' + server_address + ' port ' + str(port))
sock.bind(socket_bind)

counter = 0

while counter < 10:
    data = sock.recvfrom(48)

    if data:
        datastring = unpack('dddddd',data[0])
        print(datastring)

    sleep(0.1)