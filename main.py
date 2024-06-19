from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

# cpf_um = Cpf("86222726569")
# print(cpf_um)

exemplo_cnpj = "35379838000112"

# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
documentp = CpfCnpj(exemplo_cnpj, 'cnpj')

