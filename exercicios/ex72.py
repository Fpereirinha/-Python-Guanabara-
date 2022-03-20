numero = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte']
while True:
    x = int(input('Digite o número para ver o extenso'))
    if 21 > x >= 0:
        print(f'O número digitado foi {x} e sua escrita é {numero[x]}')
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
        while resp not in 'SN':
            resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('Digite um número no intervalo de 0 a 20 !!!')
print('Obrigado por usar o programa !!')
