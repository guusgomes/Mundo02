cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 60', '=' * 15, f'{cores['limpa']}')

n = int(input('Digite um número: '))
fatorial = n
digitado = n

while n != 1:
    fatorial = fatorial * (n - 1)
    n = n - 1

print(f'{digitado}! é igual a {fatorial}.')