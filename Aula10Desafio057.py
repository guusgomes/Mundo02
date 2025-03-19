cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 57', '=' * 15, f'{cores['limpa']}')

sexo = str(input('Digite seu sexo (M/F): ')).upper()
repete = 1

while repete == 1:
    if sexo == 'M' or sexo == 'F':
        sexo = str(input('Digite seu sexo (M/F): ')).upper()
    else:
        print('Digite o sexo correto, M para masculino e F para feminino.')
        sexo = str(input('Digite seu sexo (M/F): ')).upper()