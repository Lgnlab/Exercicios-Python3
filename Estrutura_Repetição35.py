def primos_dois(inicio = 0, fim = 0):
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    for n in range(inicio, fim + 1):
        if n > 1:
            primo = True
            for i in range(2, n):
                if n % i == 0:
                    primo = False
                    break
            if primo:
                print(n, end=' ')


primos_dois()