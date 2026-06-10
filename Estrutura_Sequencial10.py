def conversor_temperatura(gc = 0):
    gc = int(input('Graus Em Celsius: '))
    gf = (gc * 9/5) + 32
    return f'{gc}°C para {gf:.1f}°F'


print(conversor_temperatura())