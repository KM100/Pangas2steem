from random import randint
from time import sleep

print('v1.0')
fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
kasutajad = []
for rida in fail:
    kasutajad.append(rida.strip('\n'))
fail.close()
print('ID:')
id = input()
for i in range(len(kasutajad)):
    if kasutajad[i] == id:
        print('Kasutaja '+id+' tuvastatud.')
        print('Kasutaja omanik:', kasutajad[i+1])
        nr = i
        print(nr)
        kas = 'jah'
        break
    else:
        kas = 'ei'
if kas == 'jah':
    print('SALAKOOD:')
    salakood = input()
    if salakood == 'teremaailm':
        print('Palun oodake.')
        sleep(0.5)
        print('\n'*100)
        print('Palun oodake..')
        sleep(0.5)
        print('\n'*100)
        print('Palun oodake...')
        sleep(0.5)
        print('\n'*100)
        print('Palun oodake.')
        sleep(0.5)
        print('\n'*100)
        print('Palun oodake..')
        sleep(0.5)
        print('\n'*100)
        print('Palun oodake...')
        sleep(0.5)
        print('\n'*100)
        print('Logisite kasutajasse '+id+' '+kasutajad[nr+1])
        print('Konto väärtus: '+kasutajad[nr+3]+' €.')
        print('\n'*100)
        print('Kas soovite kasutajat uuendada (u) või eemaldada (e)?:')
        k = input()
        if k == 'u':
            print('Uuendatava kasutaja ID:')
            id2 = input()
            for i in range(len(kasutajad)):
                if kasutajad[i] == id2:
                    kas = 'jah'
                    nr2 = i
                    break
                else:
                    kas = 'ei'
            if kas == 'jah':
                print('Uuendan.')
                kasutajad[nr2] = randint(10000, 99999)
                fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
                for i in range(len(kasutajad)):
                    fail.write(str(kasutajad[i]))
                    fail.write('\n')
                fail.close()
                print('Salvestatud.')
                print('\n'*100)
                print('Teie uus ID on '+str(kasutajad[nr2])+'.')
            elif kas == 'ei':
                print('Tundmatu ID.')
        elif k == 'e':
            print('Eemaldatava kasutaja ID:')
            id = input()
            for i in range(len(kasutajad)):
                if kasutajad[i] == id:
                    print('Kasutaja '+id+' tuvastatud.')
                    print('Sisselogimine vajalik.')
                    kas = 'jah'
                    nr = i
                    break
                else:
                    kas = 'ei'
            print('SALAKOOD:')
            salakood = input()
            if salakood == kasutajad[nr+2]:
                print('Eemaldan.')
                for i in range(4):
                    kasutajad.remove(kasutajad[nr])
                fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
                for i in range(len(kasutajad)):
                    fail.write(str(kasutajad[i]))
                    fail.write('\n')
                fail.close()
                print('Kasutaja '+id+' eemaldatud.')
            else:
                print('Sisselogimine ebaõnnestus.')
    else:
        print('Vale SALAKOOD.')
else:
    print('Tundmatu ID.')