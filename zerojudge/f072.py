n = input()
m = input()
l = m.split()
lint = []
for i in l:
    lint.append(int(i))
if lint.count(1) < 2:
    print(0)
else:
    record1 = []
    for i, v in enumerate(lint):
        if v == 1:
            record1.append(i)
    mx, mi = max(record1), min(record1)
    lint = lint[mi:(mx+1)]
    for i, v in enumerate(lint):
        if v == 9:
            lint[i-1], lint[i+1] = lint[i-1]+2, lint[i+1]+2
        if v == 11:
            lint[i-1], lint[i+1] = lint[i-1]+2, lint[i+1]+2
    print(lint.count(0))