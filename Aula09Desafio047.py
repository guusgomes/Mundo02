cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 47', '=' * 15, f'{cores['limpa']}')

for c in range(2, 51, 2):
    print(c)