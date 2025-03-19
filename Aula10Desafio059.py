from time import sleep
cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 59', '=' * 15, f'{cores['limpa']}')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
sleep(1)
opcoes = '''
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novo números
5 - Sair
   
Qual opção você deseja? '''
opcao = int(input(f'{opcoes}'))
sleep(1)

if opcao == 1:
    soma = n1 + n2
    sleep(1)
    print(f'A soma é: {soma}.')
    sleep(1)
    opcao = int(input(f'{opcoes}'))

if opcao == 2:
    mult = n1 * n2
    sleep(1)
    print(f'A multiplicação é: {mult}')
    sleep(1)
    opcao = int(input(f'{opcoes}'))

if opcao == 3:
    sleep(1)
    if n1 == n2:
        print('Os números são iguais.')            
    if n2 > n1:
        print(f'O maior número é {n2}.')
    if n1 > n2:
        print(f'O maior número é {n1}.')
    sleep(1)
    opcao = int(input(f'{opcoes}'))

if opcao == 5:
    sleep(1)
    print('FIM')

while opcao == 4:
    sleep(1)
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    sleep(1)
    opcao = int(input(f'{opcoes}'))
    
    if opcao == 1:
        soma = n1 + n2
        sleep(1)
        print(f'A soma é: {soma}.')
        sleep(1)
        opcao = int(input(f'{opcoes}'))
    
    if opcao == 2:
        mult = n1 * n2
        sleep(1)
        print(f'A multiplicação é: {mult}')
        sleep(1)
        opcao = int(input(f'{opcoes}'))
    
    if opcao == 3:
        sleep(1)
        if n1 == n2:
            print('Os números são iguais.')            
        if n2 > n1:
            print(f'O maior número é {n2}.')
        if n1 > n2:
            print(f'O maior número é {n1}.')
        sleep(1)
        opcao = int(input(f'{opcoes}'))
    
    if opcao == 5:
        sleep(1)
        print('FIM')