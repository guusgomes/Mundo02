from random import randint
from time import sleep

print('=--=' * 6)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=--=' * 6)

vitorias = 0

while True: 
    sleep(1)
    numcomputador = randint(0, 10)
    numpessoa = int(input('\nDigite seu número: '))

    if numpessoa > 10:
        sleep(1)
        print('\nNúmero inválido.')
        break
    
    sleep(1)
    escolha = str(input('\nPAR ou ÍMPAR (P/I)? ')).strip().upper()
    soma = numcomputador + numpessoa

    if escolha != 'P' and escolha != 'I':
        sleep(1)
        print('\nEscolha inválida.')
        break

    if soma % 2 == 0:
        parouimpar = 'PAR'
    else:
        parouimpar = 'IMPAR'

    print(f'\nVocê jogou {numpessoa} e o computador {numcomputador}. Então {numpessoa} + {numcomputador} = {soma}.')
    sleep(1)
    print(f'\nO número {soma} é {parouimpar}!')

    if escolha == 'P' and parouimpar == 'PAR':
        sleep(1)
        print('\nVocê venceu! \nVamos jogar novamente!')
        vitorias += 1
    elif escolha == 'I' and parouimpar == 'IMPAR':
        sleep(1)
        print('\nVocê venceu! \nVamos jogar novamente!')
        vitorias += 1
    else:
        sleep(1)
        print('\nVocê perdeu!')
        break

sleep(1)
print(f'\nVocê venceu {vitorias} vez(es).')
sleep(0.7)
print('\nFim do jogo.\n')