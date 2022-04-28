
vet = []
i = 0
while i < 10:
    x = int(input())
    vet.append(x)
    if vet[i] == None or vet[i] <= 0:
        vet[i] = 1
    i = i + 1

i = 0
while i < 10:
    print('X[{}] = {}'.format(i, vet[i]))
    i = i + 1
