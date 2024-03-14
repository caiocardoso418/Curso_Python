frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('a frase nao é')