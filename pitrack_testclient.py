import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# Bind the socket to the port
server_address = 'localhost'
port = 4242
socket_bind = (server_address,port)
print('starting up on ' + server_address + ' port ' + str(port))
sock.connect(socket_bind)

try:
    while True:
        data = sock.recv(512)
        print(data.decode())

finally:
    print('closing socket')
    sock.close()