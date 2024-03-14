num = int(input('Digiteum número:'))
print('Voce quer transformar seu numero em:'
      '\n[1] Bianario'
      '\n[2] Octal'
      '\n[3] Exadecimal')
opcao = int(input('digite aqui: '))
if opcao == 1:
    print('o numero {} em binário é {}'.format(num, bin(num)[:2]))
elif opcao == 2:
    print('o numero {} em octal é {}'.format(num, oct(num)[:2]))
elif opcao == 3:
    print('o numero {} em exadecimal é {}'.format(num, hex(num)[:2]))
else:
    print('digite 1,2 ou 3')
