def triangulo(lado1 = 0, lado2 = 0, lado3 = 0):
    try:
        forma_triangulo = False
        tipo_triangulo = ''
        lado1 = int(input('Lado 1: '))
        lado2 = int(input('Lado 2: '))
        lado3 = int(input('Lado 3: '))
        if lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado3 + lado1 > lado2:
            forma_triangulo = True
            if lado1 == lado2 and lado1 == lado3:
                tipo_triangulo = 'Triângulo Equilátero'
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                tipo_triangulo = 'Triângulo Isósceles'
            else:
                tipo_triangulo = 'Triângulo Escaleno'
    except (ValueError, TypeError):
        return 'Informe um valor INTEIRO.'
    except KeyboardInterrupt:
        return 'Usuário preferiu não informar os dados.'
    else:
        return f'Os valores digitados podem formar um triângulo: {forma_triangulo}\nTipo do triângulo: {tipo_triangulo}'
    

print(triangulo())