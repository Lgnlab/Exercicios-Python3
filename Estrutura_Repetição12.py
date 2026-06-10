def gerador_tabuada(tabuada = 1):
    tabuada = int(input('Informe um número para ver a tabuada: '))
    cont = 1
    while cont <= 10:
        print(f'{tabuada} x {cont} = {tabuada * cont}')
        cont += 1


gerador_tabuada()