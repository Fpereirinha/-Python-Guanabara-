f = int(input('Quantos termos da fibo você quer ver ?'))
t1 = 0
t2 = 1
print(f'{t1}\n{t2}')
while f > 2:

    t3 = t1 + t2
    t1 = t2
    t2 = t3
    f -= 1
    print(t3)
print('FIM')