import criptografia
from banco import conectar_bd, fechar_bd


logs_ocorrencias = []
protocolos_votacao = []


def registrar_log(evento):
    logs_ocorrencias.append(evento)
    print("\nLog registrado com sucesso!")


def exibir_logs():
    print("\nLOGS DE OCORRENCIAS")

    if len(logs_ocorrencias) == 0:
        print("Nenhum log encontrado.")
        return

    for indice, log in enumerate(logs_ocorrencias, start=1):
        print(f"{indice}. {log}")


def gerar_protocolo(nome_eleitor):
    protocolo = "PROTOCOLO-" + str(len(protocolos_votacao) + 1)

    registro = {
        "eleitor": nome_eleitor,
        "protocolo": protocolo
    }
    protocolos_votacao.append(registro)

    registrar_log(f"Voto registrado para {nome_eleitor}")
    print(f"\nProtocolo gerado: {protocolo}")


def exibir_protocolos():
    print("\nPROTOCOLOS DE VOTACAO")

    conexao, cursor = conectar_bd()

    cursor.execute(
        """
        SELECT protocolo, titulo_eleitor, numero_candidato, data_hora
        FROM votos
        ORDER BY data_hora
        """
    )
    votos = cursor.fetchall()

    if len(votos) == 0:
        print("Nenhum protocolo encontrado.")
        fechar_bd(conexao, cursor)
        return

    for voto in votos:
        protocolo = criptografia.descriptografar(voto[0])
        print(f"Titulo: {voto[1]} | Candidato: {voto[2]} | Protocolo: {protocolo}")

    fechar_bd(conexao, cursor)


def menu_auditoria():
    while True:
        print("\nSISTEMA DE AUDITORIA DA VOTACAO")
        print("1 - Registrar Log")
        print("2 - Exibir Logs")
        print("3 - Gerar Protocolo")
        print("4 - Exibir Protocolos")
        print("5 - Encerrar Sistema")

        opcao = input("\nDigite uma opcao: ").strip()

        if opcao == "1":
            evento = input("Digite o evento ocorrido: ")
            registrar_log(evento)
        elif opcao == "2":
            exibir_logs()
        elif opcao == "3":
            nome = input("Digite o nome do eleitor: ")
            gerar_protocolo(nome)
        elif opcao == "4":
            exibir_protocolos()
        elif opcao == "5":
            registrar_log("Sistema encerrado.")
            print("\nSistema encerrado com sucesso!")
            break
        else:
            print("\nOpcao invalida. Digite uma das opcoes validas.")


if __name__ == "__main__":
    menu_auditoria()
