def conferindo_sexo(sexo = ''):
    try:
        sexo = str(input('Sexo: ')).upper()
    except KeyboardInterrupt:
        return 'Usuário preferiu não informar os dados.'
    else:
        if sexo == 'F':
            return 'Feminino'
        elif sexo == 'M':
            return 'Masculino'
        else:
            return 'Sexo Inválido.'
        
print(conferindo_sexo())