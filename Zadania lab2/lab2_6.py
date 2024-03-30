import cmath

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))

d = (b**2) - (4*a*c)
if d == 0:
    sol0 = (-b/(2*a))
    print('Rozwiązanie to: {0}+0j'.format(sol0))

else:

    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('Rozwiązania to: {0} i {1}'.format(sol1,sol2))
