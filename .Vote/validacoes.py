def validar_titulo(titulo):
    if not titulo.isdigit() or len(titulo) != 12:
        return False

    numeros = list(map(int, titulo))

    def calcular_digito(numeros_base):
        soma = 0
        peso = 2

        for i in range(len(numeros_base) - 1, -1, -1):
            soma += numeros_base[i] * peso
            peso += 1
            if peso > 9:
                peso = 2

        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    digito1 = calcular_digito(numeros[:8])
    base_segundo = numeros[:10] + [digito1]
    digito2 = calcular_digito(base_segundo)

    return digito1 == numeros[10] and digito2 == numeros[11]


def validacaocpf(cpf):
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
