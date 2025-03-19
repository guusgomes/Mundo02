cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 51', '=' * 15, f'{cores['limpa']}')

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dt = pt + (10 - 1) * r

for c in range(pt, dt + 1, r):
    print(c, end=' - ')

print('FIM')