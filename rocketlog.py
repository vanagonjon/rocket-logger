import time
import board
import busio
import adafruit_bno055
import adafruit_gps
import serial

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)

#Setup
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)