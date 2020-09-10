#!/usr/bin/env python3
def numberoutline(l, prefix=()):
    i = 0
    if type(l) in {list, tuple}:
        for v in l:
            if type(v) not in {list, tuple}:
                i += 1
            numberoutline(v, prefix+(i,))
    else:
        s = ' '*4*(len(prefix)-1)
        s += '.'.join(map(str, prefix)) + '. ' + l
        print(s)

def numberoutline2(l, prefix=()):
    
    if type(l) in {list, tuple}:
        i = 0
        for v in l:
            if type(v) not in {list, tuple}:
                i += 1
            numberoutline(v, prefix+(i,))
    else:
        s = ' '*4*(len(prefix)-1)
        s += '.'.join(map(str, prefix)) + '. ' + l
        print(s)
def sp(l, deep=0, nm=[0]):#19's solution (a little bit different)
    for i in l:
        if type(i) in {list, tuple}:
            nm.append(1)
            sp(i, deep+1, nm )
            nm.pop()
        else:
            nm.append(nm.pop()+1)
            for x in nm:
                print(x, end='.')
            print(f'{" "*4*deep}{i}')

#L=['Intro',['Motivation', 'Contributions'], 'Related Work', ['By Author', 'By Subject'],'Technical Approach', ['Overview', ['Block Diagram', 'Schematic'], 'Algorithm', ['Static', 'Dynamic']], 'Conclusions']
