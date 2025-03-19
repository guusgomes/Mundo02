cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 55', '=' * 15, f'{cores['limpa']}')

maispesado = 0
maisleve = 0

for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maispesado = peso
        maisleve = peso
    else:
        if peso > maispesado:
            maispesado = peso
        elif peso < maisleve:
            maisleve = peso

print(f'O {cores['vermelho']}maior{cores['limpa']} peso digitado foi: {cores['vermelho']}{maispesado:.2f}kg{cores['limpa']}.')
print(f'O {cores['verde']}menor{cores['limpa']} peso digitado foi: {cores['verde']}{maisleve:.2f}kg{cores['limpa']}.')