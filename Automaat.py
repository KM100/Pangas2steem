from time import sleep
from random import randint

print('''Käsud:
            
            a-ava konto
            l-loo konto




''')
s = input()
if s == 'l':
    fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
    kasutajad = []
    for rida in fail:
        kasutajad.append(rida.strip('\n'))
    fail.close()
    fail = open('jäätiskoer', 'a', encoding = 'UTF-8')
    print('Sisestage oma täisnimi:')
    nimi = input()
    id = randint(10000, 99999)
    while id in kasutajad:
        id = randint(10000, 99999)
    fail.write(str(id))
    fail.write('\n')
    fail.write(nimi)
    fail.write('\n')
    salakood = randint(1000, 9999)
    while salakood in kasutajad:
        salakood = randint(1000, 9999)
    fail.write(str(salakood))
    fail.write('\n')
    fail.write('100')
    print('Teie ID on',id)
    print('Teie SALAKOOD on',salakood)
    print('Jätke need endale meelde.')
    fail = open('kasutajad', 'a', encoding = 'UTF-8')
    fail.write(nimi)
    fail.write(' ')
    fail.write('ID: ')
    fail.write(str(id))
    fail.write('\n')
    fail.close()
elif s == 'a':
    print('ID:')
    id = input()
    fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
    kasutajad = []
    for rida in fail:
        kasutajad.append(rida.strip('\n'))
    fail.close()
    for i in range(int(len(kasutajad)/4)):
        if kasutajad[i*4] == id:
            print('Kasutaja '+id+' tuvastatud.')
            print('Kasutaja omanik:',kasutajad[i*4+1])
            nr = i*4
            kas = 'jah'
            break
        else:
            kas = 'ei'
    if kas == 'jah':
        print('SALAKOOD:')
        salakood = input()
        if salakood == kasutajad[nr+2]:
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
            print('\n'*100)
            print('Logisite kasutajasse '+id+' '+kasutajad[nr+1])
            print('Konto väärtus: '+kasutajad[nr+3]+' €.')
            print('''Käsud:
                l-lahku
                ü-tee ülekanne
                


''')
            k = input()
            if k == 'l':
                pass
            elif k == 'ü':
                fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
                kasutajad = []
                for rida in fail:
                    kasutajad.append(rida.strip('\n'))
                fail.close()
                print('Kui suure ülekande soovite teha?:')
                kui = input()
                if int(kui) > int(kasutajad[nr+3]):
                    print('Raha ei jätku.')
                else:
                    print('Kas olete kindel (ok/ei)')
                    kas = input()
                    if kas == 'ei':
                        print('Tühistatud.')
                    else:
                        print('Kellele(ID):')
                        id2 = input()
                        for i in range(len(kasutajad)):
                            if kasutajad[i] == id2:
                                print('Tuvastatud.')
                                nr1 = i
                                kas = 'jah'
                                break
                            else:
                                kas = 'ei'
                        if kas == 'jah':
                            kasutajad[nr+3] = int(kasutajad[nr+3]) - int(kui)
                            kasutajad[nr1+3] = int(kasutajad[nr1+3]) + int(kui)
                            fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
                            for i in range(len(kasutajad)):
                                fail.write(str(kasutajad[i]))
                                fail.write('\n')
                            fail.close()
                            print('Ülekanne sooritatud.')
                        else:
                            print('Tundmatu ID.')
        else:
            print('Vale SALAKOOD.')
    else:
        print('Tundmatu ID.')