from random import randint

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 44', '=' * 6, f'{cores['limpa']}')

usuario = int(input(f'''      {cores['vermelho']}JOKENPÔ!{cores['limpa']}
      {cores['azul']}1{cores['limpa']} - {cores['azul']}Pedra{cores['limpa']};
      {cores['magenta']}2{cores['limpa']} - {cores['magenta']}Papel{cores['limpa']};
      {cores['ciano']}3{cores['limpa']} - {cores['ciano']}Tesoura{cores['limpa']};
      {cores['amarelo']}Qual você escolhe?{cores['limpa']} '''))

computador = randint(1, 3)

if usuario == 1:
    if computador == 1:
        print(f'Eu também escolhi {cores['azul']}pedra{cores['limpa']}, {cores['amarelo']}EMPATAMOS{cores['limpa']}!')
    elif computador == 2:
        print(f'ISSO! Eu pensei em {cores['magenta']}papel{cores['limpa']}! Você {cores['vermelho']}PERDEU{cores['limpa']}!')
    elif computador == 3:
        print(f'Droga! Eu pensei em {cores['ciano']}tesoura{cores['limpa']}. Você {cores['verde']}VENCEU{cores['limpa']}!')
elif usuario == 2:
    if computador == 2:
        print(f'Eu também escolhi {cores['magenta']}papel{cores['limpa']}, {cores['amarelo']}EMPATAMOS{cores['limpa']}!')
    elif computador == 3:
        print(f'ISSO! Eu pensei em {cores['ciano']}tesoura{cores['limpa']}! Você {cores['vermelho']}PERDEU{cores['limpa']}!')
    elif computador == 1:
        print(f'Droga! Eu pensei em {cores['azul']}pedra{cores['limpa']}. Você {cores['verde']}VENCEU{cores['limpa']}!')
elif usuario == 3:
    if computador == 3:
        print(f'Eu também escolhi {cores['ciano']}tesoura{cores['limpa']}, {cores['amarelo']}EMPATAMOS{cores['limpa']}!')
    elif computador == 2:
        print(f'ISSO! Eu pensei em {cores['azul']}pedra{cores['limpa']}! Você {cores['vermelho']}PERDEU{cores['limpa']}!')
    elif computador == 1:
        print(f'Droga! Eu pensei em {cores['magenta']}papel{cores['limpa']}. Você {cores['verde']}VENCEU{cores['limpa']}!')
else:
    print(f'{cores['vermelho']}Opção inválida{cores['limpa']}, tente novamente!')

print(f'{cores['amarelo']}Obrigado por jogar!{cores['limpa']}')