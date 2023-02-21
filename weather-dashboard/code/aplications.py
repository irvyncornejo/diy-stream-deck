from HTTP import HTTP
from config import key, q

class Applications:
    def __init__(self):
        self._http =  HTTP()
    
    def run(self, option: str):
        if option == '1':
            print(self._http.get('http://date.jsontest.com'))
        if option == '2':
            f'http://api.weatherapi.com/v1/current.json?key={key}&q={q}&aqi=no'
        else:
            pass


        
