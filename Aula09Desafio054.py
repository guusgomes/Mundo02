from datetime import date

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 54', '=' * 15, f'{cores['limpa']}')

anoatual = date.today().year
menores = 0
maiores = 0

for c in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = anoatual - ano
    if idade < 18:
        menores = menores + 1
    else:
        maiores = maiores + 1

print(f'{cores['vermelho']}{menores} MENORES{cores['limpa']} de idade.')
print(f'{cores['verde']}{maiores} MAIORES{cores['limpa']} de idade.')