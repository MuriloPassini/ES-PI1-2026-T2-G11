import mysql.connector
from datetime import datetime
import random
import uuid

#informações do usuário
info_completa = 0
while info_completa == 0:
    titulo_eleitor= input("Digite o título de eleitor: ")
    cpf = input("Digite os 4 primeiros dígitos do CPF: "))
    chave_de_acesso = input("Digite sua chave de acesso: "))
    if titulo_eleitor != "" and cpf != "" and chave_de_acesso != "":
        info_completa += 1

#verificar banco
cursor.execute("""
SELECT * FROM eleitores
WHERE titulo_eleitor = %s
AND cpf_inicio = %s
AND chave_acesso = %s
""", (titulo_eleitor, cpf, chave_de_acesso))

eleitor = cursor.fetchone()

if eleitor is None:
    print("Dados inválidos!!!")
    exit()
if eleitor["ja_votou"] == True:
    print("esse eleitor jaa realizou a votação!")
    exit()

#solicitação do numero do candidato
confirmarnum = 0
while confirmarnum == 0:
    numero_candidato = int(input("Digite o numero do seu candidato: "))

#consulta do candidato no banco de dados
    cursor.execute("""
    SELECT * FROM Candidatos
    WHERE numcandidato = %s
    """, (numero_candidato,))

    Candidato = cursor.fetchone()

    if Candidato:
        print("Candidato:")
        print("Nome:", Candidato["nome_candidato"])
        print("Número:", Candidato["numcandidato"])
        print("Partido:", Candidato["partidocandidato"])

    #confirmação de voto
    confirmar = input("Deseja confirmar seu voto (S/N): ")
    if confirmar.upper() == "N":
        continue
    else:
        confirmarnum += 1
