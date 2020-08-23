from mpu9250 import MPU9250
import sys
from time import sleep  # import

imu = MPU9250('X')

imu.get_gyro_irq()
imu.get_accel_irq()
imu.get_mag_irq()

scale = 6.6666                      # Correction factors involve floating point
mag = list(map(lambda x, y : x*y/scale, imu.mag.ixyz, imu.mag_correction))

print(" Reading Data of Gyroscope and Accelerometer")
      
while True:            
    print("Interrupt:", [x/16384 for x in imu.accel.ixyz], [x/131 for x in imu.gyro.ixyz], mag)
    sleep(0.1)
    print("Normal:   ", imu.accel.xyz, imu.gyro.xyz, imu.mag.xyz)
    print()
    sleep(0.5)