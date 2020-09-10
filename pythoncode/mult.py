#!/usr/bin/env python3
def mult_table(l, r):
    for i in l:
        for j in r:
            print(f'{i:3} x {j:3} = {i*j:6.2f}')
if __name__ == '__main__':
    mult_table(range(9,12), range(8,11))
