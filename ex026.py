print('INÍCIO DO PROGRAMA!')
frase = str(input('Digite uma frase:')).upper().strip()
print('Verificando...')
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra a aparece na {} casa'.format(frase.find('A')+1))
print('a ultima letra A aparece na {} casa'.format(frase.rfind('A')+1))