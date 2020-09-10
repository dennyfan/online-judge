n = input()
m = input() 
l = m.split()
record1 = []
record2 = []
def find1(l, val='9'):
    k = []
    if type(l) != list: raise TypeError
    if type(val) != str: raise TypeError
    for i,v in enumerate(l):
        if v == val:
            k.append(i)
    return k 

def compare(l1,l9):
    for i,v in enumerate(l9):
        if int(v) < int(l1[0]):
            l9 = l9[(i+1):]
    for i,v in enumerate(l9):
        if int(v) > int(l1[-1]):
            l9 = l9[:(i)]
    
    x = len(l1)+len(l9)*3
    for i in l9:
        if i+1 in l1:
            x -= 1
        if i-1 in l1:
            x -= 1
        if i+1 in l9:
            x -= 1
        if i-1 in l9:
            x -= 1
    return x

for a,b in enumerate(l):
    if b == '1':
        record1.append((a,b))
    if b == '9':
        record2.append((a,b))
if len(record1)<2:
    print(0)
else:
    mx = max(record1)[0]
    mi = min(record1)[0]
    l9 = find1(l,'9')
    l1 = find1(l,'1')
    x = compare(l1, l9)
    l = l[mi:(mx+1)]
    ans = len(l) - x
    print(ans)

