from datetime import date
atual = date.today().year
nascimento = int(input('Em que ano você nasceu: '))
categoria = atual - nascimento
print('Você tem {} anos'.format(categoria))
if categoria <= 9:
    print('Categoria: MIRIM')
elif categoria >9 and categoria <= 14:
    print('Categoria: INFANTIL')
elif categoria >14 and categoria <= 19:
    print('Categoria: JÚNIOR')
elif categoria >19 and categoria <= 25:
    print('Categoria: SÊNIOR')
elif categoria >25:
    print('Categoria: MASTER')
else:
    print('ERRO! Tente novamente!')