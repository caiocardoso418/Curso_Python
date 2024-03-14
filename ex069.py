qidade = 0
homem = 0
mulher = 0
print('-_'*40)
print('ANALISE DE GRUPO')
print('-_'*40)
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        qidade += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in ['M','F']:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-' * 30)
    if opcao == 'N':
        break
print('-_'*40)
print(f'Total de pessoas com mais de 18 anos: {qidade}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
