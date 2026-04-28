from validarcpf import validacaocpf
import banco
def cadastrocandidato():
    nome_candidato = input("digite o seu nome de candidato: ")
    while nome_candidato.isdigit():
        print("nome inválido! digite apenas letras.")
        nome_candidato = input("digite o seu nome de candidato: ")
    numcandidato = input("digite o seu numero de candidato: ")
    while len(numcandidato)!=2 and not numcandidato.isdigit():
        print("numero de candidato invalido! digite novamente ")
        numcandidato = input("digite o seu numero de candidato: ")
    partidocandidato = input("digite qual o seu partido: ")
    while partidocandidato.isdigit():
        print("partido inválido! digite apenas letras.")
        partidocandidato = input("digite qual o seu partido: ")