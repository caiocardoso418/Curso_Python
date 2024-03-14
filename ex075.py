# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))

print(f'Os valores da tupla são: {num}')
print(f'o 9 apareceu {num.count(9)} vezes')
print(f'O 3 está n pocisão {num.index(3)+1}')
for n in num:
    if num % 2 == 0:
        print(n)
    else:
        print('Nenhum')