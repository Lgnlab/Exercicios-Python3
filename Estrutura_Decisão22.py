def escolha_operacao(n1 = 0, n2 = 0):
    while True: 
        n1 = float(input('Primeiro Número: '))
        n2 = float(input('Segundo Número: '))
        operação = int(input('Qual operação você deseja(1, 2, 3)? '))
        if operação == 1:
            if n1 % 2 == 0:
                print(f'{n1} é PAR!')
            elif n1 % 2 != 0:
                print(f'{n1} é ÍMPAR!')
            if n2 % 2 == 0:
                print(f'{n2} é PAR!')
            elif n2 % 2 != 0:
                print(f'{n2} é ÍMPAR!')
        elif operação == 2:
            if n1 < 0:
                print(f'{n1} é NEGATIVO!')
            elif n1 > 0:
                print(f'{n1} é POSITIVO!')
            if n2 < 0:
                print(f'{n2} é NEGATIVO!')
            elif n2 > 0:
                print(f'{n2} é POSITIVO!')
        elif operação == 3:
            arredondado1 = round(n1)
            if n1 == arredondado1:
                print(f'{n1} é INTEIRO!')
            else:
                print(f'{n1} é DECIMAL!')
            arredondado2 = round(n2)
            if n2 == arredondado2:
                print(f'{n2} é INTEIRO!')
            else:
                print(f'{n2} é DECIMAL!')
        sair = str(input('Quer continuar(S/N)? ')).upper().strip()[0]
        if sair == 'N':
            break
    return 'Volte Sempre!'

print(escolha_operacao())