def fatorial(numero = 0):
    while True:
        numero = int(input('Informe um número para ver o fatorial: '))
        multi = 1
        print('5!= ', end='')
        for c in range(numero, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            multi *= c
        print(multi)
        sair = str(input('Quer continuar[S/N]?')).upper().strip()[0]
        if sair == 'N':
            break
    return 'Volte Sempre!'   


print(fatorial()) 