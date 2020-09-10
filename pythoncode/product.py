def product(L):
    p = 1
    i = 0
    while i < len(L):
        p = p * L[i]
        i += 1
    return p 

def product2(L):
    p = 1 
    i = 0
    while True:
        if i >= len(L):
            break
        p = p * L[i]
        i = i + 1
    return p 
def product3(L):
    p = 1
    for i in range(len(L)):
        p = p * L[i]
    return p
def produc(L): #the best
    p = 1
    for n in L:
        p = p * n
    return p