numero_extenso = ('zero','um','dois','tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
            'onze', 'doze', 'treze', 'quatroze', 'quinze'
            'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

pedir_numero = int(input('Digite um número entre 0 a 20: '))
print(f'você digitou o numero {numero_extenso[pedir_numero]}')
while True:
    if pedir_numero > 20 or pedir_numero < 0:
        pedir_numero = int(input('ERRO! Tente novamente: Digite um número entre 0 a 20: '))
    else:
        break

