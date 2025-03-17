cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 42', '=' * 6, f'{cores['limpa']}')

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite outro comprimento: '))
r3 = float(input('Digite o último comprimento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r1 == r3:
        print(f'As retas digitadas formam um triângulo {cores['verde']}EQUILÁTERO{cores['limpa']}!')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print(f'As retas digitadas formam um triângulo {cores['verde']}ISÓSCELES{cores['limpa']}!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print(f'As retas digitadas formam um triângulo {cores['verde']}ESCALENO{cores['limpa']}!')
else:
    print(f'As retas digitadas {cores['vermelho']}NÃO FORMAM{cores['limpa']} um triângulo!')