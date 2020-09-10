priceargs2 = tuple()
def totaltax(rate, priceargs2):
    sum = 0
    for i in priceargs:
        sum = sum + i
    return (rate + 1) * sum

def totaltax(rate, *priceargs):
    sum = 0
    for i in priceargs:
        sum = sum + i
    return (rate + 1) * sum