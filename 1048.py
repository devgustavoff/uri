sal = float(input())

if sal > 0 and sal <= 400.00:
    novo_sal = sal + (sal * (15 / 100))
    reajuste = novo_sal - sal
    print('Novo salario: {:.2f}'.format(novo_sal))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 15 %')
elif sal > 400.00 and sal <= 800.00:
    novo_sal = sal + (sal * (12 / 100))
    reajuste = novo_sal - sal
    print('Novo salario: {:.2f}'.format(novo_sal))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 12 %')
elif sal > 800.00 and sal <= 1200.00:
    novo_sal = sal + (sal * (10 / 100))
    reajuste = novo_sal - sal
    print('Novo salario: {:.2f}'.format(novo_sal))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 10 %')
elif sal > 1200.00 and sal <= 2000.00:
    novo_sal = sal + (sal * (7 / 100))
    reajuste = novo_sal - sal
    print('Novo salario: {:.2f}'.format(novo_sal))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 7 %') 
else:
    novo_sal = sal + (sal * (4 / 100))
    reajuste = novo_sal - sal
    print('Novo salario: {:.2f}'.format(novo_sal))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 4 %')       