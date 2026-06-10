def conferindo_expressao(expressao=''):
    expressao = str(input('Digite uma expressão: '))
    pilha = []
    for p in expressao:
        if p == '(':
            pilha.append('(')
        elif p == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
    if len(pilha) == 0:
        return 'Sua expressão está válida!'
    else:
        return 'Sua expressão está errada!'

print(conferindo_expressao())