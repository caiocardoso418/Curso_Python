#salario = float(input('qual o seu salário?: R$'))
#aumento = 15/100*salario + salario
#print('um funcionário que ganhava {:.3f}, agora com o aumento de 15% ganha {:.3f}R$'.format(salario, aumento)

produto = float(input('qual o preço do produto: R$'))
parcelado = produto + (8/100)*produto
vista = produto - (15/100)*produto
print('o produtor que era R${:.3f} a vista ficara R${:.3f} e parcelado R${:.3f}'.format(produto, vista, parcelado))