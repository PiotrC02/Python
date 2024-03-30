s = {'Imie':'Józef','Nazwisko':'Nowak',5:13.2}
s.keys()
s.values()
s.items()
w = s.get('Imie')
print(w)
print(s)
w = s.pop(5)
print(w)
print(s)
s['klucz1'] = 'wartosc1'
s['klucz2'] = 'wartosc2'
s['klucz3'] = 'wartosc3'
print(s)
