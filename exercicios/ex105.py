def media(*num, sit=False):
    lista = {}
    lista['Total'] = len(num)
    lista['Maior'] = max(num)
    lista['Menor'] = min(num)
    lista['Média'] = round((sum(num)/len(num)), 2)
    if sit:
        if round((sum(num)/len(num)), 2) < 6:
            lista['Situação'] = 'RUIM'
        else:
            lista['Situação'] = 'BOM'
    return lista



for key, valor in media(5, 7, 6, 4, 5, 6, 7, sit=True).items():
    print(f'{key}={valor}')

