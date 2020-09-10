month = int(input('month'))
year = int(input('year'))

def leap(year):
    if (year % 400 == 0):
        return True
    else:
        if(year % 4 != 0):
            return False
        else:
            if (year % 100 == 0):
                return False
            else:
                return True

#def leap(year):
    #if (year % 400 == 0):
    #   return True
    #elif (year % 4 == 0):
    #   if (year % 100 == 0): 
    #        return False
    #   else:
    #        return True
    #else:
    #   return False
def lep(year):
    return (year % 400 == 0) or \
            (year % 4 == 0) and (year % 100 != 0)

def daysinmonthyear(month, year):
    return 31 if month in [1,3,5,7,9,11] else\
           30 if month in [4,6,8,10,12] else\
           28 if not leap(year) else\
           29

x = daysinmonthyear(month, year)
print(x)
