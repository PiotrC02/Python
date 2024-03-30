import math #zaimportowanie biblioteki math
class Punkt(object): #utworzenie klasy Punkt zawierająca definicje obiektu (punkt)
    def __init__(self,x=0,y=0): #metoda specjalna służąca do ustawiania właściwości obiektu w trakcie jego tworzenia
        self.x=x
        self.y=y
    def odleglosc(self): #zwraca długość punktu od początku układu współrzędnych
        return math.hypot(self.x,self.y) #zwraca normę euklidesową, czyli pierwiastek kwadratowy z sumy kwadratów jego argumentów
    def __str__(self): #metoda specjalna, która zamienia obiekt na string
        return ("Punkt(%g, %g)" % (self.x,self.y))
    def __repr__(self): #metoda specjalna, która zwraca reprezentację danego obiektu w postaci łańcucha znaków
        return ("Punkt(%g, %g)" % (self.x,self.y))
    def dystans(self,drugi): #zwraca odległośc między dwoma punktami
        z = math.sqrt((self.x-drugi.x)**2 + (self.y-drugi.y)**2) #pierwiastek kwadratowy z sumy kwadratów różnicy argumentów pomiędzy dwoma punktami
        return z

class Kolo(Punkt): #utworzenie klasy Kolo, która dziedziczy po klasie Punkt
    def __init__(self, x=0, y=0, r=1): #płaszczyzna dwuwymiarowa i promień r
        self.x=x
        self.y=y
        self.r=r
    def __str__(self):
        return ("Koło o współrzędnych(%g,%g,%g) " % (self.x, self.y, self.r))
    def __repr__(self):
        return ("Koło o współrzędnych(%g,%g,%g) " % (self.x, self.y, self.r))
    def obwod(self): #zwraca obwód koła
        return 2 * math.pi * self.r
    def pole(self): #zwraca pole powierzchni koła
        return math.pi * self.r**2
    def przesun(self, w): #metoda przesuwająca koło na płaszczyźnie o podany wektor
        self.x += w[0]
        self.y += w[1]

k1 = Kolo(2,0,1)
print(k1)

k1.przesun((1,2))
print('Przesunięto koło!')
print(k1)

k1.przesun([-1,-1])
print('Przesunięto ponownie koło!')
print(k1)
