def maior_numero(numero = 0):
    try:
        maior = 0
        for c in range(1, 4):
            numero = int(input('Digite um número: '))
            if c == 1:
                maior = numero
            else:
                if numero > maior:
                    maior = numero
    except (TypeError, ValueError):
        return 'Informe um valor INTEIRO.'
    except KeyboardInterrupt:
        return 'Usuário preferiu não informar os dados.'
    else:
        return f'Maior número digitado: {maior}'


print(maior_numero())