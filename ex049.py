num = int(input('Digite um número para saber sua tabuada: '))
for tabuada in range(0,11):
    print('{} x {} = {}'.format(num, tabuada, num*tabuada))