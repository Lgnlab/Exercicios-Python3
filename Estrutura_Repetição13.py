def pontencia(base = 0, expoente = 0):
    base = int(input('Base: '))
    expoente = int(input('Expoente: '))
    return f"{base} ** {expoente}: {base ** expoente}"


print(pontencia())