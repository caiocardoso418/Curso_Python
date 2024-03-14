for pessoa in range(0,5):
    peso = int(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor < peso
print('o menor peso lido foi {}'.format(menor))
print('o maior peso lido foi {}'. format(maior))