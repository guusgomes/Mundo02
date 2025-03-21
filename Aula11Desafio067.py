from time import sleep

while True:  
    n = int(input('\nQuer ver a tabuada de qual número? '))

    if n < 0:
        break

    sleep(1)
    print('')

    for num in range(1, 11):
        print(f'{n} x {num:2} = {n * num}')

print('\nPrograma encerrado.')