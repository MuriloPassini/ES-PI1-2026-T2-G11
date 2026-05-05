#Validação título
def validacaotitulo(titulo): 
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

#Validação cpf trabalho PI
cpf = 0
def validacaocpf():
    #Essa primeira parte verifica se tem 11 digitos, se é apenas digitos e se não sao numeros repetidos
    if len(cpf)!=11 or not cpf.isdigit() or len(set(cpf))==1:
        return False
    else:
        for d in cpf:
            digitoscpf=int(d)
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