cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 48', '=' * 15, f'{cores['limpa']}')

s = 0

for c in range(3, 500, 6):
    s = c + s

print(f'A {cores['azul']}soma{cores['limpa']} dos números {cores['amarelo']}ímpares{cores['limpa']} e {cores['amarelo']}múltiplos de 3{cores['limpa']} é: {cores['azul']}{s}{cores['limpa']}.')