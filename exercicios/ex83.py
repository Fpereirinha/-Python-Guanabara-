expressao = str(input('Digite a expressão'))
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append(simbolo)
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
print(f'Expressão válida' if len(lista) == 0 else 'Expressão inválida.')
