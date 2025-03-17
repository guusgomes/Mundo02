from datetime import date

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 39', '=' * 6, f'{cores['limpa']}')

nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento

if idade == 18:
    print(f'{cores['vermelho']}Você tem ou fará 18 anos este ano. Aliste-se já!{cores['limpa']}')
elif idade < 18:
    print(f'Você tem {cores['verde']}{idade}{cores['limpa']} anos, ainda falta(am) {cores['amarelo']}{18 - idade}{cores['limpa']} ano(os) para seu alistamento.')
else:
    print(f'Você tem {cores['amarelo']}{idade}{cores['limpa']} anos, você deveria ter se alistado há {cores['vermelho']}{idade - 18}{cores['limpa']} ano(os)!')