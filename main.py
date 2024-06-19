from cpf_cnpj import Documento
from validate_docbr import CNPJ

# cpf_um = Cpf("86222726569")
# print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "86222726569"

# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
# documento = CpfCnpj(exemplo_cnpj, 'cnpj')
# print(documento)
# documento2 = CpfCnpj(exemplo_cpf, 'cpf')
# print(documento2)
documento = Documento.cria_documento(exemplo_cpf)
print(documento)

