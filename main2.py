import re
from TelefonesBr import TelefonesBr


telefone = "5571982674427"
telefone_class = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao, telefone)
#print(resposta.group(2))

print(telefone_class)
