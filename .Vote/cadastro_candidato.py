import mysql.connector

from banco import conectar_bd, fechar_bd


def listar():
    conexao, cursor = conectar_bd()

    cursor.execute("SELECT nome, numero, partido FROM candidatos")
    resultados = cursor.fetchall()

    print(f'{"Lista de Candidatos":^57}')
    if not resultados:
        print("Nenhum candidato cadastrado.")
    for candidato in resultados:
        print(f"Nome: {candidato[0]} | Numero: {candidato[1]} | Partido: {candidato[2]}")

    fechar_bd(conexao, cursor)


def cadastrar():
    conexao, cursor = conectar_bd()

    nome_candidato = input("Digite o seu nome de candidato: ").strip()
    while not nome_candidato.replace(" ", "").isalpha():
        print("Nome invalido! Digite apenas letras.")
        nome_candidato = input("Digite o seu nome de candidato: ").strip()

    numcandidato = input("Digite o seu numero de candidato: ").strip()
    while not (numcandidato.isdigit() and len(numcandidato) == 2):
        print("Numero de candidato invalido! Digite novamente.")
        numcandidato = input("Digite o seu numero de candidato: ").strip()

    partidocandidato = input("Digite qual o seu partido: ").strip()
    while not partidocandidato.replace(" ", "").isalpha():
        print("Partido invalido! Digite apenas letras.")
        partidocandidato = input("Digite qual o seu partido: ").strip()

    try:
        cursor.execute(
            """
            INSERT INTO candidatos (nome, numero, partido)
            VALUES (%s, %s, %s)
            """,
            (nome_candidato, int(numcandidato), partidocandidato)
        )
        conexao.commit()
        print("Candidato cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        if erro.errno == 1062:
            print("Erro: numero de candidato ja existe!")
        else:
            print("Erro:", erro)

    fechar_bd(conexao, cursor)


def buscar():
    conexao, cursor = conectar_bd()

    print("Escolha uma opcao para buscar o(s) candidato(s):")
    print("1. Nome")
    print("2. Numero")
    print("3. Partido")
    opcao = input("Digite sua opcao: ").strip()

    if opcao == "1":
        nome_buscar = input("Digite o nome do candidato: ").strip()
        cursor.execute(
            "SELECT nome, numero, partido FROM candidatos WHERE nome = %s",
            (nome_buscar,)
        )
        resultados = cursor.fetchall()
    elif opcao == "2":
        numero_busca = input("Digite o numero do candidato: ").strip()
        cursor.execute(
            "SELECT nome, numero, partido FROM candidatos WHERE numero = %s",
            (numero_busca,)
        )
        resultados = cursor.fetchall()
    elif opcao == "3":
        partido_buscar = input("Digite o partido dos candidatos que deseja buscar: ").strip()
        cursor.execute(
            "SELECT nome, numero, partido FROM candidatos WHERE partido = %s",
            (partido_buscar,)
        )
        resultados = cursor.fetchall()
    else:
        print("Opcao invalida!")
        fechar_bd(conexao, cursor)
        return

    if resultados:
        for candidato in resultados:
            print("=" * 30)
            print(f"Nome    : {candidato[0]}")
            print(f"Numero  : {candidato[1]}")
            print(f"Partido : {candidato[2]}")
            print("=" * 30)
    else:
        print("Candidato nao encontrado.")

    fechar_bd(conexao, cursor)


def deletarcandi():
    conexao, cursor = conectar_bd()

    numero_busca = input("Digite o numero do candidato que deseja excluir: ").strip()
    cursor.execute(
        "SELECT nome, numero, partido FROM candidatos WHERE numero = %s",
        (numero_busca,)
    )
    resultado = cursor.fetchone()

    if resultado:
        print("\nCandidato encontrado!")
        print("=" * 30)
        print(f"Nome: {resultado[0]}")
        print(f"Numero: {resultado[1]}")
        print(f"Partido: {resultado[2]}")
        print("=" * 30)
        confirmar = input("Deseja confirmar? (s/n): ").strip().lower()
        if confirmar == "s":
            cursor.execute("DELETE FROM candidatos WHERE numero = %s", (numero_busca,))
            conexao.commit()
            print("\nCandidato deletado com sucesso!")
        else:
            print("Operacao cancelada!")
    else:
        print("Candidato nao encontrado.")

    fechar_bd(conexao, cursor)


def menu_candidatos():
    executando = True
    while executando:
        print("\n" + "=" * 30)
        print("   SISTEMA DE CANDIDATOS")
        print("=" * 30)
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Deletar")
        print("5 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            deletarcandi()
        elif opcao == "5":
            print("Saindo...")
            executando = False
        else:
            print("Opcao invalida!")
