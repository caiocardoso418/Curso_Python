sexo = str(input('Digite seu sexo M/F:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Porfavor, informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso!'.format(sexo))
