imiona = [] #stworzenie listy imion
for i in range(10): #10 razy poprosi o imię
    imię = (input("Podaj imię: "))
    if imię == "Koniec":
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
print("Oto lista imion: ", imiona)
