def area_quadrado(lado = 0):
    lado = float(input('Informe um dos lados do quadrado:'))
    area = lado ** 2
    return f'Área dobrada do quadrado: {area * 2:.0f} cm²'


print(area_quadrado())