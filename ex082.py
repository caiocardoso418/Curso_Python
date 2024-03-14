#Crie um programa que vai ler vários números e colocar em uma lista. Depois
#disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = list()
pares = list()
imapares = list()

while True:
    n = input('Digite um numero: ')
    numeros.append(int(n))
    opcao = input('Quer continuar? S/N: ').strip().upper()
    if opcao != 'S':
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        imapares.append(v)

print(f'Numeros da lista: {numeros}')
print(f'Numeros pares: {pares}')
print(f'Numeros ímpares: {imapares}')

