# Inicializamos as variáveis para armazenar o total, a quantidade de números digitados,
# o maior e o menor número.
total = 0
quantidade = 0
maior = float('-inf')  # Inicializado com um valor muito baixo
menor = float('inf')  # Inicializado com um valor muito alto

while True:
    try:
        # Solicita ao usuário para digitar um número inteiro
        num = int(input('Digite um número inteiro: '))

        # Atualiza o total e a quantidade de números
        total += num
        quantidade += 1

        # Atualiza o maior e o menor número, se necessário
        if num > maior:
            maior = num
        if num < menor:
            menor = num

        # Pergunta ao usuário se ele quer continuar
        continuar = input('Quer continuar a digitar valores? (S/N): ').strip().upper()
        if continuar != 'S':
            break  # Sai do loop se a resposta não for 'S'
    except ValueError:
        print('Por favor, digite um número inteiro válido.')

# Calcula a média dos números
media = total / quantidade if quantidade > 0 else 0

# Mostra os resultados
print(f'Média dos números digitados: {media}')
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')
