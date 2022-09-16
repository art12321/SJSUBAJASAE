import time
import board
import busio
import digitalio
from adafruit_lsm6ds import Rate, AccelRange, GyroRange
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX
import machine
import sdcard
import uos

#import adafruit_sdcard
#import sdcardio
#import storage

i2c = busio.I2C(board.GP1,board.GP0)  # uses board.SCL and board.SDA
sox = ISM330DHCX(i2c)
#sox.accelerometer_range = AccelRange.RANGE_8G
#sox.gyro_range = GyroRange.RANGE_125_DPS
#sox.accelerometer_data_rate = Rate.RATE_1_66K_HZ
#sox.accelerometer_data_rate = Rate.RATE_416_HZ
#sox.gyro_data_rate = Rate.RATE_1_66K_HZ
#sox.gyro_data_rate = Rate.RATE_SHUTDOWN


# Assign chip select (CS) pin (and start it high)
#cs = machine.Pin(15, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
#spi = machine.SPI(1,
#                  baudrate=1000000,
#                  polarity=0,
#                  phase=0,
 #                 bits=8,
#                  firstbit=machine.SPI.MSB,
#                  sck=machine.Pin(10),
#                  mosi=machine.Pin(11),
#                  miso=machine.Pin(12))

# Initialize SD card
#sd = sdcard.SDCard(spi, cs)

# Mount filesystem
#vfs = uos.VfsFat(sd)
#uos.mount(vfs, "/sd")

# Create a file and write something to it
#with open("/sd/test01.txt", "w") as file:
#    file.write("Hello, SD World!\r\n")
#    file.write("This is a test\r\n")

# Open the file we just created and read from it
#with open("/sd/test01.txt", "r") as file:
#    data = file.read()
#    print(data)
    
#spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
# Use board.SD_CS for Feather M0 Adalogger
#cs = digitalio.DigitalInOut(board.GP17)
# Or use a digitalio pin like 5 for breakout wiring:
#cs = digitalio.DigitalInOut(board.D5)

#sdcard = adafruit_sdcard.SDCard(spi, cs)
#sd = sdcardio.SDCard(busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16), board.GP17, 8_000_000)
#vfs = storage.VfsFat(sd) #(sdcard)
#storage.mount(vfs, "/sd")

#print(sox.acceleration)
#print(sox.acceleration[0])
file_maxValue = 500
#print(time.localtime())
curr_time = time.time()
start_time = curr_time
#file_name = f'/sd/test_{curr_time}.csv'
#curr_file = open(file_name)
#delta_time = time.time() - start_time
#t = (delta_time,sox.acceleration[0],sox.acceleration[1],sox.acceleration[2])
while True:
#     with open(file_name, "w") as curr_file:
#         curr_file.write(("%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n" % time.localtime()))
#         for i in range(file_maxValue):
#             delta_time = time.time() - start_time
#             t = (delta_time,sox.acceleration[0],sox.acceleration[1],sox.acceleration[2])
#             curr_file.write("%.2f, %.2f, %.2f, %.2f\n" % t)
#     curr_file.close()
    for i in range(file_maxValue):
        #t = (delta_time,sox.acceleration[0],sox.acceleration[1],sox.acceleration[2])
        t = (sox.acceleration[0])
        t=1
        #t1 = (sox.acceleration[1])
        #t2 = (sox.acceleration[2])
#    time_difference = time.time() - curr_time
#    curr_time = time.time()
#    data_rate = (file_maxValue/time_difference)
#    print("current time: ")
#    print(curr_time)
#    print("the tDiff is: ")
#    print(time_difference)
#    print("current data rate is: ")
#    print(data_rate)
#    print("__________")
    #file_name = f'/sd/test_{curr_time}.csv'
    #curr_file = open(file_name, "a")
        #curr_file.open(f"sox_{time.localtime()}")
        #templist = (time.monotonic(),sox.acceleration[0],sox.acceleration[1],sox.acceleration[2],sox.gyro[0],sox.gyro[1],sox.gyro[2])
        #t = (time.monotonic(),sox.acceleration[0],sox.acceleration[1],sox.acceleration[2])
        #f.write("Hello world!\r\n")
        #f.write(sox.acceleration \r\n)
        #print("%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f" % t)
        #f.write("%.2f, %.2f, %.2f, %.2f\n" % t)
        #print(sox.acceleration)
        #time.sleep(.1)
        #print("")
        #time.sleep(0)