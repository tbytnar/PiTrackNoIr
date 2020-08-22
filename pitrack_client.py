import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# Bind the socket to the port
server_address = '192.168.1.63'
port = 10000
socket_bind = (server_address,port)
print('starting up on ' + server_address + ' port ' + str(port))
sock.connect(socket_bind)

try:
    data = sock.recv(16)
    print(data)

finally:
    print('closing socket')
    sock.close()