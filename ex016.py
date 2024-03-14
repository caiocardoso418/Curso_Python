km = float(input("Quantos Km pecorreu com o carro?:"))
dias = int(input("quantos dias você usou o carro?:"))
preco = (60*dias) + (0.15*km)
print('como você passou {} dias e andou {}Km, o preço do aluguel do seu carro ficou em R${}'.format(dias, km, preco))