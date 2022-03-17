valor = int(input())

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

nota_1 = int(resto_valor / 1)
resto_valor = resto_valor % 1

print(valor)
print('{} nota(s) de R$ 100,00'.format(nota_100))
print('{} nota(s) de R$ 50,00'.format(nota_50))
print('{} nota(s) de R$ 20,00'.format(nota_20))
print('{} nota(s) de R$ 10,00'.format(nota_10))
print('{} nota(s) de R$ 5,00'.format(nota_5))
print('{} nota(s) de R$ 2,00'.format(nota_2))
print('{} nota(s) de R$ 1,00'.format(nota_1))