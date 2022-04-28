import calendar

i = 'sim'

while i == 'sim' or i == 'Sim' or i == 'S' or i == 's':
    ano = int(input('Informe o ano: '))
    mes = int(input('Informe o mes: '))
    print(calendar.month(ano, mes))
    i = input('Deseja verificar outro calendario?[S/N] ')
