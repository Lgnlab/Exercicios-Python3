def login(usuario = '' , senha = ''):
    while True:
        usuario = str(input('Usuário: '))
        senha = str(input('Senha: '))
        if usuario == senha:
            print('\033[31mUsuário Ou Senha Inválidos!\033[m')
        else:
            break
    return '\033[32mLogin Autorizado!\033[m'


print(login())