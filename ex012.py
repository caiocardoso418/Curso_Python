altura = float(input("qual a altura da parede:"))
comprimento = float(input("Qual o comprimento da parede:"))
print('Sua parede tem a dimenção de {} x {} e sua area é de {}m²'.format(altura,comprimento, altura*comprimento))
print('Para pintar sua parede voce precisara de {}L de tinta'.format(altura*comprimento/2))
