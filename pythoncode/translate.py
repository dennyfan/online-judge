english	=	{'one':1,'pan':'鍋⼦','cabbage':'⾼麗菜','pie':'派'}
spanish	=	{'uno':1,'pan':'麵包','col':'⾼麗菜','pie':'腳'}
french	=   {'une':1,'toi':'你','col':'衣領','pie':'鵲'}
found = False
word = input('enter	word	to	look	up:	')
if word in english:
	print(f'in	English:	{english[word]}')
    found = True
if word in spanish:
	print(f'in	Spanish:	{spanish[word]}')
    found = True
if word in french:
	print(f'in	French:	{french[word]}')
    found = True
if not found:
	print(f'{word}	not	found	in	dictionary')
