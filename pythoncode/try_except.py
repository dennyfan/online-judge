try:
    x = int(input('num1'))
    y = int(input('num2'))
    z = x / y
except ValueError:
    z = 'worng'
except ZeroDivisionError:
    z = 'in'
print(z)
