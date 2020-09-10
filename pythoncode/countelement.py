def count(x):
    if type(x) != list:
        return 1
    c = 0
    for i in x:
        c = c + count(i)
    return c
    
def count2(x):
    return 1 if type(x) != list else sum(map(count, x))

def count3(x):
    if type(x) != type([]):
        return 1
    elif x == []:
        return 0
    else:
        return count3(x[0]) + count3(x[1:])
#['a','f',['fb','fbf',['fb','ie']]]
 