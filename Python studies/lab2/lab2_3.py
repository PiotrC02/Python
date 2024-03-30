n=int(input("Podaj rok:"))

if(n%400 == 0) and (n % 100 == 0):
    print("podany rok jest rokiem przestępnym".format(n))
elif(n%4 == 0) and (n%100 != 0):
    print("podany rok jest rokiem przestępnym".format(n))
else:
    print("podany rok nie jest rokiem przestępnym".format(n))
