english	=	{'one':1,'pan':'鍋⼦','cabbage':'⾼麗菜','pie':'派'}
spanish	=	{'uno':1,'pan':'麵包','col':'⾼麗菜','pie':'腳'}
french	=   {'une':1,'toi':'你','col':'衣領','pie':'鵲'}

def lookupdicts(w):
    outlist = []
    if w in english:
	    outlist.append(f'in	English: {english[word]}')
    if w in spanish:
	    outlist.append(f'in	Spanish: {spanish[word]}')
    if w in french:
	    outlist.append(f'in	French: {french[word]}')
    return outlist

word = input('enter word to	look up: ')
outlist = lookupdicts(word)

if not outlist:
	print(f'{word} not found in dictionary')
else:
    print('\n'.join(outlist))

#print(f'{word} not found in dictionary' if not outlist \
 #      else '\n'.join(outlist) )

#print('\n'.join(outlist) if outlist \
 #      else f'{word} not found in dictionary')

