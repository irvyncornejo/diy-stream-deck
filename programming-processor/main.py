"""
Description: DIY Stream Deck
Board: Raspberry Pi Pico with rp2040
Display: NX3224T024
"""
from time import sleep

import board
import digitalio
import busio
import rotaryio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

#Objects
keyboard=Keyboard(usb_hid.devices)
consumer_control=ConsumerControl(usb_hid.devices)
serial=busio.UART(board.GP4, board.GP5, baudrate=9600)#UART1

def get_operating_system(page: int ,component: int) -> str:
    pass

def define_action(page: int ,component: int) -> None:
    """
    """
    if page==0 and component==1:
        consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
    if page==0 and component==2:
        consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)
    if page==0 and component==3:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.G)
    if page==0 and component==4:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.Y)
    if page==0 and component==5:
        keyboard.send(Keycode.WINDOWS, Keycode.E)
    if page==0 and component==6:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.P)
    

if __name__ == '__main__':
    while True:
        try:
            data=serial.read(7)#number of bytes b'e\x00\x02\x01\xff\xff\xff'
            if len(data) == 7:
                define_action(data[1], data[2])
        except:
            #Exception for data=None
            pass