import random
from time import sleep
print('-_-'*20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-_-'*20)
aleatorio = random.randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if aleatorio == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e nao no {}!'.format(aleatorio, num))
