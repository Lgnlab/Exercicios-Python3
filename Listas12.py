def consoantes(palavra = ''):
    palavra = str(input("Informe um palavra: ")).strip().lower()
    letras = list(palavra)
    print(f"Consoantes da palavra '{palavra}':")
    for c in letras:
        if c not in 'aeiou':
            print(c, end='')


consoantes()