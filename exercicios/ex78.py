#c = 0
import errno

lista = []
maximo = []
minimo = []
'''while True:
    lista.append(int(input('Digite um valor: ')))
    c += 1
    if c == 4:
        break'''
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
for posição, valores in enumerate(lista):
    print(f'{posição+1}° número digitado foi {valores}')
    if valores == max(lista):
        maximo.append(posição+1)
    if valores == min(lista):
        minimo.append(posição+1)
print(f'O maior valor digitado foi {max(lista)} em {len(maximo)} posição(es): ',end='')
for x in maximo:
    print(f'{x}...',end='')
print(f'\nO menor valor difitado foi {min(lista)} em {len(minimo)} posição(es): ', end='')
for c in minimo:
    print(f'{c}...', end='')