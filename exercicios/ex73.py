times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f'Os 5 primeiros times são: {times[:5]}\n'
      f'Os 4 ultimos são: {times[-4:]}\n'
      f'O chapecoense está em {times.index("Chapecoense")+1}°\n'
      f'Os números em ordem são {sorted(times)}')
