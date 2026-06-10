def media_idade(idade = 0):
    soma = cont = 0
    while True:
        idade = int(input('Idade[999 para parar]: '))
        if idade == 999:
            break
        else:
            soma += idade
            cont += 1
    media = soma / cont
    if media >= 0 and media <= 25:
        return f'Status da média de idades[{media:.1f}]: Jovem'
    elif media <= 60:
        return f'Status da média de idades[{media:.1f}]: Adulta'
    else:
        return f'Status da média de idades[{media:.1f}]: Idosa'
    

print(media_idade())