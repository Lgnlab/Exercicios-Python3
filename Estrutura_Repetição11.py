def intervalo_numeros(inicio = 0, fim = 0):
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    cont = inicio
    soma = 0
    if inicio < fim:
        while cont <= fim:
            print(cont, end=' ')
            soma += cont
            cont += 1
    else:
        while fim <= cont:
            print(cont, end=' ')
            soma += cont
            cont -= 1
    return f"\nSoma do intervalo: {soma}"
    


print(intervalo_numeros())