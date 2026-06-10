def maior_menor(numero = 0):
    try:
        maior = menor = 0
        for c in range(1, 4):
            numero = int(input(f'{c} Número: '))
            if c == 1:
                maior = menor = numero
            else:
                if numero > maior:
                    maior = numero
                if numero < menor:
                    menor = numero
    except (TypeError, ValueError):
        return 'Informe um número INTEIRO.'
    except KeyboardInterrupt:
        return 'O usuário preferiu não informar os dados'
    else:
        return f'Maior: {maior}\nMenor: {menor}'
    

print(maior_menor())