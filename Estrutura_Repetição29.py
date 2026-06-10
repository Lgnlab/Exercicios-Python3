def tabela():
    cont = 1
    valor_produto = 1.99
    while cont <= 50:
        print(f"{cont} - R${valor_produto * cont:.2f}")
        cont += 1

tabela()