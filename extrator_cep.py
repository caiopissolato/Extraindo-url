endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
import re
# Padrão de um CEP 5 dígitos + hífen + 3 dígitos
#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]") # a interrogação é para um valor opcional, pode ou não ter o hífen
#padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
#padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # O {0,1} significa que aquele símbolo pode aparecer 0 ou 1 vez.
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") # Esses intervalos também poderiam ser de letras como [a-z]...

busca = padrao.search(endereco) # O Método search busca um valor dentro de uma string

if busca:
    cep = busca.group()
    print(cep)

# Expressões regulares https://docs.python.org/pt-br/3/howto/regex.html#regex-howto