from imu.mpu9250 import MPU9250
from time import sleep

imu = MPU9250(bus=1, device_addr=0x68)
print(" Reading Data of Gyroscope and Accelerometer")
 
RAD_TO_DEG = 180 / 3.14159265358979323846


scale = 6.6666 

for count in range(10):
    # Correction factors involve floating point
    mag = list(map(lambda x, y : x*y/scale, imu.mag.ixyz, imu.mag_correction))
    print("Interrupt:", [x/16384 for x in imu.accel.ixyz], [(x/131)*RAD_TO_DEGREES for x in imu.gyro.ixyz])
    sleep(0.1)
    print("Normal:   ", imu.accel.xyz, imu.gyro.xyz)
    print()
    sleep(0.5)