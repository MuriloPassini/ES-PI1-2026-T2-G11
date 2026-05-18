# Função para abrir a votação
def abrir_votacao():
    # Faz a conexão com o banco e cria o cursor
    conexao, cursor = conectar_bd()
    print('=' * 10, 'ABERTURA DA VOTAÇÃO', '=' * 10)
    # Dados do mesário para autenticação
    titulo = input('Digite o seu título de eleitor: ')
    cpf = input('Digite os 4 primeiros dígitos do seu CPF: ')
    while len(cpf) != 4:
        print('ERRO!!! Digite apenas os 4 primeiros números do CPF.')
        cpf = input('Digite os 4 primeiros dígitos do seu CPF: ')

    chave = input('Digite a chave de acesso: ')

    # SQL para verificar o mesário
    sql = """
    SELECT Mesario
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

        cursor.close()
        conexao.close()
        return

    # Verifica se é mesário
    if resultado[0] != 'S':
        print('\nERRO!!! Usuário não está cadastrado como mesário.')

        cursor.close()
        conexao.close()
        return

    # Autenticação concluída
    print('\nMesário autenticado com sucesso!')

    # Zerésima
    print('\nRealizando Zerésima...')

    # Remove todos os votos
    cursor.execute("DELETE FROM votos")

    # Salva alteração no banco
    conexao.commit()
    # Busca candidatos
    cursor.execute("""
    SELECT nome, numero
    FROM candidatos
    """)
    candidatos = cursor.fetchall()
    # Exibe candidatos
    for candidato in candidatos:
        print(f'Candidato: {candidato[0]} | Número: {candidato[1]}')

    print('\nSistema liberado para votação!')
    print('\n1 - Votar')
    print('2 - Encerrar sistema')
    # Fecha conexão
    cursor.close()
    conexao.close()

# TESTE DA FUNÇÃO
abrir_votacao()






#Código para conectar ao MySQL
import mysql.connector

def conectar_bd():

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='sistema_votacao'
    )

    cursor = conexao.cursor()

    return conexao, cursor
