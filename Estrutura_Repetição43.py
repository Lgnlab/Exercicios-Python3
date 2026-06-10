def cardapio(escolha = 0):
    total = 0
    while True:
        escolha = int(input("Código do item[100-105]: "))
        if escolha == 0:
            break
        if escolha == 100:
            total += 1.20
        elif escolha == 101:
            total += 1.30
        elif escolha == 102:
            total += 1.50
        elif escolha == 103:
            total += 1.20
        elif escolha == 104:
            total += 1.30
        elif escolha == 105:
            total += 1.00
    return f"Valor total: R${total:,.2f}"


print(cardapio())