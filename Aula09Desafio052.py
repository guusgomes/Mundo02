cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 52', '=' * 15, f'{cores['limpa']}')

n = int(input('Digite um número inteiro: '))
cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        cont = cont + 1

if cont == 2:
    print(f'O número {cores['amarelo']}{n}{cores['limpa']} {cores['verde']}É PRIMO{cores['limpa']}!')
else:
    print(f'O número {cores['amarelo']}{n}{cores['limpa']} {cores['vermelho']}NÃO É PRIMO{cores['limpa']}!')