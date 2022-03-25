from datetime import datetime
def voto(x):
    idade = datetime.now().year - x
    if idade >= 18:
        val = 'OBRIGATORIO'
    else:
        val = 'NÃO OBRIGATORIO'
    return idade, val



x = int(input('Em que ano você nasceu ? '))
print(f'Com {voto(x)[0]} anos o voto é {voto(x)[1]}')


