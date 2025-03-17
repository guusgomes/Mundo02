cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 44', '=' * 6, f'{cores['limpa']}')

valor = float(input('Valor do produto: R$ '))
opcao = int(input(f'''{cores["verde"]}1 - Dinheiro/Pix{cores['limpa']};
{cores['azul']}2 - Cartão débito/crédito 1x{cores['limpa']};
{cores['amarelo']}3 - Cartão de crédito 2x{cores['limpa']};
{cores['vermelho']}4 - Cartão de crédito 3x{cores['limpa']};
Qual opção deseja? {cores['amarelo']}(1 a 4){cores['limpa']}: '''))

if opcao == 1:
    valorfinal = valor - (valor * 0.10)
    print(f'Valor final do produto: {cores["verde"]}R$ {valorfinal:.2f}{cores['limpa']}.')
elif opcao == 2:
    valorfinal = valor - (valor * 0.05)
    print(f'Valor final do produto: {cores['azul']}R$ {valorfinal:.2f}{cores['limpa']}.')
elif opcao == 3:
    print(f'Valor final do produto: {cores['amarelo']}R$ {valor:.2f}{cores['limpa']}.')
elif opcao == 4:
    valorfinal = valor + (valor * 0.20)
    print(f'Valor final do produto: {cores['vermelho']}R$ {valorfinal:.2f}{cores['limpa']}.')
else:
    print(f'{cores['vermelho']}Opção inválida{cores['limpa']}, tente novamente.')