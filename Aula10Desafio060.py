crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'vm':'\033[1;31m',
       'am':'\033[1;33m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 60', '=' * 15, f'{crs['lp']}')

#n = int(input('Digite um número: '))
#fatorial = n
#digitado = n
#
#while n != 1:
#    fatorial = fatorial * (n - 1)
#    n = n - 1
#
#print(f'{digitado}! é igual a {fatorial}.')

n = int(input('Digite um número: '))
cont = n
fatorial = 1

print(f'{crs['vd']}{n}!{crs['lp']} = ', end='')

while cont > 0:
    print(f'{crs['am']}{cont}{crs['lp']}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial = fatorial * cont
    cont = cont - 1

print(f'{crs['vm']}{fatorial}{crs['lp']}.')