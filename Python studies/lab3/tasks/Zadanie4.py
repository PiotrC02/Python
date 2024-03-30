def funkcja(): #zdefiniowanie funkcji
    with open("imiona.txt","r",encoding="utf-8") as file: #otworzenie pliku tekstowego
        imiona=[] #lista imion
        for lista in file:
            imiona.append(lista) #dodanie imion z listy z pliku tekstowego
    for imie in imiona:
        imie.strip() #do usunięcia spacji
        print(imie,end="")
funkcja() #wywołanie funkcji
