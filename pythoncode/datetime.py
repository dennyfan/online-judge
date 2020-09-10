def checkrange(name, value, l, u):
    if not (l <= value <= u):
        raise ValueError(f'{name} be {l}...{u}')

class Datetime:
    def __init__(self, year, month, day, hour, minute):
        self._year(year)
        self.set_month(month)
        self.set_day(day)
        self.set_hour(hour)
        self.smin(minute)
    def _year(self, year):
        if type(year) != int: raise TypeError('year must be int')
        self._year = year
    def set_month(self, month):
        checkrange('month', month, 1, 12)
        self._month = month
    def set_day(self, day):
        if self._month in {1,3,5,7,8,10,12}:checkrange('',day,1,31)
        elif self._month in {4,6,9,11}:     checkrange('',day,1,30)
        elif self._month == 2 and leap(self._year):#leap()還沒定義
            checkrange('',day,1,29)
        else:checkrange('',day,1,28)
        self._day = day
    def set_hour(self, hour):
        checkrange('', hour, 1, 24)
        self._hour = hour
    def smin(self, minute):
        checkrange('', minute, 0, 60)
        self.min = minute
    

class Datetime2:
    def checkandset(self, name, value, l, u):
        if type(name) != str:
            raise TypeError('name wromg')
        if not (l <= value <= u):
            raise ValueError(f'{name} must be {l}...{u}')
        self.__dict__['_'+ name] = value
    def __init__(self, year, month, day, hour, minute):
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)
        self.set_hour(hour)
        self.smin(minute)
    def set_year(self, year):
        if type(year) != int: raise TypeError('year must be int')
        self._year = year
    def set_month(self, month):
        self.checkandset('month', month, 1, 12)
    def set_day(self, day):
        if self._month in {1,3,5,7,8,10,12}:
            self.checkandset('day',day,1,31)
        elif self._month in {4,6,9,11}:
            self.checkandset('day',day,1,30)
        elif self._month == 2 and leap(self._year):
            self.checkandset('day',day,1,29)
        else:self.checkandset('day',day,1,28)
    def set_hour(self, hour):
        self.checkandset('h', hour, 1, 24)
    def smin(self, minute):
        self.checkandset('m', minute, 0, 60)

class Datetime3:#most completed
    year_from = -5000#
    year_to = +4000#
    def checkandset(self, name, value, l, u):
        if type(name) != str:
            raise TypeError('name wromg')
        if not (l <= value <= u):
            raise ValueError(f'{name} must be {l}...{u}')
        self.__dict__['_'+ name] = value
    def __init__(self, year, month, day, hour, minute):
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)
        self.set_hour(hour)
        self.smin(minute)
        
    @classmethod#如果不加@classmethod，改year_from、to 要用Datetime3.year_from、to = 9000(ex)\
                #加了後，可用yearrange去改year_from、to
    def yearrange(sel,l,u):#sel should be chamged with "cls", but i think it doesn't matter
        sel.year_from, sel.year_to = l, u
    def set_year(self, year):#
        self.checkandset('year', year, self.year_from, self.year_to)
    

    def get_month(self):
        return self.month#
    def set_month(self, month):
        if not (1 <= month <= 12):
            raise ValueError(f'month must be 1 ... 12')
        self.__dict__['month'] = month
    _month = property(lambda self: self.get_month(), lambda self, v: self.set_month(v))

    #def get_month(self):#原本（上面的版本為a._month可做修改,此原版為a.month可作修改,即a.month = 8可這樣改）
        #return self.month#續上,可用dt.__dict__去看
    #def set_month(self, month):
        #self.checkandset('month', month, 1, 12)
    #month = property(lambda self: slef.get._month(), lambda self, v: self.set_month(v))
    
    def set_day(self, day):
        if self.month in {1,3,5,7,8,10,12}:#原版為self._month
            self.checkandset('day',day,1,31)
        elif self.month in {4,6,9,11}:#原版為self._month
            self.checkandset('day',day,1,30)
        elif self.month == 2 and self.leap(self._year):#,#is use self.leap not cls.leap
            self.checkandset('day',day,1,29)#原版為self._month
        else:self.checkandset('day',day,1,28)
    def set_hour(self, hour):
        self.checkandset('h', hour, 1, 24)
    def smin(self, minute):
        self.checkandset('m', minute, 0, 60)
    
    @staticmethod
    def leap(year):
        if (year % 400 == 0): return True
        else:
            if(year % 4 != 0): return False
            else:
                if (year % 100 == 0): return False
                else: return True
