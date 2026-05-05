import random

def chave_acesso(nome_completo):
    partes = nome_completo.strip().split()
    primeiro_nome = partes[0]
    segundo_nome = partes[1] if len(partes) > 1 else "X"

    letras = primeiro_nome[:2].upper() + segundo_nome[0].upper()
    digitos = str(random.randint(1000, 9999))

    return letras + digitos