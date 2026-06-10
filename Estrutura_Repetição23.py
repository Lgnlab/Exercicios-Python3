def primo_dois(numero = 0):
    numero = int(input('Informe um número: '))
    cont = 1
    dividido = 0
    while cont <= numero:
        if numero % cont == 0:
            print(f'\033[32m{cont}\033[m', end=' ')
            dividido += 1
        else:
            print(f'\033[31m{cont}\033[m', end=' ')
        cont += 1
    print()
    if dividido > 2 or numero == 0:
        print(f'{numero} tem {dividido} divisores. \033[33mNÃO É PRIMO!\033[m')
    else:
        print(f'{numero} tem {dividido} divisores. \033[32mÉ PRIMO!\033[m')


primo_dois()