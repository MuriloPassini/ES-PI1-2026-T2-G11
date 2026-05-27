alfabeto = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

matriz_chave = [
    [7, 2],
    [3, 5]
]

caractere_padding = 'C'

matriz_inversa = [
    [25, 26],
    [21, 35]
]

def texto_p_numero(texto):
    texto_em_numero = []
    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            texto_em_numero.append(indice)
    return texto_em_numero


def fazer_matriz_hill(texto_em_numero):
    if len(texto_em_numero) % 2 != 0:
        texto_em_numero.append(alfabeto.index(caractere_padding))

    matrizes_hill = []

    for i in range(0, len(texto_em_numero), 2):
        matriz_hill = [texto_em_numero[i], texto_em_numero[i+1]]
        matrizes_hill.append(matriz_hill)

    return matrizes_hill


def matriz_criptografada(matriz_hill):
    x = matriz_hill[0]
    y = matriz_hill[1]

    novo_x = (matriz_chave[0][0] * x + matriz_chave[0][1] * y) % 36
    novo_y = (matriz_chave[1][0] * x + matriz_chave[1][1] * y) % 36
    
    return [novo_x, novo_y]


def matriz_descriptografada(matriz_hill):
    x = matriz_hill[0]
    y = matriz_hill[1]

    novo_x = (matriz_inversa[0][0] * x + matriz_inversa[0][1] * y) % 36
    novo_y = (matriz_inversa[1][0] * x + matriz_inversa[1][1] * y) % 36

    return [novo_x, novo_y]


def numero_p_texto(numeros):
    texto = ""

    for numero in numeros:
        texto = texto + alfabeto[numero]

    return texto


def criptografar(texto):
    texto = texto.upper()

    texto_em_numero = texto_p_numero(texto)
    matrizes_hill = fazer_matriz_hill(texto_em_numero)

    numeros_criptografados = []

    for matriz_hill in matrizes_hill:
        resultado = matriz_criptografada(matriz_hill)
        numeros_criptografados.append(resultado[0])
        numeros_criptografados.append(resultado[1])

    texto_criptografado = numero_p_texto(numeros_criptografados)

    return texto_criptografado


def descriptografar(texto):
    texto = texto.upper()

    texto_em_numero = texto_p_numero(texto)
    matrizes_hill = fazer_matriz_hill(texto_em_numero)

    numeros_descriptografados = []

    for matriz_hill in matrizes_hill:
        resultado = matriz_descriptografada(matriz_hill)
        numeros_descriptografados.append(resultado[0])
        numeros_descriptografados.append(resultado[1])

    texto_descriptografado = numero_p_texto(numeros_descriptografados)

    if texto_descriptografado[-1] == caractere_padding:
        texto_descriptografado = texto_descriptografado[:-1]

    return texto_descriptografado
