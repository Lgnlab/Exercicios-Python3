def intervalos_numericos(numero = 0):
    inter1 = inter2 = inter3 = inter4 = 0
    while True:
        numero = int(input("Informe um número[negativo para parar]:"))
        if numero < 0:
            break
        for ium in range(0, 26):
            if numero == ium:
                inter1 += 1
        for idois in range(26, 51):
            if numero == idois:
                inter2 += 1
        for itres in range(51, 76):
            if numero == itres:
                inter3 += 1
        for iquatro in range(76, 101):
            if numero == iquatro:
                inter4 += 1
    return f"[0-25]: {inter1}\n[26-50]: {inter2}\n[51-75]: {inter3}\n[76-100]: {inter4}"


print(intervalos_numericos())