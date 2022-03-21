from datetime import datetime
dados = {}
dados['Nome'] = str(input('Qual o nome ?'))
dados['Idade'] = datetime.now().year - int(input('Ano de nascença'))
dados['Carteira de trabalho'] = int(input('Qual a carteira (0 se não tiver)'))
if dados['Carteira de trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Qual o ano de contratação ?'))
    dados['Salario'] = int(input('Qual o salario ?'))
    dados['Aposentadoria em'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} = {v}')
