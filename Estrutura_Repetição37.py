def academia(codigo = 0, altura = 0, peso = 0):
    maior_altura = menor_altura = mais_gordo = mais_magro = cont = 0
    media_altura = media_peso = codigo_alto = codigo_menor = codigo_gordo = codigo_magro = 0
    while True:
        codigo = int(input("Código do aluno: "))
        if codigo == 0:
            break
        altura = float(input("Altura: "))
        peso = float(input("Peso(kg): "))
        media_altura += altura
        media_peso += peso
        cont += 1
        if cont == 1:
            maior_altura = menor_altura = altura
            mais_gordo = mais_magro = peso
            codigo_alto = codigo_menor = codigo_gordo = codigo_magro = codigo
        else:
            if altura > maior_altura:
                maior_altura = altura
                codigo_alto = codigo
            if altura < menor_altura:
                menor_altura = altura
                codigo_menor = codigo
            if peso > mais_gordo:
                mais_gordo = peso
                codigo_gordo = codigo
            if peso < mais_magro:
                mais_magro = peso
                codigo_magro = codigo 
    return f"Média de altura: {media_altura / cont:.1f}cm\nMédia de peso: {media_peso / cont:.1f}kg\nMaior peso: {mais_gordo:.1f}kg do aluno {codigo_gordo}\nMenor peso: {mais_magro:.1f}kg do aluno {codigo_magro}\nMaior altura: {maior_altura:.2f}cm do aluno {codigo_alto}\nMenor altura: {menor_altura:.2f}cm do aluno {codigo_menor}"


print(academia())