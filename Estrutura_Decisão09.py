def ordem_decrescente(numero = 0):
    maior = meio = menor = 0
    for c in range(1, 4):
        numero = int(input(f'{c} Número: '))
        if c == 1:
            maior = meio = menor = numero
        else:
            if numero > maior:
                meio = maior
                maior = numero
            if numero < menor:
                meio = menor
                menor = numero
            else:
                meio = numero
    return f'{maior}, {meio}, {menor}'
    

print(ordem_decrescente())