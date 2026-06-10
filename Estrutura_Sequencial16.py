import math

def calculo_tintas(area = 0):
    area = float(input('Área(m²): '))
    rendimento = area / 3
    latas = math.ceil(rendimento / 18)
    custo = latas * 80
    return f'Litros necessários: {rendimento:.2f}\nQuantidade de latas: {latas}\nCusto total: R${custo:.2f}'

print(calculo_tintas())
