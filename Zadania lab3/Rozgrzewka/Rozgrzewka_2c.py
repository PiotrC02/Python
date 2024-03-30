imiona=list()
imie1 = 'Paweł'
imie2 = 'Kasia'
imiona += [imie1]
imiona += [imie2]
w=len(imiona)
imiona.remove("Kasia")
imiona.append("Piotr")
print('Długość listy imion:',w)
print('Zawartość listy imion:',imiona)
