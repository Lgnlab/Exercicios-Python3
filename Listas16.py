def soma_quadrado(numero = 0):
    lista = []
    soma = 0
    for cont in range(1, 3):
        numero = int(input(f"{cont} Número: "))
        calculo = numero ** 2
        soma += calculo
        lista.append(calculo)
    return f"Quadrados do números digitados: {lista}\nSoma total da lista: {soma}"


print(soma_quadrado())