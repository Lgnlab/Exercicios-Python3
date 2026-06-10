def descobrindo_crime(p1= '', p2= '', p3= '', p4= '', p5 = ''):
    contsusp = 0
    p1 = str(input('Telefonou para a vítima[S/N]?')).upper().strip()[0]
    if p1 == 'S':
        contsusp += 1
    p2 = str(input('Esteve no local do crime[S/N]?')).upper().strip()[0]
    if p2 == 'S':
        contsusp += 1
    p3 = str(input('Mora perto da vítima[S/N]?')).upper().strip()[0]
    if p3 == 'S':
        contsusp += 1
    p4 = str(input('Devia para a vítima[S/N]?')).upper().strip()[0]
    if p4 == 'S':
        contsusp += 1
    p5 = str(input('Já trabalhou com a vítima[S/N]?')).upper().strip()[0]
    if p5 == 'S':
        contsusp += 1
    if contsusp == 2:
        return f'{contsusp} Respostas positivas: Suspeita'
    elif contsusp <= 4:
        return f'{contsusp} Respostas positivas: Cúmplice'
    elif contsusp == 5:
        return f'{contsusp} Respostas positivas: Assassino'
    else:
        return f'{contsusp} Respostas positivas: Inocente'


print(descobrindo_crime())