def conversor_tamanho(gigabytes = 0):
    gigabytes = float(input('Tamanho Em Gigabytes: '))
    calculom = gigabytes * 1024
    calculok = gigabytes * 1024 * 1024
    return f'{gigabytes:.1f} Gigabytes para {calculom:.1f} Megabytes e {calculok:.1f} Kilobytes'


print(conversor_tamanho())