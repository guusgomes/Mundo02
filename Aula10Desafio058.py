from random import randint
cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 58', '=' * 15, f'{cores['limpa']}')

computador = randint(1, 10)
pessoa = int(input('Adivinhe o número de 1 a 10: '))
tentativas = 0

while pessoa != computador:
    tentativas = tentativas + 1
    pessoa = int(input('Você errou, tente novamente: '))

print(f'Parabéns, você acertou! Eu pensei no número {computador}!')
print(f'Foram necessárias {tentativas} tentativas para acertar.')