print('-_-'*20)
print('{}INÍCIO DO PROGRAMA'.format(' '*20))
print('-_-'*20)
a = int(input('primeiro número:'))
b = int(input('segundo numero:'))
c = int(input('terceiro número:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('o menor valor é {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o maior valor é {}'.format(maior))