from banco import conectar_bd, fechar_bd
from chave_acesso import chave_acesso
from validacoes import validacaocpf, validar_titulo


def cadastrar_eleitor():
    conexao, cursor = conectar_bd()

    nome = input("Insira o nome do eleitor: ").strip()
    while not nome:
        print("Nome invalido. O nome nao pode ficar vazio.")
        nome = input("Insira o nome do eleitor: ").strip()

    titulo = input("Insira o titulo de eleitor do mesmo: ").strip()
    cpf = input("Insira o CPF do eleitor: ").strip()
    mesario = input("O eleitor e mesario? S/N: ").strip().upper()

    if mesario not in ("S", "N"):
        print("Opcao de mesario invalida. Use S ou N.")
        fechar_bd(conexao, cursor)
        return

    titulo_valido = validar_titulo(titulo)
    cpf_valido = validacaocpf(cpf)
    chave = chave_acesso(nome)

    if titulo_valido and cpf_valido:
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
            (nome, cpf, titulo, chave, mesario)
        )
        conexao.commit()
    else:
        print("Dados invalidos! Verifique o CPF e o titulo de eleitor.")

    fechar_bd(conexao, cursor)
