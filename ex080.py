#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = list()
quantidade_numeros = 0
while True:
    n = input('digite um numero: ')
    numeros.append(n)
    resposta = input('deseja constinuar? [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break
    if resposta == 'S':
        quantidade_numeros += 1
print(numeros)
numeros.sort(reverse=True)
print(f'A) Foram add {quantidade_numeros+1} números a lista')
print(f'B) lista de fora derescente: {numeros}')
if 5 in numeros:
    print('C) o valor 5 foi digitado e esta na lista')
else:
    print('C) o valor 5 não foi digitado e não esta na lista')
