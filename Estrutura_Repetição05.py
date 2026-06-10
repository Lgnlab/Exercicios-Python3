def crescimento_populacional(pais_a = 0, pais_b = 0, taxa_a = 0, taxa_b = 0):
    pais_a = int(input('População A: '))
    pais_b = int(input('População B: '))
    taxa_a = float(input('Taxa de crescimento A (%): '))
    taxa_b = float(input('Taxa de crescimento B (%): '))
    anos = 0
    while pais_a <= pais_b:
        pais_a = pais_a * (taxa_a / 100) + pais_a
        pais_b = pais_b * (taxa_b / 100) + pais_b
        anos += 1
    return f"Levou {anos} para o país A ultrapassar ou igualar o país B."


print(crescimento_populacional())