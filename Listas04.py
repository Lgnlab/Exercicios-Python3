def analisando_valores(numeros= 0):
    lista = []
    verificador = False
    while True:
        numeros = int(input('Informe um valor para adicionar na lista: '))
        if numeros == 5:
            verificador = True
        lista.append(numeros)
        sair = str(input('Quer continuar(S/N)?')).upper().strip()[0]
        if sair == 'N':
            break
    lista.sort(reverse=True)
    return f'Quantidade de números digitados: {len(lista)}\nLista decrescente: {lista}\O valor 5 foi digitado? {verificador}'


print(analisando_valores())