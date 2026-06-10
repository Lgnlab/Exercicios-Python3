def altura_peso(id = 0, altura = 0):
    cont = 1
    maior_altura = menor_altura = 0
    id_maior = id_menor = 0
    while cont <= 10:
        id = int(input("ID do aluno: "))
        altura = float(input("Altura(cm): "))
        cont += 1
        if cont == 1:
            maior_altura = menor_altura = altura
            id_maior = id_menor = id
        else:
            if altura > maior_altura:
                maior_altura = altura
                id_maior = id
            if altura < menor_altura:
                menor_altura = altura
                id_menor = id
    return f"Maior altura: {maior_altura:.2f} do aluno {id_maior}\nMenor altura: {menor_altura:.2f} do aluno {id_menor}"


print(altura_peso())    