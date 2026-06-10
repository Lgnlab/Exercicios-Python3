def conversor_medidadas(valor = 0):
    valor = float(input('Valor em metros(m): '))
    return f'Convertendo de metros para centímetros: {valor:1f}m -> {valor * 100:.1f}cm'


print(conversor_medidadas())