a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

lista = [a, b, c]
lista.sort(reverse = True)


if lista[0] >= lista[1] + lista[2]:
    print('NAO FORMA TRIANGULO')
elif pow(lista[0],2) == pow(lista[1],2) + pow(lista[2],2):
    print('TRIANGULO RETANGULO')
elif pow(lista[0],2) > pow(lista[1],2) + pow(lista[2],2):
    print('TRIANGULO OBTUSANGULO')
elif pow(lista[0],2) < pow(lista[1],2) + pow(lista[2],2):
    print('TRIANGULO ACUTANGULO')

if (lista[0] == lista[1] and 
    lista[0] == lista[2] and 
    lista[1] == lista[2]):
    print('TRIANGULO EQUILATERO')

if lista[0] == lista[1] and lista[0] != lista[2]:
    print('TRIANGULO ISOSCELES')
if lista[0] == lista[2] and lista[0] != lista[1]:
    print('TRIANGULO ISOSCELES')
if lista[1] == lista[2] and lista[1] != lista[0]:
    print('TRIANGULO ISOSCELES')
