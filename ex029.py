print('-_-'*20)
print('INÍCIO DO PROGRAMA')
print('-_-'*20)
velocidade = float(input('Qual a velocidade que estava andando?'))
multa = (velocidade-80)*7
if velocidade > 80:
      print('MULTADO! Você exedeu o limíte permitido de 80Km/h e deverá pagar uma multa de R${:.2f}'.format(multa))
else:
      print('Tenha um bom dia! Dirija com cuidado!')
