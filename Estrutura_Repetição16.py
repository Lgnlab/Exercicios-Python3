def fibonacci():
    t1, t2 = 0, 1
    soma = 0
    while soma < 500:
        print(t1, end=' ')
        soma += t1
        t3 = t1 + t2
        t1 = t2
        t2 = t3
    return f'\nSoma: {soma}'

print(fibonacci())