import random
sorteio = (random.randint(1,10),random.randint(1,10),
           random.randint(1,10),random.randint(1,10),
           random.randint(1,10))
print(f'Os numeros sorteados foram {sorteio}')
print(f'Os numeros em ordem ficam {sorted(sorteio)}')
print(f'O menor numero é o {sorted(sorteio)[0]}')
print(f'O maior numero é o {sorted(sorteio)[4]}')
