def iter_fac(n):
    s = 1 
    for i in range(2, n+1):
        s *= i
    return s

def iter_fac2(n):
    s = 1 
    while n >= 2:
        s *= n
        n -= 1
    return s

def rec_fac(n):
    if n < 2:
        return 1
    else:
        return n * rec_fac(n-1)

def rec_fac2(n):
    return 1 if n < 2 else n * rec_fac2(n-1)
