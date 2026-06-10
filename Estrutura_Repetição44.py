def eleicao(voto = 0):
    tot_votos = tot_nulos = tot_branco = 0
    print("1-Jose/2-João/3-Maria/4-Ana/5-Nulo/6-Branco")
    while True:
        voto = int(input("Voto: "))
        if voto == 0:
            break
        else:
            tot_votos += 1
            if voto == 5:
                tot_nulos += 1
            if voto == 6:
                tot_branco += 1
    return f"Total de votos: {tot_votos}\nTotal de nulos: {tot_nulos}\nTotal de brancos: {tot_branco}\nPercentagem de votos nulos: {(tot_nulos / tot_votos) * 100:.0f}%\nPercentagem de votos brancos: {(tot_branco / tot_votos) * 100:.0f}%"


print(eleicao())    