"""
Description: DIY Stream Deck
Board: Raspberry Pi Pico with rp2040
Display: NX3224T024
"""
from time import sleep

import board
import digitalio
import busio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

keyboard = Keyboard(usb_hid.devices)
serial = busio.UART(board.GP4, board.GP5, baudrate=9600)#UART1

if __name__ == '__main__':
    while True:
        data=serial.read(7)#number of bytes b'e\x00\x02\x01\xff\xff\xff'
        try:
            if len(data) == 7:
                keyboard.send(Keycode.WINDOWS, Keycode.E)
                sleep(1)
        except:
            #Exception for data=None
            pass