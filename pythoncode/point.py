import math
class point:
    count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.sqrt(x**2 + y**2)
        self.serial = point.count
        point.count += 1
    @property
    def theta(self):
        return math.atan(self.y/self.x) * 180 / math.pi
    def __repr__(self):
        return f'point({self.x}, {self.y})'
    def moveby(self, dx, dy):#method (inside class)
        self.x += dx
        self.y += dy
    t = theta#所以可以用t表示theta
    @property
    def area_of_rectangle(self):
        return self.x * self.y
    def volume(self):
        return self.area_of_rectangle **2#not self.area_of_rectangle()
def procmove(a, dx, dy):#function (outside class)
    a.x += dx
    a.y += dy
class colorpoint(point):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self._color = color
    


