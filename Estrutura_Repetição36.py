def tabuada(tab = 0, inicio = 0, fim = 0):
    tab = int(input("Montar a tabuada de: "))
    inicio = int(input("Começar por: "))
    fim = int(input("Terminar em: "))
    for t in range(inicio, fim + 1):
        print(f"{tab} x {t} = {tab * t}")


tabuada()