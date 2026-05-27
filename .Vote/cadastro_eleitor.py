from banco import conectar_bd, fechar_bd
from chave_acesso import chave_acesso
from editar_eleitor import editar_eleitor
from validacoes import validacaocpf, validar_titulo
import criptografia


def mostrar_eleitor(eleitor):
    cpf = criptografia.descriptografar(eleitor[1])

    print("=" * 35)
    print(f"Nome: {eleitor[0]}")
    print(f"CPF: {cpf}")
    print(f"Titulo: {eleitor[2]}")
    print(f"Mesario: {eleitor[3]}")
    print("=" * 35)


def listar_eleitores():
    conexao, cursor = conectar_bd()

    cursor.execute(
        """
        SELECT Nome_Completo, CPF, Titulo_de_eleitor, Mesario
        FROM Eleitores
        """
    )
    eleitores = cursor.fetchall()

    print(f'{"Lista de Eleitores":^57}')
    if not eleitores:
        print("Nenhum eleitor cadastrado.")

    for eleitor in eleitores:
        mostrar_eleitor(eleitor)

    fechar_bd(conexao, cursor)


def cadastrar_eleitor():
    conexao, cursor = conectar_bd()

    nome = input("Insira o nome do eleitor: ").strip()
    while nome == "" or not nome.replace(" ", "").isalpha():
        print("Nome invalido. O nome nao pode ficar vazio.")
        nome = input("Insira o nome do eleitor: ").strip()

    titulo = input("Insira o titulo de eleitor do mesmo: ").strip()
    while validar_titulo(titulo) is False:
        print("Titulo de eleitor invalido. O titulo deve conter apenas numeros, ter 12 digitos e ser valido.")
        titulo = input("Insira o titulo de eleitor do mesmo: ").strip()

    cpf = input("Insira o CPF do eleitor: ").strip().replace(".", "").replace("-", "")
    while validacaocpf(cpf) is False:
        print("CPF invalido. O CPF deve conter apenas numeros, ter 11 digitos e ser valido.")
        cpf = input("Insira o CPF do eleitor: ").strip().replace(".", "").replace("-", "")

    mesario = input("O eleitor e mesario? S/N: ").strip().upper()
    while mesario not in ("S", "N"):
        print("Opcao de mesario invalida. Use S ou N.")
        mesario = input("O eleitor e mesario? S/N: ").strip().upper()

    chave = chave_acesso(nome)
    cpf_criptografado = criptografia.criptografar(cpf)
    chave_criptografada = criptografia.criptografar(chave)

    print("=" * 35)
    print("Eleitor cadastrado com sucesso!")
    print("Resumo do eleitor:")
    print(f"Nome: {nome}")
    print(f"Titulo de eleitor: {titulo}")
    print(f"CPF: {cpf}")
    print(f"E mesario?: {mesario}")
    print(f"Chave de acesso: {chave}")
    print("GUARDE SUA CHAVE DE ACESSO!")
    print("=" * 35)

    cursor.execute(
        """
        INSERT INTO Eleitores
            (Nome_Completo, CPF, Titulo_de_eleitor, Chave_de_acesso, Mesario)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (nome, cpf_criptografado, titulo, chave_criptografada, mesario)
    )
    conexao.commit()
    fechar_bd(conexao, cursor)


def buscar_eleitor():
    conexao, cursor = conectar_bd()

    print("Escolha uma opcao para buscar o eleitor:")
    print("1. Nome")
    print("2. Titulo")
    print("3. CPF")
    opcao = input("Digite sua opcao: ").strip()

    if opcao == "1":
        nome_buscar = input("Digite o nome do eleitor: ").strip()
        cursor.execute(
            """
            SELECT Nome_Completo, CPF, Titulo_de_eleitor, Mesario
            FROM Eleitores
            WHERE Nome_Completo = %s
            """,
            (nome_buscar,)
        )
        resultados = cursor.fetchall()
    elif opcao == "2":
        titulo_buscar = input("Digite o titulo do eleitor: ").strip()
        cursor.execute(
            """
            SELECT Nome_Completo, CPF, Titulo_de_eleitor, Mesario
            FROM Eleitores
            WHERE Titulo_de_eleitor = %s
            """,
            (titulo_buscar,)
        )
        resultados = cursor.fetchall()
    elif opcao == "3":
        cpf_buscar = input("Digite o CPF do eleitor: ").strip().replace(".", "").replace("-", "")
        cpf_criptografado = criptografia.criptografar(cpf_buscar)
        cursor.execute(
            """
            SELECT Nome_Completo, CPF, Titulo_de_eleitor, Mesario
            FROM Eleitores
            WHERE CPF = %s
            """,
            (cpf_criptografado,)
        )
        resultados = cursor.fetchall()
    else:
        print("Opcao invalida!")
        fechar_bd(conexao, cursor)
        return

    if resultados:
        for eleitor in resultados:
            mostrar_eleitor(eleitor)
    else:
        print("Eleitor nao encontrado.")

    fechar_bd(conexao, cursor)


def deletar_eleitor():
    conexao, cursor = conectar_bd()

    titulo_buscar = input("Digite o titulo do eleitor que deseja excluir: ").strip()
    cursor.execute(
        """
        SELECT Nome_Completo, CPF, Titulo_de_eleitor, Mesario
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
        """,
        (titulo_buscar,)
    )
    eleitor = cursor.fetchone()

    if eleitor:
        print("\nEleitor encontrado!")
        mostrar_eleitor(eleitor)
        confirmar = input("Deseja confirmar? (s/n): ").strip().lower()

        if confirmar == "s":
            cursor.execute(
                "DELETE FROM Eleitores WHERE Titulo_de_eleitor = %s",
                (titulo_buscar,)
            )
            conexao.commit()
            print("\nEleitor deletado com sucesso!")
        else:
            print("Operacao cancelada!")
    else:
        print("Eleitor nao encontrado.")

    fechar_bd(conexao, cursor)


def menu_eleitores():
    executando = True
    while executando:
        print("\n" + "=" * 30)
        print("   SISTEMA DE ELEITORES")
        print("=" * 30)
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Editar")
        print("5 - Deletar")
        print("6 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_eleitor()
        elif opcao == "2":
            listar_eleitores()
        elif opcao == "3":
            buscar_eleitor()
        elif opcao == "4":
            editar_eleitor()
        elif opcao == "5":
            deletar_eleitor()
        elif opcao == "6":
            print("Saindo...")
            executando = False
        else:
            print("Opcao invalida!")
