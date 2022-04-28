n1, n2, n3 = input().split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

lista = [n1, n2, n3]
lista_new = sorted(lista)

i = 0
while i <= 2:
    print(lista_new[i])
    i = i + 1
print('')
i = 0
while i <= 2:
    print(lista[i])
    i = i + 1
