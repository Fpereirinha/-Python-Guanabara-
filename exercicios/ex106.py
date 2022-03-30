def ajuda(msg):
    while True:
        x = input(f'{msg} [FIM] para parar')
        if x.upper().strip()[0] == 'F':
            print('FIM.')
            break
        help(x)


mensagem = "Digite um comando."
ajuda(mensagem)
