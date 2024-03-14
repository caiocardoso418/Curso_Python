#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    n = (input(f'Digite um numero:'))
    if n not in numeros:
        numeros.append(n)
    else:
        print('valor duplicado')

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

print(sorted(numeros))
