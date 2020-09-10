def index(L, val):
    i = 0
    while i < len(L):
        if L[i] == val:
            break
        i += 1
    return i if i < len(L)\
            else -1

def index2(L, val):
    i = 0
    while i < len(L):
        if L[i] == val:
            break
        i += 1
    else:
        return -1
    return i
def index20(L, val):#(後來想的)
    i = 0
    while True:
        if i < len(L) and L[i] == val:
            break
        elif i < len(L):
            i += 1
        else:
            return -1
    return i 


def index3(L, val):
    i = 0
    while i < len(L):
        if L[i] == val:
            return i
        i += 1
    return -1

def index4(L, val): #the best
    for i, v in enumerate(L):
        if v == val:
            return i
    return -1
