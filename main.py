url = "http://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao] # sem passar o argumento do início ele interpreta que precisa começar do início da string

print(url_base)

url_parametros = url[indice_interrogacao+1:] # sem passar o argumento do fim ele interpreta que precisa ir até o fim
print(url_parametros)

parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor : indice_e_comercial]
print(valor)

testa = url.find("cambio") # posso passar uma string como parâmetro para find que retornará a posição inicial dela, caso não encontre ele retorna -1
print(testa)