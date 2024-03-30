import pickle #serializacja - zamiana obiektu na bajty
def sprawdzanie():
    wyjątki = ["Kosma","Barnaba","Bonawentura","Jarema","Kuba"] #wyjątki w imionach
    męskie = [] #podział na męskie
    żeńskie = [] #podział na żeńskie
    imiona = [] #lista z imionami
    with open ("imiona.txt","r",encoding="utf-8") as f: #otworzenie pliku tekstowego z enkodowaniem utf-8 (w razie zawarcia znaków polskich)
        for imie in f:
            imie_strip = imie.strip() #do usunięcia ciągu znaków
            imiona.append(imie_strip) #dodaje elementy z ciągu znaków
    for imie in imiona:
        imie_1 = imie.lower() #zwraca ciąg (string), w którym wszystkie znaki są małymi literami
        if imie_1[-1] == "a":
            try:
                index = wyjątki.index(imie_1) #wyjątki z końcówką 'a'
            except ValueError:
                żeńskie.append(imie_1)
            else:
                męskie.append(imie_1)
        else:
            męskie.append(imie_1)
    żeńskie_sort = sorted(żeńskie) #sortowanie imion
    męskie_sort = sorted(męskie)
    wyświetlanie(żeńskie_sort,męskie_sort)
    zapis(żeńskie_sort,męskie_sort)
def wyświetlanie(z,m):
    for x in z:
        print(x)
    for y in m:
        print(y)
def zapis(z,m):
    file = open("imiona.pkl","wb") #zapis do binarnego pliku
    list = [z,m]
    pickle.dump(list,file) #moduł pickle służący do serializacji listy
    file.close()
def odczyt():
    with open ("imiona.pkl","rb") as file: #odczyt z binarnego pliku
        newlist = pickle.load(file) #ładowanie listy
    for name in newlist:
        print(name)
sprawdzanie()
