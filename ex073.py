times = ('Botafogo','Palmeiras','Bragantino','Grêmio',
         'Atlético-MG','Flamengo','Athletico-PR','Fluminense',
         'Fortaleza','São Paulo','Internacional','Cuiabá',
         'Corinthians','Santos','Bahia','Vasco da Gama',
         'Cruzeiro','Goiás','Coritiba','América-MG')
print(f'Lista de times do Brasileirão 2023: {times}')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Na zona de rebaixamento estão: {times[16:20]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O flamengo esta na {times.index("Flamengo")+1} pocição')