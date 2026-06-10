def dados():
    lista_dados = []
    temp = []
    cont_pessoas = maior = menor = 0
    while True:
        temp.append(str(input('Nome: ')))
        temp.append(int(input('Peso(kg): ')))
        cont_pessoas += 1
        if len(lista_dados) == 0:
            maior = menor = temp[1]
        else:
            if temp[1] > maior:
                maior = temp[1]
            if temp[1] < menor:
                menor = temp[1]
        lista_dados.append(temp[:])
        temp.clear()
        sair = str(input('Quer continuar(S/N)? ')).upper().strip()[0]
        if sair == 'N':
            break
    return f'Os dados foram: {lista_dados}\nQuantidade de cadastro: {cont_pessoas}\nMaior peso: {maior}\nMenor peso: {menor}'


print(dados())