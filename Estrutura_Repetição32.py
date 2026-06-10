def fatorial(numero = int):
    numero = int(input('Informe um número: '))
    cont = numero
    multi = 1
    print("5!= ", end='')
    while cont >= 1:
        print(cont, end='')
        if cont > 1:
            print(" x ", end='')
        else:
            print(' = ', end='')  
        multi *= cont
        cont -= 1
    return multi


print(fatorial())