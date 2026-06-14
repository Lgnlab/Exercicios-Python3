def juntando(vetor_1 = 0, vetor_2 = 0):
    a = []
    b = []
    for cont_a in range(1, 4):
        vetor_1 = int(input(f"{cont_a} Número: "))
        a.append(vetor_1)
    print("=" * 12)
    for cont_b in range(1, 4):
        vetor_2 = int(input(f"{cont_b} Número: "))
        b.append(vetor_2)
    c = a + b
    return f"Lista três: {c}"

print(juntando())