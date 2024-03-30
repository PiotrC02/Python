try:
    x = int(input('Podaj liczbę całkowitą 1: '))
    y = int(input('Podaj liczbę całkowitą 2: '))
except ValueError:
    print('To nie jest liczba całkowita!')
else:
    z = x/y
    print('Wprowadziłeś liczbę',x)
    print('Wprowadziłeś liczbę',y)
    print('Ich iloraz wynosi: ',z)
finally:
    print('Dziękuje!')
