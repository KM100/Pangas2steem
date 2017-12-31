from random import randint
from time import sleep

print('ID:')
id = input()
fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
kasutajad = []
for rida in fail:
    kasutajad.append(rida.strip('\n'))
fail.close()
for i in range(len(kasutajad)):
    if kasutajad[i] == id:
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
        print('Alustame. Teenime. Teenimiseks arva ära 4-numbriline kood ja saad 80 €. Sisesta la lahkumiseks.')
        while True:
            print('Start! Uus round!')
            kood = randint(1000, 9999)
            v = input()
            while int(v) !=kood:
                if str(v) == 'la':
                    break
                if int(v) < kood:
                    print('Kood on suurem.')
                elif int(v) > kood:
                    print('Kood on väikesem.')
                v = input()
            print('Õige. Teenisid 80 €.')
            kasutajad[nr+3] = int(kasutajad[nr+3]) + 80
            fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
            for i in range(len(kasutajad)):
                fail.write(str(kasutajad[i]))
                fail.write('\n')
            fail.close()
            print('Kas soovid lahkuda:')
            k = input()
            if k == 'la':
                break
            
        
        
        
        
        
        