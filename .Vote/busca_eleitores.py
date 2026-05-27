from banco import conectar_bd, fechar_bd
import criptografia


def iniciar_login():
    print("=" * 9, "L O G I N", "=" * 9)

    conexao, cursor = conectar_bd()

    titulo_eleitor = input("Digite o seu titulo de eleitor: ").strip()
    cpf = input("Digite os quatro primeiros digitos do seu CPF: ").strip()
    chave = input("Digite a sua chave de acesso: ").strip()
    mesario = input("E mesario? (S/N): ").strip().upper()

    cursor.execute(
        """
        SELECT CPF, Chave_de_acesso, Mesario
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
        """,
        (titulo_eleitor,)
    )
    resultado = cursor.fetchone()

    if resultado is not None:
        cpf_banco = criptografia.descriptografar(resultado[0])
        chave_banco = criptografia.descriptografar(resultado[1])

        if cpf_banco[:4] != cpf or chave_banco != chave:
            resultado = None

    if resultado is None:
        print("Dados invalidos. Acesso negado.")
    elif mesario == "S":
        if resultado[2] == "S":
            print("Bem-vindo, mesario! Voce pode acessar as funcoes de mesario.")
        else:
            print("Acesso negado. Voce nao e um mesario registrado.")
    else:
        print("Usuario validado com sucesso! Voce pode votar normalmente.")

    fechar_bd(conexao, cursor)


if __name__ == "__main__":
    iniciar_login()
