print('-_'*25)
print('           LOJA SUPER BARATÂO              ')
print('-_'*25)
produto = ''
preco = 0
total = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    total += preco
    seguir = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if seguir == 'N':
        break


print(f'O total da compra foi R${total}')
print('Temos {} produtos custando mais de 1000')