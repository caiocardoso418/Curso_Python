n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Alnuno REPROVADO')
elif media >= 5.0 and media < 7.0:
    print('Aluno em RECUPERAÇÂO')
elif media >= 7.0:
    print('Aluno APROVADO')
print('Sua média ficou {:.1f}'.format(media))
