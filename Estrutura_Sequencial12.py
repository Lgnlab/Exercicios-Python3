def conversor_tamanho(gigabytes = 0):
    gigabytes = float(input('Tamanho Em Gigabytes: '))
    calculo = gigabytes * 1024
    return f'{gigabytes:.1f} Gigabytes para {calculo:.1f} Megabytes'


print(conversor_tamanho())