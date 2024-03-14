print('-_-'*20)
print('{}INÍCIO DO PROGRAMA'.format(' '*20))
print('-_-'*20)
distancia = float(input('Qual a distancia da sua viagem em KM/h? '))
if distancia <= 200:
    print('o valor da passagem será R${:.2f}'.format(distancia * 0.50))
else:
    print('O valor da passagem será R${:.2f}'.format(distancia * 0.45))