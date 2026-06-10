def validacaotitulo(titulo):
    """
    Valida um titulo de eleitor pelo tamanho, formato e digitos verificadores.

    Args:
        titulo (str): Numero do titulo de eleitor informado pelo usuario.

    Returns:
        bool: True se o titulo for valido, False caso contrario.
    """
    if not titulo.isdigit() or len(titulo) != 12:
        return False

    numeros = list(map(int, titulo))
    estado = numeros[8] * 10 + numeros[9]  # codigo da UF

    if estado < 1 or estado > 28:
        return False

    soma1 = 0
    for i in range(8):
        soma1 += numeros[i] * (i + 2)

    resto1 = soma1 % 11
    if resto1 == 10:
        digito1 = 0
    else:
        digito1 = resto1

    if estado in (1, 2) and resto1 == 0:
        digito1 = 1

    soma2 = numeros[8] * 7 + numeros[9] * 8 + digito1 * 9
    resto2 = soma2 % 11
    if resto2 == 10:
        digito2 = 0
    else:
        digito2 = resto2

    if estado in (1, 2) and resto2 == 0:
        digito2 = 1

    return digito1 == numeros[10] and digito2 == numeros[11]


def validacaocpf(cpf):
    """
    Valida um CPF pelo tamanho, repeticao de digitos e digitos verificadores.

    Args:
        cpf (str): CPF informado pelo usuario, apenas com numeros.

    Returns:
        bool: True se o CPF for valido, False caso contrario.
    """
    #Essa primeira parte verifica se tem 11 digitos, se é apenas digitos e se não sao numeros repetidos
    if len(cpf)!=11 or not cpf.isdigit() or len(set(cpf))==1:
        return False
    else:
        digitoscpf=[]
        for d in cpf:
            digitoscpf.append(int(d))
        #Validacao do primeiro digito
        soma1=0
        dg=10 # Quantidade de digitos para a multiplicação
        for i in range(9):
            soma1 += digitoscpf[i]*dg  # Aqui nesta linha pegará os 9 primeiros digitos e multiplicar cada numero pelo descrescente dos digitos(coloquei a variavel como 'dg')
            dg -= 1  # Aqui o digito da multiplicação vai diminuindo para que não multiplique todos os 9 números por 10

        resto1=soma1%11 #Aqui calcula-se o resto desta soma para descobrir o primeiro numero verificador
        if resto1<2:
            resto1=0
        else:
            if resto1>=2:
                resto1=11-resto1

        #validação segundo digito
        soma2=0
        dg2=11
        for i in range(10): 
            soma2 += digitoscpf[i]*dg2 #É a mesma coisa, porém desta vez a multiplicação começa com '11' invés de '10'
            dg2 -= 1

        resto2=soma2%11
        if resto2<2:
            resto2=0
        else: 
            if resto2>=2:
                resto2=11-resto2

        if resto1==digitoscpf[9] and resto2==digitoscpf[10]:
            return True
        else:
            return False
