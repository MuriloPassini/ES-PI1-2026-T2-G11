def validar_titulo(titulo): 
    if not titulo.isdigit() or len(titulo) !=12:
        return False   
    numeros = list(map(int, titulo))
    soma = 0
    peso = 2
    
    # Primeiro dígito
    for i in range(7, -1, -1):
        soma += numeros[i] * peso
        peso += 1
        if peso > 9:
            peso = 2

    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Segundo dígito
    soma = 0
    peso = 7

    for i in range(8, 10):
        soma += numeros[i] * peso
        peso -= 1

    soma += digito1 * 9

    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    return digito1 == numeros[10] and digito2 == numeros[11]
