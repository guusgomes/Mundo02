cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 36', '=' * 6, f'{cores['limpa']}')

valor = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = valor / (anos * 12)

if prestacao <= salario * 0.30:
    print(f'Empréstimo {cores['verde']}APROVADO{cores['limpa']}. O valor da sua prestação é {cores['amarelo']}R$ {prestacao:.2f}{cores['limpa']}.')
else:
    print(f'Empréstimo {cores['vermelho']}NEGADO{cores['limpa']}. O valor da prestação excede 30% do seu salário.')