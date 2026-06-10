def escolha_barata(valor = 0):
    try:
        barato = 0
        for c in range(1, 4):
            valor = float(input('Preço do produto: R$'))
            if c == 1:
                barato = valor
            else:
                if valor < barato:
                    barato = valor
    except (TypeError, ValueError):
        return 'Informe o valor em R$'
    except KeyboardInterrupt:
        return 'Usuário preferiu não informar os dados'
    else:
        return f'Produto mais barato: R${barato:.2f}'
    

print(escolha_barata())