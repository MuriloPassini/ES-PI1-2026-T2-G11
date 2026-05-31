def validar_titulo(titulo):
    if not titulo.isdigit() or len(titulo) != 12:
        return False

    numeros = list(map(int, titulo))
    estado = numeros[8] * 10 + numeros[9]  # código do estado (01=SP, 02=MG)

    soma1 = 0
    peso = 2
    for i in range(8):
        soma1 += numeros[i] * peso
        peso += 1

    resto1 = soma1 % 11
    if estado in (1, 2):  # SP ou MG
        digito1 = 1 if resto1 == 0 else resto1
    else:
        digito1 = 0 if resto1 in (0, 1) else resto1

    soma2 = numeros[8] * 7 + numeros[9] * 8 + digito1 * 9
    resto2 = soma2 % 11

    if estado in (1, 2):  # SP ou MG
        digito2 = 1 if resto2 == 0 else resto2
    else:
        digito2 = 0 if resto2 in (0, 1) else resto2

    if digito1 == numeros[10] and digito2 == numeros[11]:
        print('Titulo válido')
        return True
    else:
        print('Titulo Invalido')
        return False
#Comandos para testar o codigo: 
#titulo = input("Coloque seu título: ").strip()
#validar_titulo(titulo)