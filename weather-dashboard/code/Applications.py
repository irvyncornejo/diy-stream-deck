from HTTP import HTTP
from umachine import Pin, PWM

class Applications:
    def __init__(self):
        self._http =  HTTP()
    
    def run(self, option: str):
        if option == '1':
            print(self._http.get('http://date.jsontest.com'))
        else:
            pass

class Actuators:
    def __init__(
        self,
        pin: int,
        mode:str
    ) -> None:
        self._pin = (
            Pin("LED", Pin.OUT) if mode == 'output' else Pin(pin, Pin.IN)
        )
    
    def changeState(self, state:bool) -> None:
        if state:
            self._pin.on()
        self._pin.off()
    
    def changeValue(self, value:int) -> None:
        pass

class NextionDisplay:
    pass

class Servo:
    pass

        
