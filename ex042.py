print('-_-'*20)
print('{}INÍCIO DO PROGRAMA'.format(' '*20))
print('-_-'*20)
r1 = float(input('r1:'))
r2 = float(input('r2'))
r3 = float(input('r3'))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('os segmentos podem formar um triangulo', end='')
    if r1 == r2 and r2 == r3:
        print('Equilatero')
    if r1 != r2 != r3 != r1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('os segmentos NAO podem formar um triangulo')