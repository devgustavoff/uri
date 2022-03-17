valor = float(input())

nota_100 = int(valor / 100) 
resto_valor = valor % 100

nota_50 = int(resto_valor / 50)
resto_valor = resto_valor % 50

nota_20 = int(resto_valor / 20)
resto_valor = resto_valor % 20

nota_10 = int(resto_valor / 10)
resto_valor = resto_valor % 10

nota_5 = int(resto_valor / 5)
resto_valor = resto_valor % 5

nota_2 = int(resto_valor / 2)
resto_valor = resto_valor % 2

#------------MOEDAS---------------

moeda_1 = int(resto_valor / 1)
resto_valor = resto_valor % 1

resto_valor *= 100
    
moeda_50 = int(resto_valor / 50.0)
resto_valor = resto_valor % 50.0

moeda_20 = int(resto_valor / 25.0)
resto_valor = resto_valor % 25.0

moeda_10 = int(resto_valor / 10.0)
resto_valor = resto_valor % 10.0

moeda_05 = int(resto_valor / 5.0)
resto_valor = resto_valor % 5.0

moeda_01 = int(resto_valor / 1.0)
resto_valor = resto_valor % 1.0

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(nota_100))
print('{} nota(s) de R$ 50.00'.format(nota_50))
print('{} nota(s) de R$ 20.00'.format(nota_20))
print('{} nota(s) de R$ 10.00'.format(nota_10))
print('{} nota(s) de R$ 5.00'.format(nota_5))
print('{} nota(s) de R$ 2.00'.format(nota_2))

print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(moeda_1))
print('{} moeda(s) de R$ 0.50'.format(moeda_50))
print('{} moeda(s) de R$ 0.25'.format(moeda_20))
print('{} moeda(s) de R$ 0.10'.format(moeda_10))
print('{} moeda(s) de R$ 0.05'.format(moeda_05))
print('{} moeda(s) de R$ 0.01'.format(moeda_01))
