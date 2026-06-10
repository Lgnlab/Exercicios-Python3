def calculo_salario(salario = 0):
    salario = float(input("Salário: R$"))
    cont = 1
    percent_aumento = 1.5
    while cont <= 2:
        calculo_aumento = salario * (percent_aumento / 100)
        salario_aumento = calculo_aumento + salario
        percent_aumento *= 2
        cont += 1
    return f"Salário atual: R${salario_aumento:,.2f}\nValor do aumento: R${calculo_aumento:,.2f}\nPercentual final: {percent_aumento}%"


print(calculo_salario())