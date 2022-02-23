import re

url = 'https://www.bytebank.com.br/cambio'

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio') # entre parênteses significa que tem que ser extamento igual.

match = padrao_url.match(url) # O Método match vê se a string toda é uma url

if not match:
    raise ValueError("A URL não é válida.")

print("URL válida.")