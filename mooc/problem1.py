s1 = input('Enter a string:\n')
s2 = input('Enter another string:\n')
if len(s1) > len(s2):
    print(f'Shorter string: {s2} (length {len(s2)})\nLonger string: {s1} (length {len(s1)})')
elif len(s1) < len(s2):
    print(f'Shorter string: {s1} (length {len(s1)})\nLonger string: {s2} (length {len(s2)})')
else:
    print(f'First string: {s1} (length {len(s1)})\nSecond string: {s2} (length {len(s2)})')
#correct2020.08.17