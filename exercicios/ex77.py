c = ('Apender','Programar','Executar','Transparência', 'Igualdade', 'Sinceridade', 'Consistência', 'doido', 'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
a = e = i = o = u = soma = 0
for p in c:
    print(f'Na palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
        if letra.upper() in 'A':
            a += 1
        elif letra.upper() in 'E':
            e += 1
        elif letra.upper() in 'I':
            i += 1
        elif letra.upper() in 'O':
            o += 1
        elif letra.upper() in 'U':
            u += 1
    print(f'\nO total de A é {a}.\nO total de E é {e}.'
          f'\nO total de I é {i}.\nO total de O é {o}.'
          f'\nO total de U é {u}')
    soma += a + e + i + o + u
    a = e = i = o = u = 0
print(f'total de {soma} vogais')
