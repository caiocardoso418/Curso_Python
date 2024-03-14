mulheres = 0
mediaidade = 0
somaidade = 0
maioridade = 0
nomevelho = ''
for pessoa in range(1,5):
    print("-----{}ª PESSOA-----".format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if idade < 21 and sexo == 'F':
        mulheres += 1
    if pessoa == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
print('O homem mais velho é o {} e ele tem {} anos'.format(nomevelho, maioridade))
mediaidade = somaidade / 4
print('a media das idades são {}'.format(mediaidade))
print('ao todo sao {} mulheres com menos de 20 anos'.format(mulheres))
