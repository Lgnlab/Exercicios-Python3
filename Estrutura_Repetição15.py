def fibonacci(termo = 0):
    termo = int(input('Quantos termos você quer ver? '))
    cont = 1
    t1, t2 = 0, 1  
    while cont <= termo:
        print(t1, end=' ')   # 0  1  1  2  3                     
        t3 = t1 + t2         # t1 t2 t3
        t1 = t2
        t2 = t3
        cont += 1


fibonacci()