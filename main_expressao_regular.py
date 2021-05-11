import re
from tefefones_br import TelefonesBr

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"
resposta = re.search(padrao, texto)

print(resposta.group())


telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto.format_numero())