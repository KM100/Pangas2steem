from random import choice

sõnad = ['Peedu', 'ratas', 'Tarmo', 'lill', 'jäätis', 'kana', 'kast', 'Barbie', 'patsikumm', 'kleit', 'kannab', 'elevant', 'koer', 'kingad', 'lips', 'sõna', 'Marta', 'hakib', 'rattaga', 'sõidab', 'tegi', 'aerutas', 'lendab', 'palliga', 'sõitis', 'liha', 'kloun', 'aitas', 'ka', 'söök', 'ehitab', 'kakab', 'see', 'ta', 'ma', 'Oskar', 'Kaarel', 'Veiko', 'tappis', 'Maile', 'vist', 'jah', 'ei', 'äkki', 'julgelt', 'wc', 'alasti', 'porgand', 'hüppama', 'saagis', 'rakett', 'Eesti', 'Soome', 'Venemaa', 'cd', 'trepp', 'imelik']
print('Mitu lauset moodustan?:')
lauseid = input()
for i in range(int(lauseid)):
    lause = choice(sõnad)+' '+choice(sõnad)+' '+choice(sõnad)+' '+choice(sõnad)+'.'
    lause.title()
    print(lause)