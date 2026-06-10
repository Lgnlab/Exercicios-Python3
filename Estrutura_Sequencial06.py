def area_circulo(raio = 0):
    raio = float(input('Raio do círculo: '))
    area = (raio ** 2) * 3.14
    return f'A área de círculo com raio {raio}: {area}'


print(area_circulo())