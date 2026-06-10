def formato_data(data = ''):
    data = str(input('Informe a data(dd/mm/aaaa): ')).strip()
    if len(data) < 10:
        return 'Data Inválida.'
    else:
        return 'Data Válida.'
    

print(formato_data())