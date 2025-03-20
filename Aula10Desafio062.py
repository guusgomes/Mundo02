crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'vm':'\033[1;31m',
       'am':'\033[1;33m',
       'az':'\033[1;34m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 62', '=' * 15, f'{crs['lp']}')

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1
total = 0
mais = 10

while mais != 0:

    total = total + mais

    while cont <= total:
        print(f'{crs['vd']}{termo}{crs['lp']} - ', end='')
        termo = termo + r
        cont = cont + 1

    print(f'{crs['az']}PAUSA{crs['lp']}')

    mais = int(input('Quantos termos deseja mostrar a mais? '))

print(f'{crs['am']}Progressão finalizada com {crs['vm']}{total}{crs['am']} termos mostrados.{crs['lp']}')
print(f'{crs['vm']}FIM.{crs['lp']}')