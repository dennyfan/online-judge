#!/usr/bin/env python3
d = {'rate': 0.05}
def totalwithtax(*names, **kv):
    global d
    total = 0.0
    for kw, val in kv.items():
        d[kw] = val
        if kw != 'rate':
            total += val
    for name in names:
        if name in d.keys():
            total += d[name]
        if type(name) in {int, float}:
            total += name
    return total * (1 + d['rate'])
if __name__ == '__main__':
	assert totalwithtax(rate=0.05, apple=20, oranges=15, guava=12) == 49.35
	assert totalwithtax('apple', 'guava') == 33.6
	assert totalwithtax(23, 45, 'oranges', mango=60) == 150.15