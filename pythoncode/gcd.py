a = input('one')
b = input('two')
m = int(a)
n = int(b)
def gcd(m, n):
    if n == 0:
         
        print(m)
    else:
        print(gcd(n, m%n))
print(gcd(m, n))


