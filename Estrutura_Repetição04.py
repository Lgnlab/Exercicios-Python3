def crescimento_populacional():
    pais_a = 80_000
    pais_b = 200_000
    anos = 0
    while pais_a <= pais_b:
        pais_a = pais_a * (3 / 100) + pais_a
        pais_b = pais_b * (1.5 / 100) + pais_b
        anos += 1
    return f"Levou {anos} para o país A ultrapassar ou igualar o país B."


print(crescimento_populacional())