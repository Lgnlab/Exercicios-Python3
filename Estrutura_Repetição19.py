def operando_valores(numero = 0):
    maior = menor = soma = cont = 0
    while True:
        numero = int(input('Digite um número: '))
        if numero < 0 or numero > 1_000:
            print('Informe um número entre 0 e 1000')
            break
        else:
            cont += 1
            soma += numero
            if cont == 1:
                maior = numero
                menor = numero
            else:
                if numero > maior:
                    maior = numero
                if numero < menor:
                    menor = numero
            sair = str(input('Quer adicionar mais números[S/N]: ')).strip().upper()[0]
            if sair == 'N':
                break
    return f'Maior: {maior}\nMenor: {menor}\nSoma: {soma}'


print(operando_valores())