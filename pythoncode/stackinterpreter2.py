def stackinterpreter2():
    '''this is a'''#docstring
    l = []
    d = {'':lambda: None, 'show':lambda: print(l), 'push':lambda: l.extend(words[1:]),
         'pop':lambda: print(l.pop())}
    while True:
        line = input('command')
        words = line.split()
        if words[0] == 'quit':
            break
        d.get(words[0], lambda: print('unknown command'))()
         