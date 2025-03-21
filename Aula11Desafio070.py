nome = str(input('Produto: ')).strip().upper()
preco = float(input('Preço: R$ '))
total = preco
precomaisbarato = preco
nomemaisbarato = nome
quantidade = 0

if preco > 1000:
    quantidade += 1

continuar = str(input('Continuar (S/N)? ')).strip().upper()

if continuar != 'N':
    while True:
        nome = str(input('Produto: ')).strip().upper()
        preco = float(input('Preço: R$ '))
        total += preco

        if preco > 1000:
            quantidade += 1

        if preco < precomaisbarato:
            precomaisbarato = preco
            nomemaisbarato = nome

        continuar = str(input('Continuar (S/N)? ')).strip().upper()

        if continuar == 'N':
            break

print(f'Compra total: R$ {total:.2f}')
print(f'{quantidade} produtos custam mais de R$ 1000.00.')
print(f'O produto mais barato é {nomemaisbarato} custando R$ {precomaisbarato:.2f}.')
