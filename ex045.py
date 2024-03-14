from random import randint
from time import sleep
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
opcao = int(input('Qual sua opção: '))
print('Jo')
sleep(2)
print('KEN')
sleep(2)
print('PÔ')
sleep(0.5)
computador = randint(0 , 2)
itens = ('pedra', 'papel', 'tesoura')
print('-='*20)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[opcao]))
print('-='*20)
if computador == 0:
    if opcao == 0:
        print('EMPATOU! TENTE NOVAMENTE')
    elif opcao == 1:
        print('GANHOU! PARABÈNS!')
    elif opcao == 2:
        print('PERDEU! TENTE NOVAMENTE!')
    else:
        print('invalido!')
if computador == 1:
    if opcao == 0:
        print('PERDEU! TENTE NOVAMENTE!')
    elif opcao == 1:
        print('EMPATOU! TENTE NOVAMENTE!')
    elif opcao == 2:
        print('GANHOU! PARABENS!')
    else:
        print('invalido!')
if computador == 2:
    if opcao == 0:
        print('GANHOU! PARABENS!')
    elif opcao == 1:
        print('PERDEU! TENTE NOVAMENTE!')
    elif opcao == 2:
        print('EMPATE! TENTE  NOVAMENTE!')
    else:
        print('invalido!')