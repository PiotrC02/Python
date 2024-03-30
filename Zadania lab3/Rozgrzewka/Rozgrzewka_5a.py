try:
    x = int(input('Podaj liczbę całkowitą: '))
except ValueError:
    print('To nie jest liczba całkowita!')
else:
    print('Wprowadziłeś liczbę',x)
finally:
    print('Dziękuje!')
