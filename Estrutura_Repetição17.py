def fatorial(numero = 0):
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
    return multi    


print(fatorial())  


def fatorial_dois(numero = 0):
    numero = int(input('Digite um número para ver o fatorial: '))
    cont = numero
    fatorial = 1
    print('5!= ', end='')
    while cont >= 1:
        print(cont, end='')
        if cont > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        fatorial *= cont
        cont -= 1
    return fatorial


print(fatorial_dois())