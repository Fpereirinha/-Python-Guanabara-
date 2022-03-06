nome = str(input('Qual seu nome ?')).strip()
n = nome.split()
print('Seu primero nome é {} e o ultimo é {}'.format(n[0], n[len(n)-1]))
