def controle_de_pesca(peso_peixes = 0):
    peso_peixes = int(input('Peso dos peixes(kg): '))
    if peso_peixes > 50:
        excesso = peso_peixes - 50
        multa = excesso * 4
        return f'Excesso: {excesso}kg\nMulta: R${multa:.2f}'
    

print(controle_de_pesca())
