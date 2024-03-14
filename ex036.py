print('-_-'*20)
print('{}INÍCIO DO PROGRAMA'.format(' '*20))
print('-_-'*20)
casa = float(input('Valor da casa: R$'))
salario = float(input('Seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
exeder = salario + (30 / 100)
if salario