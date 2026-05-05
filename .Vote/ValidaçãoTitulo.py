def validar_titulo(titulo): 
    # Esse primeiro if garante que so serão digitados numeros e exatamente 12.
    if not titulo.isdigit() or len(titulo) !=12:
        return False  
    # esse transforma a string em uma lista de numeros inteiros.
    numeros = list(map(int, titulo))
    soma = 0
    peso = 2
    
    # Cálculo do primeiro dígito verificador
    # esse for pega os primeiros 8 itens de tras pra frente, comecando do 7 e indo até o 0 multiplicando cada numero pelo peso, começando no 2 e indo até o 9.
    for i in range(7, -1, -1):
        soma += numeros[i] * peso
        peso += 1
        if peso > 9:
            peso = 2
    # Se este resto der menor que 2, o digito é 0, caso for maior que 2, o dígito é 11 - resto.
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # O segundo dígito pega os numeros de posição 8 e 9, estado do titulo, com os pesos 7 e 6.
    soma = 0
    peso = 7

    for i in range(8, 10):
        soma += numeros[i] * peso
        peso -= 1
    # Depois adiciona o digito1 * 9 na soma.
    soma += digito1 * 9
    # Faz a mesma coisa fez no primeiro dígito.
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    # Aqui ele compara o que foi calculado com os 2 ultimos numeros do titulo, se bater deu certo, se não deu errado!
    return digito1 == numeros[10] and digito2 == numeros[11]
