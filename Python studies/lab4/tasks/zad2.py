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
    def dystans(self): #zwraca odległośc między dwoma punktami
        z = math.sqrt((self.x-w2.x)**2 + (self.y-w2.y)**2) #pierwiastek kwadratowy z sumy kwadratów różnicy argumentów pomiędzy dwoma punktami
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
    
print(str(Kolo()))
print(repr(Kolo()))
