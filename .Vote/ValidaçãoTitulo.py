def validar_titulo(titulo):
    if not titulo.isdigit() or len(titulo) != 12:
        return False
    numeros = list(map(int, titulo))
    soma1 = 0
    peso = 2
    for i in range(8):
        soma1 += numeros[i] * peso
        peso += 1
    resto1 = soma1 % 11
    if resto1 == 10:
        digito1 = 0
    else:
        digito1 = resto1
    soma2 = (
        numeros[8] * 7 +
        numeros[9] * 8 +
        digito1 * 9
    )
    resto2 = soma2 % 11
    if resto2 == 10:
        digito2 = 0
    else:
        digito2 = resto2
    return digito1 == numeros[10] and digito2 == numeros[11]
#teste
titulo = input("Coloque seu título: ")
if validar_titulo(titulo):
    print("Título válido")
else:
    print("Título inválido")
