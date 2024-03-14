n = 0
s = 0
q = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s+n
    q = n+1
print(f'Foram digitados {q} números e a soma entre eles são {s}')