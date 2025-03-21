maiores = homens = mulheresmenosvinte = 0

while True:
    idade = int(input('\nIdade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()

    if idade > 18:
        maiores += 1
    
    if sexo == 'M':
        homens += 1

    if idade < 20 and sexo == 'F':
        mulheresmenosvinte += 1
    
    while True:
        if sexo != 'M' and sexo != 'F':
            sexo = str(input('Sexo (M/F): ')).strip().upper()
            if sexo == 'M':
                homens += 1
            if idade < 20 and sexo == 'F':
                mulheresmenosvinte += 1
        else:
            break

    continuar = str(input('\nQuer continuar (S/N)? ')).strip().upper()
    
    while True:
        if continuar != 'S' and continuar != 'N':
            continuar = str(input('Quer continuar (S/N)? ')).strip().upper()
        else:
            break
    
    if continuar == 'N':
        break

print(f'\nPessoas com mais de 18 anos: {maiores}.')
print(f'Homens cadastrados: {homens}.')
print(f'Mulheres com menos de 20 anos: {mulheresmenosvinte}.')
print('\nFIM.')