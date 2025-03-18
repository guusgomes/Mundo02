cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 53', '=' * 15, f'{cores['limpa']}')

frase = str(input('Digite uma frase: ')).upper()
letras = [letra for letra in frase if letra.isalpha()]
reverso = []

for c in letras[::-1]:
    reverso = reverso + [c]

if letras == reverso:
    print(f'A frase {cores['verde']}É{cores['limpa']} um {cores['azul']}palíndromo{cores['limpa']}!')
else:
    print(f'A frase {cores['vermelho']}NÃO É{cores['limpa']} um {cores['azul']}palíndromo{cores['limpa']}!')