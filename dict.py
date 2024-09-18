import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
while True:
    try:
        txt = input("what do you want to know: ")
        a = dict(people='hito', Me='ore')
        b = a.keys()
        
        print(a.get(txt, 'Not found'))
        
        if txt == 'exit':
            break
        elif txt == '':
            break

    except KeyboardInterrupt:
        break