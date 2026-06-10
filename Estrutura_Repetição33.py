def meteorologia(temperaturas = 0):
    soma = menor = maior = cont = 0
    while True:
        temperaturas = int(input('Temperatura[999 para parar](°C):'))
        if temperaturas == 999:
            break
        else:
            soma += temperaturas
            cont += 1
        if cont == 1:
            maior = menor = temperaturas
        else:
            if temperaturas > maior:
                maior = temperaturas
            if temperaturas < menor:
                menor = temperaturas
    return f"Maior temperatura: {maior}°C\nMenor temperatura: {menor}°C\nMédia de temperaturas: {soma / cont:.0f}C°"


print(meteorologia())