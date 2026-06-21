def sistema_operacional(voto = int):
    from collections import Counter

    lista_votos = []
    cont = 0
    while True:
        voto = int(input("Qual o melhor sistema operacional para uso em servidores[1/6]? "))
        if voto == 0:
            break
        else:
            lista_votos.append(voto)
            cont += 1
    contagem_votos = Counter(lista_votos)
    dicionario_comum = dict(contagem_votos)

    print("Opções de voto:")
    print("""
    1- Windows Server
    2- Unix                     
    3- Linux                    
    4- Netware                  
    5- Mac OS                    
    6- Outro  
    """)
    print("Resultado da votação:")
    for k, v in dicionario_comum.items():
        perce = v / cont * 100
        print(f"Sistema Operacional: {k} - Votos: {v} - Percentual: {perce:.1f}%")


sistema_operacional()