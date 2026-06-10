def caixa_eletronico(saque = 0):
    saque = int(input('Valor do saque(mínimo de R$10,00 e máximo de R$600,00): '))
    cedula = 100
    divida = saque
    cont_ced = 0
    while True:
        if divida >= cedula:
            divida -= cedula
            cont_ced += 1
        else:
            if cont_ced > 0:
                print(f'Total de {cont_ced} cédulas de R${cedula}')
            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 1
            cont_ced = 0
            if divida == 0:
                break
    return 'Volte Sempre!'


print(caixa_eletronico())