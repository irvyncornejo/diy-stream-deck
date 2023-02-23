from time import sleep
from umachine import Pin, UART

class NextionDisplays:
    
    def __init__(self, tx:int, rx:int, bits:int=8, baudrate:int=9600)->None:
        self._bits = bits
        self._uart = UART(1, baudrate=baudrate, tx=Pin(tx), rx=Pin(rx))
        self._uart.init(bits=bits, parity=None, stop=1)
    
    def read(self):
        _data = self._uart.read()
        if _data and len(list(_data)) == self._bits - 1:
            _data = list(_data)[1:]
            return _data
        return _data
    
    def write(self, command: str):
        '''
            temp.txt="34 C"
        '''
        _command = bytes(str(command), 'UTF-8')
        _base_command = b'\xff\xff\xff'
        _buffer = _command + _base_command
        self._uart.write(bytearray(_buffer))