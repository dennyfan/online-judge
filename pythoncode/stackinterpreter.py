def stackinterpreter():
    l = []
    while True:
        line = input('command')
        words = line.split()
        if len(words) == 0:
            pass
        elif words[0] == 'show':
            print(l)
        elif words[0] == 'push':
            l.extend(words[1:])
        elif words[0] == 'pop':
            print(l.pop())
        elif words[0] == 'quit':
            break
        else:
            print('unknown commmand')
