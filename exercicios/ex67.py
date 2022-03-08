while True:
    n = int(input("Quer ver a taboada de qual valor ?"))
    if n < 0:
        print('PROGRAMA ENCERRADO, VOLTE SEMPRE.')
        break
    c = 1
    while c < 11:
        print(f'{n} x {c} = {n*c}')
        c += 1

