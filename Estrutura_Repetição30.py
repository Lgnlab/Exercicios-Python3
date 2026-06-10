def tabela(valor = 0):
    valor = float(input("Preço do pão: R$"))
    cont = 1
    while cont <= 50:
        print(f"{cont} - R${valor * cont:.2f}")
        cont += 1


tabela()