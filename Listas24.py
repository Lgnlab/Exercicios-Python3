def saltos(atleta = str, saltos = 0):
    lista_saltos = []
    resultado = ""
    while True:
        atleta = str(input("Atleta: ")).strip()
        if atleta == "":
            break
        else:
            for cont in range(1, 6):
                saltos = int(input(f"{cont}ª Salto: "))
                lista_saltos.append(saltos)
            print("Resultado final:")
            print(f"Atleta: {atleta}")
            print("Saltos:", end=' ')
            for i ,salto in enumerate(lista_saltos):
                resultado += str(salto)
                if i < len(lista_saltos) - 1:
                    resultado += " - "
            print(resultado)
            lista_saltos.clear()
            print()
            
saltos()