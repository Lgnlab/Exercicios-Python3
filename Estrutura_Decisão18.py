def decompor_numeros(numero = 0):
    numero = int(input('Informe um número(menor 1.000): '))
    tratando = str(numero)
    if len(tratando) == 1:
        return f'{numero} Unidade(s)'
    elif len(tratando) == 2:
        return f'{tratando[0]} Dezena(s) e {tratando[1]} Unidade(s)'
    elif len(tratando) == 3:
        return f'{tratando[0]} Centena(s), {tratando[1]} Dezena(s) e {tratando[2]} Unidade(s)'
    else:
        return '\033[31mVALOR INVÁLIDO PARA ESSE PROGRAMA.\033[m'

print(decompor_numeros())