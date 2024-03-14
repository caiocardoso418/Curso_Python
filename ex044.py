produto = float(input('Preço das compras: R$'))
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
pagamento = int(input('Qual é sua opção? '))
if pagamento == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(produto, produto-(produto*10/100)))
elif pagamento == 2:
    print('sua compra de R${:.2f} vai custar R${:.2f}'.format(produto, produto-(produto*5/100)))
elif pagamento == 3:
    print('Sua compra de R${} vai custar {}'.format(produto, produto))
elif pagamento == 4:
    print('Sua compra de R${} vai custar R${}'.format(produto, produto+(produto*20/100)))
else:
    pagamento = 0
    print("ERRO! TENTE NOVAMENTE")