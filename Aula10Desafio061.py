crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vm':'\033[1;31m',
       'am':'\033[1;33m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 61', '=' * 15, f'{crs['lp']}')

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1 

while cont <= 10:
    print(f'{crs['am']}{termo}{crs['lp']} - ', end='')
    termo = termo + r
    cont = cont + 1

print(f'{crs['vm']}FIM{crs['lp']}')