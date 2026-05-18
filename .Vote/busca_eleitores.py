from banco import conectar_bd, fechar_bd


def iniciar_login():
    print("=" * 9, "L O G I N", "=" * 9)

    conexao, cursor = conectar_bd()

    titulo_eleitor = input("Digite o seu titulo de eleitor: ").strip()
    cpf = input("Digite os quatro primeiros digitos do seu CPF: ").strip()
    chave = input("Digite a sua chave de acesso: ").strip()
    mesario = input("E mesario? (S/N): ").strip().upper()

    cursor.execute(
        """
        SELECT Mesario
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
          AND SUBSTRING(CPF, 1, 4) = %s
          AND Chave_de_acesso = %s
        """,
        (titulo_eleitor, cpf, chave)
    )
    resultado = cursor.fetchone()

    if resultado is None:
        print("Dados invalidos. Acesso negado.")
    elif mesario == "S":
        if resultado[0] == "S":
            print("Bem-vindo, mesario! Voce pode acessar as funcoes de mesario.")
        else:
            print("Acesso negado. Voce nao e um mesario registrado.")
    else:
        print("Usuario validado com sucesso! Voce pode votar normalmente.")

    fechar_bd(conexao, cursor)


if __name__ == "__main__":
    iniciar_login()
