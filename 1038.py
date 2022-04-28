cdg, qtd = input().split()

cdg = int(cdg)
qtd = int(qtd)

if cdg == 1:
    print('Total: R$ {:.2f}'.format(qtd * 4.00))
elif(cdg == 2):
    print('Total: R$ {:.2f}'.format(qtd * 4.50))
elif(cdg == 3):
    print('Total: R$ {:.2f}'.format(qtd * 5.00))
elif(cdg == 4):
    print('Total: R$ {:.2f}'.format(qtd * 2.00))
elif(cdg == 5):
    print('Total: R$ {:.2f}'.format(qtd * 1.50))