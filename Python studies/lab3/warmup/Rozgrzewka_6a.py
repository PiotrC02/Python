f = open('plik1.txt', 'wt+')
f.write('ABCDEFGHIJKLMNOP')
f.tell()
f.seek(0)
f.read(6)
f.read()
f.write('pierwszy')
f.write('drugi')
f.write('trzeci')
f.seek(0)
f.readline()
f.readline()
f.seek(0)
f.readlines()
if not f.closed: f.close()
