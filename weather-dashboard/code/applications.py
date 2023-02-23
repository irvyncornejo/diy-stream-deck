from HTTP import HTTP
from config import key, q
from nextionDisplay import NextionDisplays

class Applications:
    def __init__(self):
        self._http =  HTTP()
        self._display = NextionDisplays(4, 5)
        self._buffer = []
    
    def _show_new_values(self, time, temp, condition, humidity)->None:
        
        _values = {
         'localtime': f'localtime.txt="{time.split()[1]}"',
         'temp': f'temp.txt="{temp} C"',
         'condition': f'condition.txt="{condition}"',
         'humidity' : f'humidity.txt="{humidity}%"'
        }
        
        [self._display.write(value) for value in _values.values()]
    
    def _retrieve_weather(self)->None:
        if self._buffer[1] == 0:
            response = self._http.get(
                url=f'http://api.weatherapi.com/v1/current.json?key={key}&q={q}&aqi=no'
            )
            self._show_new_values(
                time=response['location']['localtime'],
                temp=response['current']['temp_c'],
                condition=response['current']['condition']['text'],
                humidity=response['current']['humidity']
            )

    
    def run(self)->None:
        self._buffer = self._display.read()
        if self._buffer:
            self._retrieve_weather()


