import mysql.connector

conexao = mysql.connector.connect(
    host="BD-ACD",
    user="BD250226129",
    password="Gcpop08",
    database="Candidato"
)

def cadastrocandidato():
    nome_candidato = input("Digite o seu nome de candidato: ").strip()
    while not nome_candidato.isalpha():
        print("Nome inválido! Digite apenas letras.")
        nome_candidato = input("Digite o seu nome de candidato: ")

    numcandidato = input("Digite o seu número de candidato: ").strip()

    while not (numcandidato.isdigit() and len(numcandidato) == 2):
        print("Número de candidato invalido! Digite novamente ")
        numcandidato = input("digite o seu numero de candidato: ")
    
    partidocandidato = input("Digite qual o seu partido: ")
    while not partidocandidato.isalpha():
        print("Partido inválido! Digite apenas letras.")
        partidocandidato = input("Digite qual o seu partido: ")