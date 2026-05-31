def validacaocpf(cpf):
    """
    Valida um CPF pelo tamanho, repeticao de digitos e digitos verificadores.

    Args:
        cpf (str): CPF informado pelo usuario, apenas com numeros.

    Returns:
        bool: True se o CPF for valido, False caso contrario.
    """
    cpf = cpf.strip()

    if len(cpf) != 11 or not cpf.isdigit() or len(set(cpf)) == 1:
        return False

    digitoscpf = [int(d) for d in cpf]

    soma1 = 0
    peso1 = 10
    for i in range(9):
        soma1 += digitoscpf[i] * peso1
        peso1 -= 1

    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = 0
    peso2 = 11
    for i in range(10):
        soma2 += digitoscpf[i] * peso2
        peso2 -= 1

    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    return digito1 == digitoscpf[9] and digito2 == digitoscpf[10]
