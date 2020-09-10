x = input()
k = int(input())
l = [chr(i) for i in range(65, 65+26)]
x1 = list(x)
re = []
for i in x1:
    a = l.index(i) - k
    re.append(l[a])
print(''.join(re))

