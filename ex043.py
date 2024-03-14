altura = float(input('Qual sua altura: '))
peso = float(input('Qual o seu peso: '))
imc = peso / altura**2
print('Seu imc esta {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc <40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')
else:
    print('ERRO! TENTE NOVAMENTE!')