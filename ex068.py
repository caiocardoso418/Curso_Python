from random import randint
print('VAMOS JOGAR PAR OU IMPAR')
computador = randint(0,10)
tentativas = 0
while True:
    v = int(input('Diga um valor: '))
    pi = str(input('Par ou Impar? [P/I]')).upper().strip()
    while pi not in ['P','I']:
        print('Opção inválida. Tente novamente!')
        pi = str(input('Par ou Impar? [P/I]')).upper().strip()
    print(f'Voce jogou {v} e o computador jogou {computador}')
    soma = computador+v
    par1 = soma % 2 == 0
    if (pi == 'P' and par1) or (pi == 'I' and not par1):
        print('Ganhou')
        tentativas += 1
    else:
        break
    print('vamos jogar dnv...')
    computador = randint(0, 10)
print(f'Game Over! Você ganhou {tentativas} vezes')

