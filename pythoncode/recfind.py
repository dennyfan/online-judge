#!/usr/bin/env python3
def recfind(l, val):
    if type(l) in {list, tuple}:
        for i, v in enumerate(l):
            p = recfind(v, val)
            if p == True:
                return (i,)
            if p != False:
                return (i, )+p
    return l ==val

def recfind2(l, val):
    if type(l) in {list, tuple}:
        for i, v in enumerate(l):
            p = recfind(v, val)
            if p == True:
                return (i,)
            if type(p) == tuple:
                return (i, )+p
    return l ==val

def recfind3(l, val):
    if type(l) in {list, tuple}:
        for i, v in enumerate(l):
            p = recfind(v, val)
            if p == True:
                return (i,)
            if bool(p) == True:
                return (i, )+p
    return l ==val

def recfind4(l, val):
    if type(l) in {list, tuple}:
        for i, v in enumerate(l):
            p = recfind(v, val)
            if p != False:#這邊不能!=False，因為下層的回傳(i,)會變成True，最後return最上層的(i,)
                return (i,)
            if p != False:
                return (i, )+p
    return l ==val
#l = [1,2,[3,[4,5]],6]
# False change to True ??