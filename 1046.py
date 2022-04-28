
hora_inicial, hora_final = input().split()


hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

if hora_inicial > hora_final:
    hora_inicial = 24 - hora_inicial
    duracao = hora_inicial + hora_final
    print('O JOGO DUROU {} HORA(S)'.format(duracao))
elif hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
    print('O JOGO DUROU {} HORA(S)'.format(duracao))
elif hora_inicial == hora_final:
    duracao = 24
    print('O JOGO DUROU {} HORA(S)'.format(duracao))