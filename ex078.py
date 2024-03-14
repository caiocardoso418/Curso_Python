#Faça um programa em que leia 5 valores e guardeos em uma lista
#no final, mostre maior e menor valor digitado em suas respectivas posições
maior = 0
menor = 0
lista = []
for n in range(0,5):
    lista.append(input(f'digite um numero para a {n} posição:'))
#para saber qual é o maior e o menor numero
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print(f'Lista : {lista}')
for i,v in enumerate(lista):
    if v == maior:
        print(f'O maior numero é o {maior} na pocisao {i}')
print()
for i, v in enumerate(lista):
    if v == menor:
        print(f'o menor valor é o {menor} na pocisção {i}')
print()