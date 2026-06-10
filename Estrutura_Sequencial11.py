def calculos():
    valor_inteiro1 = int(input('1 valor inteiro: '))
    valor_inteiro2 = int(input('2 valor inteiro: '))
    valor_real = float(input('Valor real: '))
    print(f'O produto do dobro do primeiro com metade do segundo: {(valor_inteiro1 * 2) * (valor_inteiro2 / 2 ):.1f}')
    print(f'A soma do triplo do primeiro com o terceiro: {(3 * valor_inteiro1) + valor_real:.1f}')
    print(f'O terceiro elevado ao cubo: {valor_real ** 3:.1f}')


calculos()
