import math
class wektor(object):
    def __init__(self, x=1,y=1):
        self.x=x
        self.y=y
    def dlugosc(self):
        return math.hypot(self.x,self.y)
    def obrot(self, p=1,q=1):
        p = self.x * math.cos(math.degrees(3)) - self.y * math.sin(math.degrees(3))
        q = self.y * math.sin(math.degrees(3)) + self.x * math.cos(math.degrees(3))
        return math.degrees(3)
    def __add__(self,other):
        return wektor(self.x+other.x, self.y+other.y)
    def __str__(self):
        return ("Wektor(%g,%g)" % (self.x,self.y))
    def __repr__(self):
        return ("Wektor(%g,%g)" % (self.x,self.y))
help(object)

w1 = wektor()
w2 = wektor(2,2)
w3 = w1+w2
w4 = wektor(-3,3)
print('wektor w1=', w1, 'ma długość', w1.dlugosc())
print('wektor w2=', w2, 'ma długość', w2.dlugosc())
print('wektor w3=', w3, 'ma długość', w3.dlugosc())
print('wektor w4=', w4, 'ma długość', w4.dlugosc(), 'i ma stopni: ', w4.obrot())
