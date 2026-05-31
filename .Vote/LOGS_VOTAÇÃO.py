from datetime import datetime
from pathlib import Path

ARQUIVO_LOG = Path(__file__).resolve().parent / "logs_ocorrencias.txt"
ARQUIVO_PROTOCOLOS = Path(__file__).resolve().parent / "protocolos.txt"

def registrar_protocolo(protocolo):
    with open(ARQUIVO_PROTOCOLOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{protocolo}\n")

def registrar_log(descricao):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_hora}] {descricao}\n")

def registrar_abertura():
    registrar_log(
        "ABERTURA: Votação iniciada com sucesso. Total de votos zerado."
    )

def registrar_acesso_negado():
    registrar_log(
        "ALERTA: Tentativa de acesso negado"
    )

def registrar_voto_duplo():
    registrar_log(
        "ALERTA: Tentativa de voto duplo"
    )

def registrar_voto_sucesso():
    registrar_log(
        "SUCESSO: Voto realizado com sucesso"
    )

def registrar_encerramento():
    registrar_log(
        "ENCERRAMENTO: Votação finalizada com sucesso."
    )

def exibir_logs():
    print("\n===== LOGS DE OCORRÊNCIAS =====\n")

    try:
        with open(ARQUIVO_LOG, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

            if conteudo.strip():
                print(conteudo)
            else:
                print("Nenhum log registrado.")

    except FileNotFoundError:
        print("Arquivo de log não encontrado.")

def exibir_protocolos():
    print("\n===== PROTOCOLOS DE VOTAÇÃO =====\n")

    try:
        with open(ARQUIVO_PROTOCOLOS, "r", encoding="utf-8") as arquivo:
            protocolos = arquivo.readlines()

            if not protocolos:
                print("Nenhum protocolo registrado.")
                return

            for protocolo in sorted(protocolos):
                print(protocolo.strip())

    except FileNotFoundError:
        print("Arquivo de protocolos não encontrado.")
        
def menu_auditoria():
    while True:
        print("\n===== auditoria =====")
        print("1 - Exibir Logs")
        print("2 - Exibir Protocolos")
        print("0 - Voltar")

        opcao = input("\nDigite o numero da opcao desejada: ")

        match opcao:
            case "1":
                exibir_logs()
            case "2":
                exibir_protocolos()
            case "0":
                break
            case _:
                print("Opção inválida. Digite 1, 2 ou 0.")
