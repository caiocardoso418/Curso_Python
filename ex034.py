print('-_-'*20)
print('{}INÍCIO DO PROGRAMA'.format(' '*20))
print('-_-'*20)
salaraio = float(input('Qual o salário do funcionário:'))
aumento = salaraio + (salaraio * 15/100)
aumento1 = salaraio + (salaraio * 10/100)
if salaraio>1250.00:
    print('seu novo salário será de R%{:.2f}'.format(aumento1))
else:
    print('seu novo salário será de R${:.2f}'.format(aumento))