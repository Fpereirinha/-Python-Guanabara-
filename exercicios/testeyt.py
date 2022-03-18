import time
print('\033[34m{:=^40}\033[m'.format(' CASAS BAHIA '))
preco = float(input('Preço total das compras: R$'))
blue = '\033[36m'
red = '\033[31m'
green = '\033[32m'
end = '\033[m'


print('''[1] À vista DINHEIRO/CHEQUE ({}10% de desconto{}):
[2] À vista CARTÃO ({}5% de desconto{}):
[3] Até 2X no CARTÃO (preço normal):
[4] 3 ou Mais vezes no CARTÃO ({}20% de JUROS{}):
'''.format(blue, end, blue, end, red, end))
opcao = int(input('Opção: >'))
if opcao == 1:
    desc = (preco*10)/100
    desc2 = preco - desc
    print('Olá essa é uma mensagem gravada.')
    time.sleep(0.5)
    print('O meio de pagamento escolhido foi em DINHEIRO/CHEQUE')
    time.sleep(0.5)
    print('{}Processando...{}'.format(blue, end))
    time.sleep(2)
    print('O novo valor passou a ser {}, com desconto à vista em dinheiro.'.format(desc2))
    time.sleep(3)
    print('Muito obrigado por comprar conosco.')
    print('AVALIE O ATENDIMENTO VIRTUAL EM NOSSO SITE: https://www.casasbahia.com.br')
elif opcao == 2:
    desc = (preco*5)/100
    desc2 = preco - desc
    print('Olá essa é uma mensagem gravada.')
    time.sleep(0.5)
    print('O meio de pagamento escolhido foi À VISTA NO CARTÃO.')
    time.sleep(0.5)
    print('{}Processando...{}'.format(blue, end))
    time.sleep(2)
    print('O novo valor passou a ser {}, com desconto à vista no cartão.'.format(desc2))
    time.sleep(0.2)
    senha = str(input('DIGITE SUA SENHA: '))
    time.sleep(0.4)
    print('{}Processando...{}'.format(blue, end))
    time.sleep(2)
    print('{}PAGAMENTO APROVADO!{}'.format(green, end))
    time.sleep(3)
    print('Muito obrigado por comprar conosco.')
    print('AVALIE O ATENDIMENTO VIRTUAL EM NOSSO SITE: https://www.casasbahia.com.br')
elif opcao == 3:
    print('Olá essa é uma mensagem gravada.')
    time.sleep(0.5)
    print('Com a sua escolha sendo 2X no CARTÃO, não haverá desconto.')
    time.sleep(0.5)
    senha = str(input('DIGITE SUA SENHA: '))
    time.sleep(0.4)
    print('{}Processando...{}'.format(blue, end))
    time.sleep(2)
    print('{}PAGAMENTO APROVADO!{}'.format(green, end))
    time.sleep(3)
    print('Muito obrigado por comprar conosco.')
    print('AVALIE O ATENDIMENTO VIRTUAL EM NOSSO SITE: https://www.casasbahia.com.br')
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    if parcelas >= 3:
        desc = (preco * 20) / 100
        desc2 = preco + desc
        total = desc2 / parcelas
        print('Olá essa é uma mensagem gravada.')
        time.sleep(0.5)
        print('O meio de pagamento escolhido foi {}x no CARTÃO.'.format(parcelas))
        time.sleep(0.5)
        print('{}Processando...{}'.format(blue, end))
        time.sleep(2)
        print('O novo valor passou a ser {}, com o aumento de juros em {} parcelas de R${:.2f}.'.format(desc2, parcelas, total))
        time.sleep(0.2)
        senha = str(input('DIGITE SUA SENHA: '))
        time.sleep(0.4)
        print('{}Processando...{}'.format(blue, end))
        time.sleep(2)
        print('{}PAGAMENTO APROVADO!{}'.format(green, end))
        time.sleep(3)
        print('Muito obrigado por comprar conosco.')
        print('AVALIE O ATENDIMENTO VIRTUAL EM NOSSO SITE: wwwcasasbahiacombr')
else:
    print('{}Opcão Incorreta. TENTE NOVAMENTE...{}'.format(red, end))