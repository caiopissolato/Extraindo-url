url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao] # sem passar o argumento do início ele interpreta que precisa começar do início da string

print(url_base)

url_parametros = url[indice_interrogacao+1:] # sem passar o argumento do fim ele interpreta que precisa ir até o fim

print(url_parametros)