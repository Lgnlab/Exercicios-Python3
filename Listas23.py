def bonus_vendedor():
    contadores = [0] * 9
    while True:
        vendas = float(input("Vendas brutas (0 para encerrar): "))
        if vendas == 0:
            break
        salario = 200 + vendas * 0.09
        if salario >= 1000:
            contadores[8] += 1
        else:
            indice = int((salario - 200) // 100)
            contadores[indice] += 1
    faixas = [
        "$200 - $299",
        "$300 - $399",
        "$400 - $499",
        "$500 - $599",
        "$600 - $699",
        "$700 - $799",
        "$800 - $899",
        "$900 - $999",
        "$1000 em diante"
    ]
    print("\nQuantidade de vendedores por faixa salarial:")
    for i in range(len(contadores)):
        print(f"{faixas[i]}: {contadores[i]}")


bonus_vendedor()