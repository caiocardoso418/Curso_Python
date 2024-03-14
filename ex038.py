num = int(input('primeiro numero:'))
num2 = int(input('segundo numero:'))
if num > num2:
    print('o primeiro valor é maior')
elif num2 > num:
    print('o segundo valor é maior')
elif num2 == num:
    print('os dois numeros sao valores iguais')
else:
    print('ERRO! TENTE NOVAMENTE!')