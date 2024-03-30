def analiza(liczba):
    if liczba < 0: print(-1000)
    elif liczba == 0: print('ZEROOO!!!!')
    elif 0 < liczba < 10: print(liczba)
    elif 10 <= liczba <= 100: print('dużo')
    else: print('bardzo dużo')

liczba = int(input('Podaj liczbę całkowitą: '))
print('Analiza: ')
analiza(liczba)
