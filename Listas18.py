def juntando(vetor_1 = 0, vetor_2 = 0, vetor_3 = 0):
    a = []
    b = []
    c = []
    for cont_a in range(1, 11):
        vetor_1 = int(input(f"{cont_a} Número: "))
        a.append(vetor_1)
    print("=" * 12)
    for cont_b in range(1, 11):
        vetor_2 = int(input(f"{cont_b} Número: "))
        b.append(vetor_2)
    print("=" * 12)
    for cont_c in range(1, 11):
        vetor_3 = int(input(f"{cont_c} Número: "))
        c.append(vetor_3)
    d = a + b + c
    return f"Lista três: {d}"

print(juntando())