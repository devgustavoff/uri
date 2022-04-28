palavra1 = input()
palavra2 = input()
palavra3 = input()



if palavra1 == 'vertebrado':
    if palavra2 == 'ave' and palavra3 == 'carnivoro':
        print('aguia')
    elif palavra2 == 'ave' and palavra3 == 'onivoro':
        print('pomba')
    elif palavra2 == 'mamifero' and palavra3 == 'onivoro':
        print('homem')
    elif palavra2 == 'mamifero' and palavra3 == 'herbivoro':
        print('vaca')
elif palavra1 == 'invertebrado':
    if palavra2 == 'inseto' and palavra3 == 'hematofago':
        print('pulga')
    elif palavra2 == 'inseto' and palavra3 == 'herbivoro':
        print('lagarta')
    elif palavra2 == 'anelideo' and palavra3 == 'hematofago':
        print('sanguessuga')
    elif palavra2 == 'anelideo' and palavra3 == 'onivoro':
        print('minhoca')