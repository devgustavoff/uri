cdg_peca1, qtd_peca1, valor_peca1 = input().split()
cdg_peca2, qtd_peca2, valor_peca2 = input().split()

print('VALOR A PAGAR : R$ {:.2f}'.format(float(valor_peca1) * int(qtd_peca1) + float(valor_peca2) * int(qtd_peca2)))
