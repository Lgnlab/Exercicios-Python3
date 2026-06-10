def conversor_temperatura(gf = 0):
    gf = int(input('Graus Em Fahrenheit: '))
    gc = 5 * ((gf - 32) / 9)
    return f'{gf}°F para {gc:.1f}°C'


print(conversor_temperatura())