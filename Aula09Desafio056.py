cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}

print(f'{cores['titulo']}', '=' * 15, 'DESAFIO 56', '=' * 15, f'{cores['limpa']}')

idadetotal = 0
idademaisvelho = 0
menosvinte = 0
nomemaisvelho = ''

for c in range (1, 5):
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    idadetotal = idadetotal + idade
    mediaidade = idadetotal / 4

    if sexo == 'M' and idade > idademaisvelho:
        nomemaisvelho = nome
        idademaisvelho = idade
    elif sexo == 'F' and idade < 20:
        menosvinte = menosvinte + 1
    elif sexo != 'M' and sexo != 'F':
        print(f'{cores['vermelho']}Sexo digitado inválido.{cores['limpa']}')

print(f'A {cores['amarelo']}média{cores['limpa']} de idade do grupo é: {cores['amarelo']}{mediaidade:.1f} anos{cores['limpa']}.')
print(f'O {cores['vermelho']}homem mais velho{cores['limpa']} do grupo é: {cores['vermelho']}{nomemaisvelho}{cores['limpa']}, com {cores['vermelho']}{idademaisvelho}{cores['limpa']} anos.')
print(f'{cores['verde']}{menosvinte} mulher(es){cores['limpa']} do grupo tem {cores['verde']}menos de 20 anos{cores['limpa']}.')