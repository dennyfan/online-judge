def RepeatedLookup2():
	ESdict={'one':'uno','dos':'two','three':'tres'}
    while True:
        word = input('enter word')
        if word == '':
            break
        if word in ESdict:
            print(f'{word} means {ESdict[word]}')
        else:
            print(f'{word} not in dict')
RepeatedLookup2()