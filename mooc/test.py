records = []
s = 0
def write_record(cost,date='2020/01/18',description='something'): 
    records.append((cost,date,description))
    global s
    s += cost
def list_records():
    for i in records:
        print(f'${i[0]}, {i[1]}, {i[2]}')
def total_expense():
    return s
for i in range(4):
    calling_write_record = input()
    exec(calling_write_record)
list_records()
print(total_expense())