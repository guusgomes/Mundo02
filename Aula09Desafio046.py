from time import sleep

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 46', '=' * 15, f'{cores['limpa']}')

for c in range (10, 0, -1):
    print(c)
    sleep(1)

print(f'{cores['amarelo']}FELIZ ANO NOVO!!{cores['limpa']}')