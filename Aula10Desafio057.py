crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'vm':'\033[1;31m',
       'am':'\033[1;33m',
       'az':'\033[1;34m',
       'mg':'\033[1;35m',
       'ci':'\033[1;36m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 57', '=' * 15, f'{crs['lp']}')

#sexo = str(input('Digite seu sexo (M/F): ')).upper()
#repete = 1
#
#while repete == 1:
#    if sexo == 'M' or sexo == 'F':
#        sexo = str(input('Digite seu sexo (M/F): ')).upper()
#    else:
#        print('Digite o sexo correto, M para masculino e F para feminino.')
#        sexo = str(input('Digite seu sexo (M/F): ')).upper()

sexo = str(input(f'Digite seu sexo {crs['am']}(M/F){crs['lp']}: ')).upper().strip()

while sexo not in 'MmFf':
    
    sexo = str(input(f'{crs['vm']}Sexo inválido{crs['lp']}, digite seu sexo {crs['am']}(M/F){crs['lp']}: ')).upper().strip()

print(f'{crs['vd']}Sexo {sexo} recebido.{crs['lp']}')