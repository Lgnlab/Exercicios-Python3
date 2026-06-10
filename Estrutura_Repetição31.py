def registradore_rudimentar(valor_produto = float):
    total = 0
    cont = 1
    while True:
        valor_produto = float(input(f"Produto {cont}: R$"))
        if valor_produto == 0:
            break
        else:
            total += valor_produto
            cont += 1
    dinheiro = float(input("Dinheiro: R$"))
    troco = dinheiro - total
    return f"Total: R${total:,.2f}\nTroco: R${troco:,.2f}"


print(registradore_rudimentar())