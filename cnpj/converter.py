from .exceptions import CNPJInvalidError


def converter_cnpj(cnpj):
    '''
    Essa função vai converter o cnpj alfa númerico para inteiro
    '''
    digit_cnpj = []
    if len(cnpj) != 14:
        raise CNPJInvalidError("CNPJ inválido, o tamanho não está equivalente a 14 dígitos!")

    for c in cnpj:
        if c.isdigit():
            digit_cnpj.append(int(c))
        elif c.isalpha():
            digit_cnpj.append(ord(c.lower()))
        else:
            raise CNPJInvalidError("CNPJ inválido, caracter inválido dentro do cnpj")
    return digit_cnpj
            