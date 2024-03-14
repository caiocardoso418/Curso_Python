preco = float(input('qual o preço do produto?: R$'))
desconto = (5/100)*preco
print('o produto que custava {:.3f} agora com o desconto de 5% esta por {:.3f}'.format(preco, preco-desconto))