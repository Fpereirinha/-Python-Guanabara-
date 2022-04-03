import urllib.request
import requests

try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print('Inacessivel.')
else:
    print('Tudo ok')
    print(site.read())


def conect():
    try:
        requests.get('http://pudim.com.br/')
        return True
    except:
        return False

if conect():
    print('Pudim está conectado')
else:
    print('Pudim está Desconectado')