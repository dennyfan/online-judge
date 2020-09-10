#!/usr/bin/env python3
def indentlist(l, level = 0):
    if l == None:
        return
    if type(l) in {list, tuple}:
        for i in l:
            indentlist(i, level+1)
    else:
        print(f'{" "*4*level}{l}')
if __name__ == '__main__':
    l = ['f1',['f4','f5',['f8']],'f2','f3','d3',['f6','f7']]
    indentlist(l)
