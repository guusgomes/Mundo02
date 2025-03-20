from time import sleep

crs = {'lp':'\033[m',
       'tt':'\033[1;31;47m',
       'vd':'\033[1;32m',
       'vm':'\033[1;31m',
       'am':'\033[1;33m',
       'az':'\033[1;34m',
       'mg':'\033[1;35m',
       'ci':'\033[1;36m'}

print(f'{crs['tt']}', '=' * 15, 'DESAFIO 59', '=' * 15, f'{crs['lp']}')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0

while opcao != 5:
    sleep(1)
    print(f'''
{crs['vd']}1 - Somar{crs['lp']}
{crs['az']}2 - Multiplicar{crs['lp']}
{crs['ci']}3 - Maior{crs['lp']}
{crs['mg']}4 - Novo números{crs['lp']}
{crs['vm']}5 - Sair{crs['lp']}
    ''') 
    
    sleep(1)
    opcao = int(input('Qual é sua opção? '))
    print(' ')

    if opcao == 1:
        soma = n1 + n2
        sleep(1)
        print(f'A soma é {crs['vd']}{soma}{crs['lp']}.')
    elif opcao == 2:
        mult = n1 * n2
        sleep(1)
        print(f'A multiplicação é {crs['az']}{mult}{crs['lp']}.')
    elif opcao == 3:
        if n1 > n2:
            sleep(1)
            print(f'O maior número é {crs['ci']}{n1}{crs['lp']}.')
        elif n1 < n2:
            sleep(1)
            print(f'O maior número é {crs['ci']}{n2}{crs['lp']}.')
        elif n1 == n2:
            sleep(1)
            print(f'Os números são {crs['am']}iguais{crs['lp']}.')
    elif opcao == 4:
        sleep(1)
        print(f'{crs['mg']}Informe os números novamente.{crs['lp']}')
        sleep(1)
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print(f'{crs['vm']}Fim do programa.{crs['lp']}')
        print(' ')
    else:
        print(f'{crs['vm']}Opção inválida, tente novamente!{crs['lp']}')

sleep(1)
print(f'{crs['am']}Até a próxima!{crs['lp']}')