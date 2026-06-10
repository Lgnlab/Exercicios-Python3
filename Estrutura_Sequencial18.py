def calculando_download(megabytes = 0, velocidade = 0):
    megabytes = int(input('Megabytes: '))
    velocidade = int(input('Velocidade: '))
    convert = megabytes * 8
    calculov = convert / velocidade
    calculof = calculov / 60
    return f'Tamanho: {convert}Mb\nVelocidade: {calculof:.2f} minutos'


print(calculando_download())
