n = 0
soma = 0
tentativas = 0

while n != 999:
    tentativas = tentativas + 1
    n = int(input('Digite um número: '))
    soma = soma + n

print(f'Você digitou {tentativas - 1} números antes de acertar!')
print(f'A soma dos números digitados antes de acertar é: {soma - 999}.')