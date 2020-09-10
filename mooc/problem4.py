l = []
def write_record(expense, date='2020/01/18',description='something'):
    l.append(f'${expense}, {date}, {description}')
def list_records():
    for i in l:
        print(f'{i}')
def total_expense():
    t = 0
    for v in l:
        j = v.split('$')
        k = j[1]
        a = k.split(',')
        b = a[0]
        c = int(b)
        t = t+ c
        
    return t
for i  in range(4):
    calling_write_record = input()
    exec(calling_write_record)
list_records()
print(total_expense())