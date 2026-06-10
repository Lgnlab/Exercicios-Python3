def intervalo_numeros(inicio = 0, fim = 0):
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(cont, end=' ')
            cont += 1
    else:
        while fim <= cont:
            print(cont, end=' ')
            cont -= 1
    


intervalo_numeros()