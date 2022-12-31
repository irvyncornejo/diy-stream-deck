from Applications import Applications


if __name__=='__main__':
    """
    Cases Use
        - Option 1 - Get Time
    """
    while True:
        try:
            app = Applications()
            option = input('Ingresa la Opción: ')
            app.run(option)

        except Exception as e:
            print(e)
            
