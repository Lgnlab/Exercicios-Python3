def acidentes_transito(codigo_cidade = 0, veiculos = 0, acidentes = 0):
    cont = soma = 0
    maior_acidentes = menor_acidentes = 0 
    codigo_maior_acidentes = codigo_menor_acidentes = 0
    while cont <= 4:
        codigo_cidade = int(input("Código da cidade: "))
        veiculos = int(input("Quantidade de veículos: "))
        acidentes = int(input("Quantidade de acidentes com vítimas: "))
        soma += veiculos
        cont += 1
        if cont == 1:
            maior_acidentes = menor_acidentes = acidentes
            codigo_maior_acidentes = codigo_menor_acidentes = codigo_cidade
        else:
            if acidentes > maior_acidentes:
                maior_acidentes = acidentes
                codigo_maior_acidentes = codigo_cidade
            if acidentes < menor_acidentes:
                menor_acidentes = acidentes
                codigo_menor_acidentes = codigo_cidade
    return f"Maior Índice de acidentes: {maior_acidentes} é da cidade {codigo_maior_acidentes}\nMenor Índice de acidentes: {menor_acidentes} é da cidade {codigo_menor_acidentes}\nMédia de veículos: {soma / cont:.1f}"


print(acidentes_transito())