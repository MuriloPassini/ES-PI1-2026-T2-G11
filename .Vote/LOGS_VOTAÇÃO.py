from datetime import datetime

ARQUIVO_LOG = "logs_ocorrencias.txt"


def registrar_log(tipo, mensagem):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as log:

        log.write(
            f"[{timestamp}] [{tipo}] {mensagem}\n"
        )


def exibir_logs():

    print('\nLOGS\n')

    try:

        with open(ARQUIVO_LOG, "r", encoding="utf-8") as log:

            conteudo = log.read()

            if conteudo.strip() == "":
                print("Nenhum log registrado.")

            else:
                print(conteudo)

    except FileNotFoundError:

        print("Arquivo de log não encontrado.")
