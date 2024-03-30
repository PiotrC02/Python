s = {} #stworzenie słownika
s[0] = 'Zero'
s[1] = 'Jeden'
s[2] = 'Dwa'
s[3] = 'Trzy'
s[4] = 'Cztery'
s[5] = 'Pięć'
s[6] = 'Sześć'
s[7] = 'Siedem'
s[8] = 'Osiem'
s[9] = 'Dziewięć'
podana = int(input('Podaj cyfrę: '))
for cyfra in s:
    if cyfra == podana:
        print(s[cyfra])
