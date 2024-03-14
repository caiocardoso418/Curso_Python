from random import randint
aleatorio = randint(0,10)
print('sou seu computador e acabei de pensar em um numero tente adivinhar')
acertou = False
contagem = 0
while not acertou:
    jogador = int(input('qual o seu palpite:'))
    if jogador == aleatorio:
        acertou = True
    if acertou == False:
        contagem += 1
print('Acertou')
print('você acertou {} tentativas'.format(contagem))
