from banco import conectar_bd, fechar_bd


def abrir_votacao():
    conexao, cursor = conectar_bd()

    print("=" * 10, "ABERTURA DA VOTACAO", "=" * 10)

    titulo = input("Digite o seu titulo de eleitor: ").strip()
    cpf = input("Digite os 4 primeiros digitos do seu CPF: ").strip()
    while not (cpf.isdigit() and len(cpf) == 4):
        print("ERRO! Digite apenas os 4 primeiros numeros do CPF.")
        cpf = input("Digite os 4 primeiros digitos do seu CPF: ").strip()

    chave = input("Digite a chave de acesso: ").strip()

    cursor.execute(
        """
        SELECT Mesario
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
          AND SUBSTRING(CPF, 1, 4) = %s
          AND Chave_de_acesso = %s
        """,
        (titulo, cpf, chave)
    )
    resultado = cursor.fetchone()

    if resultado is None:
        print("\nERRO! Validacao falhou.")
        fechar_bd(conexao, cursor)
        return False

    if resultado[0] != "S":
        print("\nERRO! Usuario nao esta cadastrado como mesario.")
        fechar_bd(conexao, cursor)
        return False

    print("\nMesario autenticado com sucesso!")
    print("\nRealizando Zeresima...")

    cursor.execute("DELETE FROM votos")
    cursor.execute("UPDATE Eleitores SET Ja_votou = FALSE")
    conexao.commit()

    cursor.execute("SELECT nome, numero FROM candidatos")
    candidatos = cursor.fetchall()

    if candidatos:
        for candidato in candidatos:
            print(f"Candidato: {candidato[0]} | Numero: {candidato[1]}")
    else:
        print("Nenhum candidato cadastrado.")

    print("\nSistema liberado para votacao!")
    fechar_bd(conexao, cursor)
    return True


if __name__ == "__main__":
    abrir_votacao()
