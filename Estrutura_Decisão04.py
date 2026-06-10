def validando_letra(letra = ''):
    letra = str(input('Informe uma letra: ')).upper()
    if letra in 'AEIOU':
        return f'{letra} é uma VOGAL!'
    else:
        return f'{letra} é uma CONSOANTE!'
    
print(validando_letra())
