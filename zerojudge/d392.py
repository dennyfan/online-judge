while True:
    try:
        x = input()
        l = x.split()
        lans = [int(i) for i in l]
        total = 0
        for i in lans:
            total += i
        print(total)
    except:
        break