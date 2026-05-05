def validar_titulo(titulo):
    # Esse primeiro if garante que so serão digitados numeros e exatamente 12.
    if not titulo.isdigit() or len(titulo) != 12:
        return False  

    # esse transforma a string em uma lista de numeros inteiros.
    numeros = list(map(int, titulo))

    # Esse codigo verifica o digito
    def calcular_digito(numeros_base):
        soma = 0
        peso = 2

        # esse for pega os numeros de tras pra frente multiplicando cada numero pelo peso,
        # começando no 2 e indo até o 9, depois reinicia para 2.
        for i in range(len(numeros_base)-1, -1, -1):
            soma += numeros_base[i] * peso
            peso += 1
            if peso > 9:
                peso = 2

        # Se este resto der menor que 2, o digito é 0, caso for maior que 2, o dígito é 11 - resto.
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Primeiro dígito (usa os 8 primeiros numeros do titulo)
    digito1 = calcular_digito(numeros[:8])

    # O segundo dígito usa os 10 primeiros numeros + o primeiro digito calculado
    base_segundo = numeros[:10] + [digito1]

    # Faz a mesma coisa que fez no primeiro dígito
    digito2 = calcular_digito(base_segundo)

    # Aqui ele compara o que foi calculado com os 2 ultimos numeros do titulo,
    # se bater deu certo, se não deu errado!
    return digito1 == numeros[10] and digito2 == numeros[11]

# O codigo abaixo é pra fazer o teste
#titulo = input("coloque seu titulo: ")

#if validar_titulo(titulo):
#    print("titulo valido")
#else:
#    print("titulo invalido")

#Validação cpf
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
