cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 61', '=' * 15, f'{cores['limpa']}')

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dt = pt + (10 - 1) * r
termos = pt

print(termos, end=' - ')

while termos != dt:
    termos = termos + r
    print(termos, end=' - ')

opcao = int(input('Você quer mostrar mais quantos termos? (0 para nenhum): '))

while opcao != 0:
    novopt = dt
    novot = novopt + (opcao - 1) * r 
    
    while novopt != novot:
        termos = termos + r
        print(termos, end=' - ')


