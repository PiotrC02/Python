x = {'jeden','dwa','trzy'}
y = {'dwa','trzy','cztery'}
x.intersection(y)
{'jeden', 'trzy'}.issubset(x)
{'jeden', 'trzy'}.issubset(y)
x|y
x&y
x^y
x-y
z={1,2,3,1,1,2,2,3,3,1,2,3,1,3,2,1,2,3}
set(z)
unique_z = list(set(z))
print('Długość:',len(unique_z),'Zbiór:',unique_z)
