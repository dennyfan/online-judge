n = input()#1 to 25
m = input()#1 and 0 
l = m.split()
record = []
for a,b in enumerate(l):
    if b == '1':
        record.append(1)
print(record)