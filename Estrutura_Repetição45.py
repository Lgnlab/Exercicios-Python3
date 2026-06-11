# Gabarito da prova
gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

notas = []

while True:
    acertos = 0

    print("\n--- Novo Aluno ---")

    # Recebe as respostas
    for i in range(10):
        resposta = input(f"Questão {i+1}: ").upper()

        if resposta == gabarito[i]:
            acertos += 1

    print(f"Acertos: {acertos}")
    print(f"Nota: {acertos}")

    notas.append(acertos)

    continuar = input(
        "\nOutro aluno vai utilizar o sistema? (S/N): ").upper()

    if continuar != "S":
        break

# Estatísticas finais
maior = max(notas)
menor = min(notas)
total_alunos = len(notas)
media = sum(notas) / total_alunos

print("\n===== RESULTADO FINAL =====")
print(f"Maior acerto: {maior}")
print(f"Menor acerto: {menor}")
print(f"Total de alunos: {total_alunos}")
print(f"Média da turma: {media:.2f}")