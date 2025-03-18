cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 49', '=' * 15, f'{cores['limpa']}')
print(f'{cores['azul']}TABUADA{cores['limpa']}')

n = int(input('Digite um número inteiro: '))

for c in range(1, 11):
    print(f'{cores['amarelo']}{n}{cores['limpa']} X {cores['amarelo']}{c:>2}{cores['limpa']} = {cores['azul']}{n * c:>3}{cores['limpa']}')