from banco import conectar_bd, fechar_bd
import criptografia


def editar_eleitor():
    conexao, cursor = conectar_bd()

    mostrar_eleitores = input("Mostrar todos os eleitores? S/N: ").strip().upper()
    if mostrar_eleitores == "S":
        cursor.execute("SELECT Nome_Completo, CPF, Titulo_de_eleitor FROM Eleitores")
        eleitores = cursor.fetchall()
        for eleitor in eleitores:
            cpf_eleitor = criptografia.descriptografar(eleitor[1])
            print(f"Nome: {eleitor[0]} | CPF: {cpf_eleitor} | Titulo: {eleitor[2]}")

    nome_eleitor = input("Digite o nome do eleitor que gostaria de editar: ").strip()

    cursor.execute(
        """
        SELECT Nome_Completo, CPF, Titulo_de_eleitor
        FROM Eleitores
        WHERE Nome_Completo = %s
        """,
        (nome_eleitor,)
    )
    eleitor = cursor.fetchone()

    if eleitor is None:
        print("Eleitor nao encontrado!")
        fechar_bd(conexao, cursor)
        return

    nome_atual, cpf_atual, titulo_atual = eleitor

    novo_nome = input(
        "Digite o novo nome do eleitor (enter para manter o atual): "
    ).strip()
    novo_cpf = input(
        "Digite o novo CPF do eleitor (enter para manter o atual): "
    ).strip()
    novo_titulo = input(
        "Digite o novo titulo do eleitor (enter para manter o atual): "
    ).strip()

    if novo_nome == "":
        novo_nome = nome_atual
    if novo_cpf == "":
        novo_cpf = cpf_atual
    else:
        novo_cpf = criptografia.criptografar(novo_cpf)
    if novo_titulo == "":
        novo_titulo = titulo_atual

    cursor.execute(
        """
        UPDATE Eleitores
        SET Nome_Completo = %s,
            CPF = %s,
            Titulo_de_eleitor = %s
        WHERE Nome_Completo = %s
        """,
        (novo_nome, novo_cpf, novo_titulo, nome_eleitor)
    )
    conexao.commit()
    print("Eleitor atualizado com sucesso!")

    fechar_bd(conexao, cursor)
