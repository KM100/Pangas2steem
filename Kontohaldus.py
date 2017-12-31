from time import sleep

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
        print('Kasutaja omanik:',kasutajad[i+1])
        nr = i
        kas = 'jah'
        break
    else:
        kas = 'ei'
if kas == 'jah':
    print('SALAKOOD:')
    salakood = input()
    if salakood == kasutajad[nr+2]:
        print('\n'*100)
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
        print('Logisite kasutajasse '+id+' '+kasutajad[nr+1])
        print('Konto väärtus: '+kasutajad[nr+3]+' €.')
        print('''Käsud:
                        
                        ms-muuda SALAKOOD
                        k-kõik kasutajad
                        la(ükskõikmida peale ms,k ja mn)-lahku


''')
        mida = input()
        if mida == 'ms':
            print('Teie praegune SALAKOOD on '+kasutajad[nr+2]+'. Milleks soovite muuta?:')
            uus = input()
            print('OK')
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
            print('Salvestan...')
            kasutajad[nr+2] = uus
            fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
            for i in range(len(kasutajad)):
                fail.write(str(kasutajad[i]))
                fail.write('\n')
            fail.close()
            print('Korras.')
        elif mida == 'k':
            fail = open('kasutajad', 'r', encoding = 'UTF-8')
            kasutajad = []
            for rida in fail:
                kasutajad.append(rida.strip('\n'))
            fail.close()
            for i in range(len(kasutajad)):
                print(kasutajad[i])
    else:
        print('Vale SALAKOOD.')
