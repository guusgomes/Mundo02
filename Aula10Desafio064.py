crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'am':'\033[1;33m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 64', '=' * 15, f'{crs['lp']}')

n = 0
soma = 0
tentativas = 0
n = int(input(f'Digite um número {crs['am']}(999 para parar){crs['lp']}: '))

while n != 999:
    soma = soma + n
    tentativas = tentativas + 1
    n = int(input(f'Digite um número {crs['am']}(999 para parar){crs['lp']}: '))

print(f'Você digitou {crs['am']}{tentativas}{crs['lp']} números e a soma deles é: {crs['vd']}{soma}{crs['lp']}!')