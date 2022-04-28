
qtd = 0
vet = []
i = 0
while i < 6:
    x = float(input())
    vet.append(x)
    if vet[i] >= 0:
        qtd = qtd + 1
    i = i + 1

print('{} valores positivos'.format(qtd))