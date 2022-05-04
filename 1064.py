valores = []
positivos = []
soma_positivos = 0

for i in range(6):
    valor = float(input())
    valores.append(valor)
    if valores[i] > 0:
        positivos.append(valores[i])
        soma_positivos = soma_positivos + valores[i] 
        
media = soma_positivos / len(positivos)

print("{} valores positivos".format(len(positivos)))
print(media)