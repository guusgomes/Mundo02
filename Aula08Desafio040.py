cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 40', '=' * 6, f'{cores['limpa']}')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5.00:
    print(f'Média: {cores['vermelho']}{media:.2f}{cores['limpa']}. {cores['vermelho']}REPROVADO{cores['limpa']}!')
elif media >= 5.00 and media < 7.00:
    print(f'Média: {cores['amarelo']}{media:.2f}{cores['limpa']}. {cores['amarelo']}RECUPERAÇÃO{cores['limpa']}!')
else:
    print(f'Média: {cores['verde']}{media:.2f}{cores['limpa']}. {cores['verde']}APROVADO{cores['limpa']}!')