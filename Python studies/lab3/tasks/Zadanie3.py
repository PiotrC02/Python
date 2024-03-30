import itertools #importowanie biblioteki
imiona = [] #stworzenie listy imion
for i in itertools.count(start=1): #pętla, dzięki której po napisaniu 'koniec' program zakończy działanie
    imię = (input("Podaj imię: "))
    z = imię.lower() #zwraca ciąg (string), w którym wszystkie znaki są małymi literami
    if z == "koniec": #po napisaniu koniec kończy działanie program
        break
    else:
        x = imię.isalpha() #w celu wykrycia czy składa się tylko z liter
        if x == True:
            y = imię.capitalize() #Wielka litera pierwszej litery
            if y in imiona:
                print("To imię już zostało podane.")
            else:
                imiona.append(y) #dodaje element (imię) na końcu listy
        else:
            print("Podane imię jest błędne.")
print("Oto twoja lista imion: ", "\n", imiona)
plik = open(r"imiona.txt", "w") #zapisywanie do pliku tekstowego
for i in imiona:
    plik.write(i)
    plik.write("\n") #zapisuje imiona po kolei w nowych wierszach
plik.close()
