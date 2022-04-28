n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4) / 10

if media >= 7.0:
  print('Media: {:.1f}'.format(media))
  print('Aluno aprovado.')
elif media < 5.0:
  print('Media: {:.1f}'.format(media))
  print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
  nota_exame = float(input())
  nova_media = (media + nota_exame) / 2
  print('Media: {:.1f}'.format(media))
  print('Aluno em exame.')
  print('Nota do exame:', nota_exame)
  if nova_media >= 5.0:
    print('Aluno aprovado.')
    print('Media final: {:.1f}'.format(nova_media))
  else:
    print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(nova_media))