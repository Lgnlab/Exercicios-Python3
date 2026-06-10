def validador_dados(nome = '', idade = 0, salario = 0, estado_civil = ''):
    while True:
        nome = str(input('Nome: ')).strip()
        if len(nome) <= 3:
            print('\033[31mNome Inválido!\033[m')
        else:
            print('\033[32mNome registrado com sucesso.\033[m')
            break
    while True:
        idade = int(input('Idade: '))
        if idade < 0 and idade > 150:
            print('\033[31mIdade Inválida!\033[m')
        else:
            print('\033[32mIdade registrada com sucesso.\033[m')
            break
    while True:
        salario = float(input('Salário: R$'))
        if salario <= 0:
            print('\033[31mSalário Inválido!\033[m')
        else:
            print('\033[32mSalário registrado com sucesso.\033[m')
            break
    while True:
        estado_civil = str(input('Estado Civil(S, C, V, D): ')).upper().strip()
        if estado_civil not in 'SCVD':
            print('\033[31mEstado civil Inválido!\033[m')
        else:
            print('\033[32mEstado civil registrado com sucesso.\033[m')
            break
    return '\033[33mDados Registrados Com Sucesso.\033[m'


print(validador_dados())
