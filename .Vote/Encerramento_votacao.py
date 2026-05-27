from banco import conectar_bd, fechar_bd

def fechar_votacao():

    # Faz a conexão com o banco e cria o cursor

    conexao, cursor = conectar_bd()
    print('=' * 10, 'ENCERRAMENTO VOTAÇÃO', '=' * 10)

    # Dados do mesário para autenticação

    titulo = input('Digite o seu título de eleitor: ').strip()
    cpf = input('Digite os 4 primeiros dígitos do seu CPF: ').strip()
    while not (cpf.isdigit() and len(cpf) == 4):
        print('ERRO!!! Digite apenas os 4 primeiros números do CPF.')
        cpf = input('Digite os 4 primeiros dígitos do seu CPF: ').strip()

    chave = input('Digite a chave de acesso: ').strip()

    # SQL para verificar o mesário

    sql = """
    SELECT Mesario, Nome_Completo
    FROM Eleitores
    WHERE Titulo_de_eleitor = %s
    AND SUBSTRING(CPF, 1, 4) = %s
    AND Chave_de_acesso = %s
    """

    # Executa o SQL
    cursor.execute(sql, (titulo, cpf, chave))

    # Pega o resultado
    resultado = cursor.fetchone()

    # Se não encontrar usuário
    if resultado is None:
        print('\nERRO!!! Validação falhou.')
        fechar_bd(conexao, cursor)
        return

    # Verifica se é mesário
    if resultado[0] != 'S':
        print('\nERRO!!! Usuário não está cadastrado como mesário.')
        fechar_bd(conexao, cursor)
        return

    nome_mesario = resultado[1]
    print(f"\nMesario {nome_mesario} autenticado com sucesso!")

    #verificação de encerramento
    confirmar_encerramento = input("Deseja realmente encerrar a votação (S/N): ").strip().upper()
    if confirmar_encerramento == "N":
        print("Cancelando o encerramento de votação")
        print("RETORNANDO A ULTIMA TELA...")
        fechar_bd(conexao, cursor)
        return False
    else:
        segunda_chave = input('Por favor insira novamente a sua chave de acesso: ').strip()
        while segunda_chave != chave:
            print("ERRO!!! Chave incorreta.")
            segunda_chave = input("Tente novamente: ").strip()
        #fechar a urna
        cursor.execute("UPDATE status_votacao SET aberta = FALSE WHERE id = 1")
        conexao.commit()

        print(f"\nVotacao encerrada com sucesso!")
        print(f"Mesario responsavel: {nome_mesario}")

        fechar_bd(conexao, cursor)
        return True

if __name__ == "__main__":
    fechar_votacao()