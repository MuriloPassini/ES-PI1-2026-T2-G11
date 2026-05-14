# Lista que armazena os logs do sistema
logs_ocorrencias = []

# Lista que armazena os protocolos de votação
protocolos_votacao = []

def registrar_log(evento):

    # Adiciona o evento na lista de logs
    logs_ocorrencias.append(evento)

    # Mostra mensagem de confirmação
    print("\nLog registrado com sucesso!")

def exibir_logs():
    print("\nLOGS DE OCORRÊNCIAS-->")

    # Verifica se não existem logs
    if len(logs_ocorrencias) == 0:
        print("Nenhum log encontrado.")

    else:
        # Percorre toda a lista de logs
        for indice, log in enumerate(logs_ocorrencias, start=1):

            # Mostra cada log numerado
            print(f"{indice}. {log}")

def gerar_protocolo(nome_eleitor):

    # Cria um protocolo usando o tamanho da lista
    protocolo = "PROTOCOLO-" + str(len(protocolos_votacao) + 1)

    # Junta o nome do eleitor com o protocolo
    registro = {
        "eleitor": nome_eleitor,
        "protocolo": protocolo
    }

    # Adiciona o registro na lista
    protocolos_votacao.append(registro)

    # Registra no log que um voto foi realizado
    registrar_log(f"Voto registrado para {nome_eleitor}")

    # Mostra o protocolo gerado
    print(f"\nProtocolo gerado: {protocolo}")

def exibir_protocolos():
    print("\nPROTOCOLOS DE VOTAÇÃO-->")

    # Verifica se não existem protocolos
    if len(protocolos_votacao) == 0:
        print("Nenhum protocolo encontrado.")

    else:
        # Ordena alfabeticamente pelo protocolo
        protocolos_ordenados = sorted(
            protocolos_votacao,
            key=lambda item: item["protocolo"]
        )

        # Percorre a lista ordenada
        for item in protocolos_ordenados:

            # Mostra eleitor e protocolo
            print(
                f"Eleitor: {item['eleitor']} | "
                f"Protocolo: {item['protocolo']}"
            )

while True:
    print(" SISTEMA DE AUDITORIA DA VOTAÇÃO-->")
    
    print("1 - Registrar Log")
    print("2 - Exibir Logs")
    print("3 - Gerar Protocolo")
    print("4 - Exibir Protocolos")
    print("5 - Encerrar Sistema")

    # Usuário escolhe uma opção
    opcao = input("\nDigite uma opção: ")

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
        print("\nOpção inválida. Digite uma das opções válidas.")