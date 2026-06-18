def juntando_valores(valores = 0):
    lista_valores = []
    while True:
        valores = int(input("Informe um valor: "))
        if valores == -1:
            break
        else:
            lista_valores.append(valores)
    
    return f"Valores lidos: {len(lista_valores)}\nValores: {lista_valores}\nLista reversa: {lista_valores[::-1]}\nSoma: {sum(lista_valores)}\nMédia: {sum(lista_valores) / len(lista_valores):.1f}\n"


print(juntando_valores())