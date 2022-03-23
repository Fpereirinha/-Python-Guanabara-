def escreva(y):
    tam = len(y) + 2
    print(f'{"~"}'* tam)
    print(f'{y:^{tam}}')
    print(f'{"~"}'* tam)


escreva('Pedrão')
escreva('SHOW')
escreva("Show"*2)