cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 50', '=' * 15, f'{cores['limpa']}')

s = 0
cont = 0

for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1

print(f'A {cores['azul']}soma{cores['limpa']} dos {cores['amarelo']}{cont}{cores['limpa']} números {cores['azul']}pares{cores['limpa']} digitados é: {cores['amarelo']}{s}{cores['limpa']}.')