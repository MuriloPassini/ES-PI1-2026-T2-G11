import mysql.connector

conexao = mysql.connector.connect(
    host="BD-ACD",
    user="BD250226129",
    password="Gcpop08",
    database="Candidato"
)

cursor = conexao.cursor()

nome_candidato = input("digite o seu nome de candidato: ")
while not nome_candidato.isalpha():
        print("nome inválido! digite apenas letras.")
        nome_candidato = input("digite o seu nome de candidato: ")

numcandidato = input("digite o seu numero de candidato: ")
while not (numcandidato.isdigit() and len(numcandidato) == 2):
        print("numero de candidato invalido! digite novamente ")
        numcandidato = input("digite o seu numero de candidato: ")
    
partidocandidato = input("digite qual o seu partido: ")
while not partidocandidato.isalpha():
        print("partido inválido! digite apenas letras.")
        partidocandidato = input("digite qual o seu partido: ")

sql = """
INSERT INTO candidatos (nome, numero, partido)
VALUES (%s, %s, %s)
"""

valores = (nome_candidato, numcandidato, partidocandidato)

cursor.execute(sql, valores)
conexao.commit()

print("Candidato cadastrado com sucesso!")

cursor.close()
conexao.close()