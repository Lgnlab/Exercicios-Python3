def calculando_divida(divida = 0):
    while True:
        divida = float(input("Valor da dívida: R$"))
        if divida == 0:
            break
        else:
            print(f"Valor dos Juros: 0 | Parcelas: 0 | Valor da parcela: R${divida:,.2f}")
            print(f"Valor dos juros: R${divida * 0.1:,.2f} | Parcelas: 3 | Valor da parcela: R${(divida * 0.1 + divida) / 3:,.2f}")
            print(f"Valor dos juros: R${divida * 0.15:,.2f} | Parcelas: 6 | Valor da parcela: R${(divida * 0.15 + divida) / 6:,.2f}")
            print(f"Valor dos juros: R${divida * 0.2:,.2f} | Parcelas: 9 | Valor da parcela: R${(divida * 0.2 + divida) / 9:,.2f}")
            print(f"Valor dos juros: R${divida * 0.25:,.2f} | Parcelas: 12 | Valor da parcela: R${(divida * 0.25 + divida) / 12:,.2f}")


calculando_divida()