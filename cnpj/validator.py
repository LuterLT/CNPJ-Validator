from .converter import converter_cnpj

def validar_cnpj(cnpj):
    '''Vai validar o cnpj retornando True para correto e False para CNPJ inválido'''
    digit_cnpj = converter_cnpj(cnpj)
    cal_cnpj = digit_cnpj.copy()

    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(peso1[i] * cal_cnpj[i] for i in range(12))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1
    cal_cnpj[12] = digito1

    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(peso2[i] * cal_cnpj[i] for i in range(13))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    return digit_cnpj[12] == digito1 and digit_cnpj[13] == digito2