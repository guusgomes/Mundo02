n = int(input('Digite um número: '))
opcao = str(input('Deseja continuar? (S/N) ')).upper()
soma = n
contador = 1
maior = n
menor = n
media = soma / contador

while opcao == 'S':

    n = int(input('Digite um número: '))
    contador = contador + 1
    soma = soma + n
    media = soma / contador

    if n > maior:
        maior = n
    if n < menor:
        menor = n
    
    opcao = str(input('Deseja continuar? (S/N): ')).upper()

if opcao == 'N':

    print(f'A média dos valores digitados é: {media}.')
    print(f'O maior número digitado foi {maior}.')
    print(f'O menor número digitado foi: {menor}.')

    if maior == menor:
        print(f'Os números digitados são iguais!')

if opcao != 'S' and opcao != 'N':
    print('Esta opção não existe. Tente novamente!')   