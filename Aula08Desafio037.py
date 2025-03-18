cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 37', '=' * 6, f'{cores['limpa']}')

n = int(input('Digite um número inteiro: '))
base = int(input(f'''{cores['amarelo']}1 - Binário{cores['limpa']};
{cores['azul']}2 - Octal{cores['limpa']};
{cores['verde']}3 - Hexadecimal{cores['limpa']} 
Qual será a base de conversâo? '''))

if base == 1:
    print(f'O número {cores['vermelho']}{n}{cores['limpa']} em {cores['amarelo']}binário{cores['limpa']} é: {cores['amarelo']}{bin(n)[2:]}{cores['limpa']}.')
elif base == 2:
    print(f'O número {cores['vermelho']}{n}{cores['limpa']} em {cores['azul']}octal{cores['limpa']} é: {cores['azul']}{oct(n)[2:]}{cores['limpa']}.')
elif base == 3:
    print(f'O número {cores['vermelho']}{n}{cores['limpa']} em {cores['verde']}hexadecimal{cores['limpa']} é: {cores['verde']}{hex(n)[2:]}{cores['limpa']}.')
else:
    print(f'{cores['vermelho']}Opção inválida{cores['limpa']}, tente novamente!')