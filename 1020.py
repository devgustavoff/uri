dias = int(input())

ano = dias // 365
resto_dias = dias % 365

mes = resto_dias // 30
resto_dias = resto_dias % 30

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(resto_dias))
