from math import factorial
from time import time
def silnia_rekur(n):
    if n==0 or n==1:
        return 1
    else:
        return n*silnia_rekur(n-1)
def silnia_iter(n):
    wynik=1
    for i in range(1,n+1):
        wynik*=i
    return wynik 
i=int(input('Podaj liczbę całkowitą:'))
p_rekur = time()
w_rekur = silnia_rekur(i)
k_rekur = time()

p_iter = time()
w_iter = silnia_iter(i)
k_iter = time()

p_mat = time()
w_mat = factorial(i)
k_mat = time()

print(str(i)+"!, wynosi:", w_rekur)
print('Obliczenia rekurencyjnie trwały:',k_rekur-p_rekur,'sekund')
print('Obliczenia iteracyjnie trwały:',k_iter-p_iter,'sekund')
print('Obliczenia math.factorial trwały:',k_mat-p_mat,'sekund')
