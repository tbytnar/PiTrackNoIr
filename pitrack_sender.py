from imu.mpu9250 import MPU9250
import socket
from struct import *
from time import sleep  # import

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect the socket to the port where the server is listening
# Bind the socket to the port
server_address = '192.168.1.17'
port = 4242
server = (server_address,port)
print('Connecting to ' + server_address + ' on port ' + str(port))


imu = MPU9250(bus=1, device_addr=0x68)
print(" Sending Data from Gyroscope and Accelerometer")
 
try:
    scale = 1

    for count in range(30):
        # Correction factors involve floating point
        mag = list(map(lambda x, y : x*y/scale, imu.mag.ixyz, imu.mag_correction))
        print("Interrupt:", [x/16384 for x in imu.accel.ixyz], [x/131 for x in imu.gyro.ixyz], mag)
        sleep(0.1)
        print("Normal:   ", imu.accel.xyz, imu.gyro.xyz, imu.mag.xyz)
        print()
        sleep(0.5)

        Ax = imu.accel.ixyz[0]
        Ay = imu.accel.ixyz.[1]
        Az = imu.accel.ixyz.[2]

        Gx = imu.gyro.ixyz.[0]
        Gy = imu.gyro.ixyz.[1]
        Gz = imu.gyro.ixyz.[2]

        print('getting reading')
        message = pack('dddddd',Ax,Ay,Az,Gx,Gy,Gz)
        print(message)

        sock.sendto(message, server)
        sleep(0.5)

finally:
    print('closing socket')
    sock.close()
