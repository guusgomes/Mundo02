from datetime import date

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 41', '=' * 6, f'{cores['limpa']}')

nascimento = int(input('Qual seu ano de nascimento? '))
idade = date.today().year - nascimento

if idade <= 9:
    print(f'Você tem {cores['amarelo']}{idade} anos{cores['limpa']}. {cores['azul']}MIRIM{cores['limpa']}, até {cores['amarelo']}9 anos{cores['limpa']}.')
elif idade > 9 and idade <= 14:
    print(f'Você tem {cores['amarelo']}{idade} anos{cores['limpa']}. {cores['azul']}INFANTIL{cores['limpa']}, {cores['amarelo']}10{cores['limpa']} aos {cores['amarelo']}14 anos{cores['limpa']}.')
elif idade > 14 and idade <= 19:
    print(f'Você tem {cores['amarelo']}{idade} anos{cores['limpa']}. {cores['azul']}JUNIOR{cores['limpa']}, {cores['amarelo']}15{cores['limpa']} aos {cores['amarelo']}19 anos{cores['limpa']}.')
elif idade == 20:
    print(f'Você tem {cores['amarelo']}{idade} anos{cores['limpa']}. {cores['azul']}SÊNIOR{cores['limpa']}, {cores['amarelo']}20 anos{cores['limpa']}.')
else:
    print(f'Você tem {cores['amarelo']}{idade} anos{cores['limpa']}. {cores['azul']}MASTER{cores['limpa']}, a partir de {cores['amarelo']}21 anos{cores['limpa']}.')