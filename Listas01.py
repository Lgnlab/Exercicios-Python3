def maior_menor(*numeros):
    lista_numeros = []
    posicoes_maior = []
    posicoes_menor = []
    maior = menor = 0
    for n in range(0, 5):
        numeros = int(input(f'Digite o número na posição {n}: '))
        if n == 0:
            maior = menor = numeros
        else:
            if numeros > maior:
                maior = numeros
            elif numeros < menor:
                menor = numeros
        lista_numeros.append(numeros)
    for i, v in enumerate(lista_numeros):
        if v == maior:
            posicoes_maior.append(i)
        elif v == menor:
            posicoes_menor.append(i)
    return f'Números digitados: {lista_numeros}\nMaior: {maior} nas posições {posicoes_maior}\nMenor: {menor} nas posições {posicoes_menor}'


print(maior_menor())