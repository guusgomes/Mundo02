crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'vm':'\033[1;31m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 63', '=' * 15, f'{crs['lp']}')

termos = int(input('Quantos termos você quer mostrar? ')) - 2
cont = 1
pt = 0
st = 1

print(f'{crs['vd']}{pt}{crs['lp']} - {crs['vd']}{st}{crs['lp']} - ', end='')

while cont <= termos:
    tt = pt + st
    print(f'{crs['vd']}{tt}{crs['lp']}', end=' - ')
    cont = cont + 1
    pt = st
    st = tt
    
print(f'{crs['vm']}FIM.{crs['lp']}')