def desconto_salario(valor_hora = 0, horas_trabalhadas = 0):
    valor_hora = float(input('Valor da hora: R$'))
    horas_trabalhadas = int(input('Horas Trabalhadas(mês): '))
    salario_bruto = valor_hora * horas_trabalhadas
    if salario_bruto <= 900:
        ir = 0
    elif salario_bruto <= 1500:
        ir = salario_bruto * (5 / 100)
    elif salario_bruto <= 2500:
        ir = salario_bruto * (10 / 100)
    else:
        ir = salario_bruto * (20 / 100)
    inss = salario_bruto * (10 / 100)
    fgts = salario_bruto * (11 / 100)
    total_descontos = ir + inss
    return f'Salário bruto: R${salario_bruto:.2f}\nIR: R${ir:.2f}\nINSS: R${inss:.2f}\nFGTS: R${fgts:.2f}\nTotal descontos: R${total_descontos:.2f}\nSalário liquido: R${salario_bruto - ir - inss:.2f}'


print(desconto_salario())