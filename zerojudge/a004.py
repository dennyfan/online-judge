while True:
    try:
        def leap(year):
                if (year % 400 == 0): return True
                else:
                    if(year % 4 != 0): return False
                    else:
                        if (year % 100 == 0): return False
                        else: return True
        x = int(input())
        if leap(x) == True:
            print('閏年')
        else:
            print('平年')
    except:
        break
