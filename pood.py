#09.12.2017
#
from tkinter import *
olemas = []
print('Teretulemast poodi!')
print('Palun oodake...')
print('Palun sisestage oma ID:')
id = input()
file = open(id, 'r', encoding = 'UTF-8')
for rida in file:
    olemas.append(rida.strip('\n'))
file.close()
print('Teil on olemas:')
for i in range(len(olemas)):
    print(olemas[i])
print('Nüüd ostma!')
asjad = ['leib', 'sai', 'piim', 'pelmeenid', 'juust', 'komm', 'jäätis', 'müsli', 'šokolaad', 'krõbinad', 'keefir', 'kala', 'vesi', 'kartul']
hinnad = ['80', '80', '100', '110', '30', '40', '45', '84', '67', '92', '100', '300', '50', '90']
fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
kasutajad = []
for rida in fail:
    kasutajad.append(rida.strip('\n'))
fail.close()
for i in range(len(kasutajad)):
    if kasutajad[i] == str(id):
        nr = i
        break
ostetud = []
hind = 0
while True:
    print('Olgu.Mida te vajate?')
    vajadus = input()
    if vajadus in asjad:
        print('Palun oodake...')
        for i in range(len(asjad)):
            if asjad[i] == vajadus:
                print('See on meil olemas.See maksab '+hinnad[i]+' €.')
                ostetud.append(vajadus)
                hind+=int(hinnad[i])
                break
    else:
        break
    i+=1
print('Maksmis aeg!')
print('Arve on '+str((hind))+' €.')

print('ID:')
id = input()
for i in range(len(kasutajad)):
        if kasutajad[i] == id:
            print('Kasutaja '+id+', tuvastatud!')
            print('Kasutaja omanik:',kasutajad[i+1])
            nr = i
            kas = 'jah'
            raha = kasutajad[nr+3]
            break
        else:
            nr = i
            kas = 'ei'
if kas == 'jah':
    print('SALAKOOD:')
    salakood = input()
    if salakood == kasutajad[nr+2]:
        print('Palun oodake...')
        print('Teostan makset...')
        if hind <= int(raha):
            kasutajad[nr+3] = int(kasutajad[nr+3])-hind
            fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
            for i in range(len(kasutajad)):
                fail.write(str(kasutajad[i]))
                fail.write('\n')
            fail.close()
            fail = open(id, 'r', encoding = 'UTF-8')
            varem = []
            for rida in fail:
                varem.append(rida.strip('\n'))
            fail.close()
            for i in range(len(varem)):
                ostetud.append(str(varem[i]))
            file = open(id, 'w', encoding = 'UTF-8')
            for i in range(len(ostetud)):
                file.write(str(ostetud[i]))
                file.write('\n')
            file.close()
            print('\n'*100)
            print('Makse sooritatud.Head päeva.')
        else:
            print('Raha ei jätku.')
    else:
        print('Makset ei sooritatud.Kasutajad ei tuvastatud.')
        















        
