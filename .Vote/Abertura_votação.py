from banco import conectar_bd, fechar_bd
import criptografia
from LOGS_VOTAÇÃO import registrar_abertura, registrar_acesso_negado 

def abrir_votacao():
    """
    Autentica um mesario, zera os votos anteriores e libera a votacao.

    Args:
        Nenhum.

    Returns:
        bool: True quando a votacao e aberta; False quando a validacao falha.
    """
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
        SELECT CPF, Chave_de_acesso, Mesario
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
        """,
        (titulo,)
    )
    resultado = cursor.fetchone()

    if resultado is None:
        print("\nERRO! Validacao falhou.")
        registrar_acesso_negado()
        fechar_bd(conexao, cursor)
        return False

    cpf_banco = criptografia.descriptografar(resultado[0])
    chave_banco = criptografia.descriptografar(resultado[1])
    mesario_banco = resultado[2]

    if cpf_banco[:4] != cpf or chave_banco != chave:
        print("\nERRO! Validacao falhou.")
        registrar_acesso_negado()
        fechar_bd(conexao, cursor)
        return False

    if mesario_banco != "S":
        print("\nERRO! Usuario nao esta cadastrado como mesario.")
        registrar_acesso_negado()
        fechar_bd(conexao, cursor)
        return False

    print("\nMesario autenticado com sucesso!")
    print("\nRealizando Zeresima...")

    cursor.execute("DELETE FROM votos")
    cursor.execute("UPDATE Eleitores SET Ja_votou = FALSE")
    conexao.commit()
    registrar_abertura()

    cursor.execute("SELECT nome, numero FROM candidatos")
    candidatos = cursor.fetchall()

    if candidatos:
        for candidato in candidatos:
            print(f"Candidato: {candidato[0]} | Numero: {candidato[1]}")
    else:
        print("Nenhum candidato cadastrado.")

    print("\nSistema liberado para votacao!")

    #abrir votação no banco
    cursor.execute("UPDATE status_votacao SET aberta = TRUE WHERE id = 1")
    conexao.commit()

    fechar_bd(conexao, cursor)
    return True
