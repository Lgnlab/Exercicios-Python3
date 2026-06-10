import math

def calculo_tintas(area = 0):
    area = float(input('Área(m²): '))
    rendimento = area / 6
    latas = math.ceil(rendimento / 18)
    latasm = math.ceil(rendimento / 3.6)
    folga = rendimento * 1.10
    latasgran = math.ceil(folga / 18)
    sobragran = folga - 18
    lataspeq = math.ceil(sobragran / 3.6 )
    custo = latas * 80
    custom = latasm * 25
    return f'Litros necessários: {rendimento:.2f}\nQuantidade de latas de 18 litros: {latas}\nQuantidade de latas de 3,6 litros: {latasm}\nCusto total 18 litros: R${custo:.2f}\nCusto total 3,6 litros: R${custom:.2f}\nMisturando latas: {latasgran} lata(s) grande(s) e {lataspeq} lata(s) menor(es)'


print(calculo_tintas())