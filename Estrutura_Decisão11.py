def aumento_salario(salario = 0):
    try:
        salario = float(input('Salário: R$'))
        if salario <= 280:
            aumento = salario * (20 / 100)
            percentual = '20%'
        elif salario <= 700:
            aumento = salario * (15 / 100)
            percentual = '15%'
        elif salario <= 1500:
            aumento = salario * (10 / 100)
            percentual = '10%'
        else:
            aumento = salario * (5 / 100)
            percentual = '5%'
    except (TypeError, ValueError):
        return 'Informe um valor em R$'
    else:
        return f'R${salario:.2f}\nPercentual de aumento: {percentual}\nValor do aumento: R${aumento:.2f}\nNovo salário: R${salario + aumento:.2f}'
    

print(aumento_salario())