x = input()
l = x.split()
l[0] = ' '+l[0]+ ' '
print(l[0].join(l[1:]))