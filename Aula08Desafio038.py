cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 38', '=' * 6, f'{cores['limpa']}')

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro:'))

if n1 > n2:
    print(f'O {cores['amarelo']}primeiro valor{cores['limpa']} é {cores['azul']}maior{cores['limpa']}.')
elif n2 > n1:
    print(f'O {cores['amarelo']}segundo valor{cores['limpa']} é {cores['azul']}maior{cores['limpa']}.')
else:
    print(f'{cores['amarelo']}Não existe{cores['limpa']} valor maior, os dois são {cores['azul']}iguais{cores['limpa']}.')