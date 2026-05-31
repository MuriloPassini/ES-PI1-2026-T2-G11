from datetime import datetime
from pathlib import Path

ARQUIVO_LOG = Path(__file__).resolve().parent / "logs_ocorrencias.txt"
ARQUIVO_PROTOCOLOS = Path(__file__).resolve().parent / "protocolos.txt"

def registrar_protocolo(protocolo):
    """
    Salva um protocolo de voto no arquivo de protocolos.

    Args:
        protocolo (str): Codigo de protocolo gerado para o voto.

    Returns:
        None: A funcao apenas grava o protocolo no arquivo.
    """
    with open(ARQUIVO_PROTOCOLOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{protocolo}\n")

def registrar_log(descricao):
    """
    Registra uma ocorrencia no arquivo de logs com data e hora.

    Args:
        descricao (str): Texto que descreve a ocorrencia registrada.

    Returns:
        None: A funcao apenas grava a ocorrencia no arquivo.
    """
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_hora}] {descricao}\n")

def registrar_abertura():
    """
    Registra no log que a votacao foi aberta.

    Args:
        Nenhum.

    Returns:
        None: A funcao apenas envia a mensagem de abertura para o log.
    """
    registrar_log(
        "ABERTURA: Votação iniciada com sucesso. Total de votos zerado."
    )

def registrar_acesso_negado():
    """
    Registra no log uma tentativa de acesso negado.

    Args:
        Nenhum.

    Returns:
        None: A funcao apenas envia a mensagem de alerta para o log.
    """
    registrar_log(
        "ALERTA: Tentativa de acesso negado"
    )

def registrar_voto_duplo():
    """
    Registra no log uma tentativa de voto duplicado.

    Args:
        Nenhum.

    Returns:
        None: A funcao apenas envia a mensagem de alerta para o log.
    """
    registrar_log(
        "ALERTA: Tentativa de voto duplo"
    )

def registrar_voto_sucesso():
    """
    Registra no log que um voto foi realizado com sucesso.

    Args:
        Nenhum.

    Returns:
        None: A funcao apenas envia a mensagem de sucesso para o log.
    """
    registrar_log(
        "SUCESSO: Voto realizado com sucesso"
    )

def registrar_encerramento():
    """
    Registra no log que a votacao foi encerrada.

    Args:
        Nenhum.

    Returns:
        None: A funcao apenas envia a mensagem de encerramento para o log.
    """
    registrar_log(
        "ENCERRAMENTO: Votação finalizada com sucesso."
    )

def exibir_logs():
    """
    Exibe no terminal o conteudo do arquivo de logs.

    Args:
        Nenhum.

    Returns:
        None: A funcao imprime os logs ou informa que o arquivo nao foi encontrado.
    """
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
    """
    Exibe no terminal os protocolos salvos no arquivo de protocolos.

    Args:
        Nenhum.

    Returns:
        None: A funcao imprime os protocolos ou informa que o arquivo nao foi encontrado.
    """
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
    """
    Exibe o menu de auditoria para consultar logs e protocolos.

    Args:
        Nenhum.

    Returns:
        None: A funcao controla o menu ate o usuario escolher voltar.
    """
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
