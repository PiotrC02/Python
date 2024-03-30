import math

liczba=int(input('Podaj liczbę całkowitą: '))
if liczba < 0:
    print(-1000)
elif liczba == 0:
    print('ZEROOOO!!!!')
elif liczba > 0 and liczba < 10:
    print(liczba)
elif liczba >= 10 and liczba <= 100:
    print('duzo')
elif liczba > 100:
    print('bardzo duzo')
