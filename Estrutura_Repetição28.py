def colecionador(quantidade = 0, valor = 0):
    quantidade = int(input('Quantidade de CDs: '))
    cont = 1
    soma = 0
    while cont <= quantidade:
        valor = int(input('Valor de cada um: R$'))
        soma += valor
        cont += 1
    return f'Quantidade de CDs: {quantidade}\nMédia: R${soma / cont:.2f} por CD'


print(colecionador())