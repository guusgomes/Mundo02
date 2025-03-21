um = 0
dez = 0
vinte = 0
cinquenta = 0
valor = int(input('Qual valor deseja sacar? R$ '))

if valor < 10:
    um = valor // 1

if valor >= 10 and valor < 20:
    dez = valor // 10
    um = valor - (dez * 10) // 1

if valor >= 20 and valor < 50:
    vinte = valor // 20
    dez = (valor - (vinte * 20)) // 10
    um = (valor - ((vinte * 20) + (dez * 10))) // 1

if valor >= 50:
    cinquenta = valor // 50
    vinte = (valor - (cinquenta * 50)) // 20
    dez = (valor - ((cinquenta * 50) + (vinte * 20))) // 10
    um = (valor - ((cinquenta * 50) + (vinte * 20) + (dez * 10))) // 1

print(f'{cinquenta} notas de R$ 50.')
print(f'{vinte} notas de R$ 20.')
print(f'{dez} notas de R$ 10.')
print(f'{um} notas de R$ 1.')