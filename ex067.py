while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(0,11):
        print(f'{n} x {c} = {n*c}')
print('Seu programa encerrou')