"""
Description: DIY Stream Deck
Board: Raspberry Pi Pico with rp2040
Display: NX3224T024 yellow = Rx | Blue = Tx
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
from rgb import RGB

#Objects
keyboard=Keyboard(usb_hid.devices)
consumer_control=ConsumerControl(usb_hid.devices)
serial=busio.UART(board.GP4, board.GP5, baudrate=9600)#UART1 tx - rx
rgb = RGB()

colors = {
    '1': 'red',
    '2': 'green',
    '3': 'blue',
    '4': {'red':32000,'blue':40000,'green':65535}
}

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
    if page==1 and component==3:
        rgb.off_rgb()
        rgb.blink_rgb()
    if page==2:
        rgb.off_rgb()
        color = colors[str(component)]
        rgb.turn_on(color)
        

if __name__ == '__main__':
    rgb.off_rgb()
    while True:
        try:
            data=serial.read(7)#number of bytes b'e\x00\x02\x01\xff\xff\xff'
            if len(data) == 7:
                define_action(data[1], data[2])
        except:
            #Exception for data=None
            pass