from time import sleep
x = str(input('Digite seu nome e vamos checar se é um Palindromo:'))
sleep(3)
print(f'{f"ESTAMOS CHECANDO {x.strip().upper()}!!":=^40}')
separa = x.split()
junto = ''.join(separa)
inverso = ''
sleep(3)
## print(f'O nome {x.upper()} invertido é {junto.upper()}.')
for c in range(len(junto) -1 , -1, -1):
    inverso += junto[c]
print(f'{junto} invertido é \n {inverso}')
if junto == inverso:
    print('É palindromo')
else:
    print('Não é palindromo.')