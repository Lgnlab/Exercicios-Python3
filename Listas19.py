def idade_altura(idade = 0, altura = 0):
    dados = [[], []]
    qtd_alunos = 0
    cont = 1
    while cont <= 3:
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        dados[0].append(idade)
        dados[1].append(altura)
        cont += 1
    media = sum(dados[1]) / len(dados[1])
    for itens1, itens2 in zip(dados[0], dados[1]):
        if itens1 > 13 and itens2 < media:
            qtd_alunos += 1
    return f"Alunos com mais de 13 anos e altura inferior à média: {qtd_alunos}\nMédia de altura: {media:.1f}"


print(idade_altura())