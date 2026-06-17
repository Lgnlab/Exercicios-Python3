def criminoso(respostas = ""):
    perguntas = ["Telefonou para a vítima", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
    cont_respostas = 0
    for p in perguntas:
        respostas = str(input(f"{p}[S/N]? ")).upper().strip()[0]
        if respostas == "S":
            cont_respostas += 1
    if cont_respostas == 2:
        return f"{cont_respostas} respostas positivas: Classificado como SUSPEITA"
    elif cont_respostas <= 4:
        return f"{cont_respostas} respostas positivas: Classificado como CÚMPLICE"
    elif cont_respostas == 5:
        return f"{cont_respostas} respostas positivas: Classificado como ASSASSINO"
    else:
        return f"{cont_respostas} respostas positivas: INOCENTE"

    
print(criminoso())