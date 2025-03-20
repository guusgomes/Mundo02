from random import randint

crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'vm':'\033[1;31m',
       'am':'\033[1;33m',
       'az':'\033[1;34m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 58', '=' * 15, f'{crs['lp']}')

computador = randint(1, 10)
pessoa = int(input(f'''Pensei em um número de {crs['vm']}1 a 10{crs['lp']}.
Você consegue acertar? Qual seu palpite?  '''))
tentativas = 1

while pessoa != computador:

    if pessoa > computador:
        print(f'{crs['am']}Menos...{crs['lp']}')
    elif pessoa < computador:
        print(f'{crs['az']}Mais...{crs['lp']}')
    
    tentativas = tentativas + 1
    pessoa = int(input(f'Tente novamente: '))

print(f'{crs['vd']}Parabéns, você acertou!{crs['lp']} Eu pensei no número {crs['vd']}{computador}{crs['lp']}!')
print(f'Foram necessárias {crs['vm']}{tentativas}{crs['lp']} tentativas para acertar.')