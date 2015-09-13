__author__ = 'Marc'

import serial
ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
while True:
    print ser.readline()

# version 2
# spam spam spam