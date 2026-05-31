from banco import conectar_bd, fechar_bd
import criptografia
from LOGS_VOTAÇÃO import registrar_encerramento, registrar_acesso_negado

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

    cursor.execute(
        """
        SELECT CPF, Chave_de_acesso, Mesario, Nome_Completo
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
        """,
        (titulo,)
    )

    # Pega o resultado
    resultado = cursor.fetchone()

    # Se não encontrar usuário
    if resultado is None:
        print('\nERRO!!! Validação falhou.')
        fechar_bd(conexao, cursor)
        return False

    cpf_banco = criptografia.descriptografar(resultado[0])
    chave_banco = criptografia.descriptografar(resultado[1])
    mesario_banco = resultado[2]
    nome_mesario = resultado[3]

    if cpf_banco[:4] != cpf or chave_banco != chave:
        print('\nERRO!!! Validação falhou.')
        fechar_bd(conexao, cursor)
        return False

    # Verifica se é mesário
    if mesario_banco != 'S':
        print('\nERRO!!! Usuário não está cadastrado como mesário.')
        fechar_bd(conexao, cursor)
        return False
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
