def calculo_salario(ganhoh = 0, htrabalhadas = 0):
    ganhoh = float(input('Ganho Por Hora: R$'))
    htrabalhadas = int(input('Horas Trabalhadas: '))
    return f'Você trabalhou {htrabalhadas} horas com um ganho de R${ganhoh:.2f}: Salário R${(ganhoh * htrabalhadas) * 30:.2f}'


print(calculo_salario())