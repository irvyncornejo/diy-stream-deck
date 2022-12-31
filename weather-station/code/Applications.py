from HTTP import HTTP


class Applications:
    def __init__(self):
        self._http =  HTTP()
    
    def run(self, option: str):
        if option == '1':
            print(self._http.get('http://date.jsontest.com'))
        else:
            pass
        