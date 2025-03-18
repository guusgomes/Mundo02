n = int(input('Digite um número inteiro: '))

if n <= 1:
    print('Número não primo.')
elif n == 2:
    print('Número primo.')
else:
    for c in range(2, n + 1):
        if n % c == 0:
            print('Número primo.')
        else:
            print('Número não primo.')
    