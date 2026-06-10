def calculo_salario(ganhoh = 0, horast = 0):
    ganhoh = float(input('Ganho por hora: R$'))
    horast = int(input('Horas trabalhadas: '))
    salario_bruto = (ganhoh * horast) * 30
    print(f'Salário Bruto: R${salario_bruto:.2f}')
    calculo_ir = salario_bruto * (11 / 100)
    print(f'IR (11%): R${calculo_ir:.2f}')
    calculo_inss = salario_bruto * (8 / 100)
    print(f'INSS (8%): R${calculo_inss:.2f}')
    sindicato = salario_bruto * (5 / 100)
    print(f'Sindicato (5%): R${sindicato:.2f}')
    print(f'Salário Liquído: R${salario_bruto - calculo_ir - calculo_inss - sindicato:.2f}')


calculo_salario()