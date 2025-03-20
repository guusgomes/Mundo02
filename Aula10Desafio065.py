crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'vm':'\033[1;31m',
       'am':'\033[1;33m',
       'az':'\033[1;34m',
       'mg':'\033[1;35m',
       'ci':'\033[1;36m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 65', '=' * 15, f'{crs['lp']}')

n = int(input('Digite um número: '))
opcao = str(input(f'Deseja continuar? {crs['am']}(S/N){crs['lp']} ')).upper()
soma = n
contador = 1
maior = n
menor = n
media = soma / contador

while opcao == 'S':

    n = int(input('Digite um número: '))
    contador = contador + 1
    soma = soma + n
    media = soma / contador

    if n > maior:
        maior = n
    if n < menor:
        menor = n
    
    opcao = str(input(f'Deseja continuar? {crs['am']}(S/N){crs['lp']}: ')).upper()

if opcao == 'N':

    print(f'A {crs['am']}média{crs['lp']} dos valores digitados é: {crs['am']}{media:.2f}{crs['lp']}.')
    print(f'O {crs['vd']}maior número{crs['lp']} digitado foi {crs['vd']}{maior}{crs['lp']}.')
    print(f'O {crs['mg']}menor número{crs['lp']} digitado foi: {crs['mg']}{menor}{crs['lp']}.')

    if maior == menor:
        print(f'{crs['am']}Os números digitados são iguais!{crs['lp']}')

if opcao != 'S' and opcao != 'N':
    print(f'{crs['vm']}Esta opção não existe. Tente novamente!{crs['lp']}')