sal = float(input())

if sal >= 0.00 and sal <= 2000.00:
  print('Isento')
elif sal > 2000.00 and sal <= 3000.00:
  renda_1 = sal - 2000.00
  imposto = (renda_1 + (renda_1 * (8/100))) - renda_1
  print('R$ {:.2f}'.format(imposto))
elif sal > 3000.00 and sal <= 4500.00:
  renda_2 = sal - 2000.00
  renda_2 = renda_2 - 1000.00
  imposto = (renda_2 + (renda_2 * (18/100))) - renda_2
  imposto_2 = (1000.00 + (1000.00 * (8/100))) - 1000.00
  imposto = imposto + imposto_2
  print('R$ {:.2f}'.format(imposto))
elif sal > 4500.00:
  renda_3 = sal - 2000.0
  renda_3 = renda_3 - 1000.00
  renda_3 = renda_3 - 1500.00
  new_sal = sal - 20
  imposto = (renda_3 + (renda_3 * (28/100))) - renda_3
  imposto_2 = (1000.00 + (1000.00 * (8/100))) - 1000.00
  imposto_3 = (1500.00 + (1500.00 * (18/100))) - 1500.00
  imposto = imposto + imposto_2 + imposto_3
  print('R$ {:.2f}'.format(imposto))
