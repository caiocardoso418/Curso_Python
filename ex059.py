from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('_-'*10)
    soma = print('[ 1 ] somar')
    mutiplicar = print('[ 2 ] mutiplicar')
    maior = print('[ 3 ] maior')
    novos = print('[ 4 ] novos numeros')
    sair = print('[ 5 ] sair do programa')
    opcao = int(input('Qual sua opção: '))
    print('_-' * 10)
    sleep(1)
    if opcao == 1:
        print('Soma = ',n1 + n2)
    elif opcao == 2:
        print('Mutiplicação = ', n1 * n2)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('o maior é {}'.format(maior))
    elif opcao == 4:
        print('informe os numeros novamente: ')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao Invalida. tente novament!')
    sleep(1)
print('Fim do programa')