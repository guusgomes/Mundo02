#cont = 1
#while True:
#    print(cont, ' ', end='- ')
#    cont = cont + 1
#    if cont == 10:
#        print(cont, ' ', end='- ')
#        break
#
#print('FIM.')

n = s = 0

while True:
    
    n = int(input('Digite um número: '))
    
    if n == 999:
        break
    
    s += n

print(f'A soma dos números é: {s}.')