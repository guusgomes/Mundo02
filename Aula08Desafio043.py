cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'magenta':'\033[1;35m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 43', '=' * 6, f'{cores['limpa']}')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu imc é: {cores['amarelo']}{imc:.2f}{cores['limpa']}. Você está {cores['amarelo']}ABAIXO{cores['limpa']} do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é: {cores['verde']}{imc:.2f}{cores['limpa']}. Você está no {cores['verde']}PESO IDEAL{cores['limpa']}.')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é: {cores['amarelo']}{imc:.2f}{cores['limpa']} Você está com {cores['amarelo']}SOBREPESO{cores['limpa']}.')
elif imc >= 30 and imc < 40:
    print(f'Seu imc é: {cores['magenta']}{imc:.2f}{cores['limpa']}. Você está com {cores['magenta']}OBESIDADE{cores['limpa']}.')
else:
    print(f'Seu imc é: {cores['vermelho']}{imc:.2f}{cores['limpa']}. Você está com {cores['vermelho']}OBESIDADE GRAVE{cores['limpa']}.')