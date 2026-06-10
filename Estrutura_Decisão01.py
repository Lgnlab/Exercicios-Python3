def maior_numero(n1= 0, n2= 0):
    maior = 0
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    return f'Maior número digitado: {maior}'


print(maior_numero())