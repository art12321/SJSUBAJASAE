import time
import board
import busio
from adafruit_lsm6ds import Rate, AccelRange, GyroRange
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX
import machine
import sdcard
import uos

## Initialize the Accelerometer 
i2c = busio.I2C(board.GP1,board.GP0)  # uses board.SCL and board.SDA
sox = ISM330DHCX(i2c)
sox.accelerometer_range = AccelRange.RANGE_2G
#sox.gyro_range = GyroRange.RANGE_125_DPS
sox.accelerometer_data_rate = Rate.RATE_1_66K_HZ
#sox.accelerometer_data_rate = Rate.RATE_416_HZ
#sox.gyro_data_rate = Rate.RATE_1_66K_HZ
sox.gyro_data_rate = Rate.RATE_SHUTDOWN

## Initialize the SDcard
# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(15, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=8000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(12))

# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

## [Start Code]

# setup time recording
print(time.localtime())
curr_time = time.time()
start_time = curr_time
delta_time = time.time() - start_time

file_name = f'/sd/test_{curr_time}.csv'		#append file name
t = (delta_time,sox.acceleration[0],sox.acceleration[1],sox.acceleration[2])	# initialize t variable
file_maxValue = 200 	# Number of recordings between append file

while True:
    with open(file_name, "w") as curr_file:
        curr_file.write(("%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n" % time.localtime()))
        for i in range(file_maxValue):
            delta_time = time.time() - start_time
            t = (delta_time,sox.acceleration[0],sox.acceleration[1],sox.acceleration[2])
            curr_file.write("%.2f, %.2f, %.2f, %.2f\n" % t)
    curr_file.close()
	
	# Debug code
    time_difference = time.time() - curr_time
    curr_time = time.time()
    data_rate = (file_maxValue/time_difference)
    print("current time: ")
    print(curr_time)
    print("the tDiff is: ")
    print(time_difference)
    print("current data rate is: ")
    print(data_rate)
    print("__________")
	# /Debug code
    file_name = f'/sd/test_{curr_time}.csv'	#Append new file
