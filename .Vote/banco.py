import mysql.connector
import os


def conectar_bd():
    """
    Abre a conexao com o banco de dados usado pelo sistema.

    Args:
        Nenhum.

    Returns:
        tuple: Conexao ativa com o MySQL e cursor para executar comandos SQL.
    """
    conexao = mysql.connector.connect(
        host=os.getenv("VOTE_DB_HOST", "BD-ACD"),
        user=os.getenv("VOTE_DB_USER", "BD120226828"),
        password=os.getenv("VOTE_DB_PASSWORD", "Iwgyx6"),
        database=os.getenv("VOTE_DB_NAME", "BD120226828")
    )
    cursor = conexao.cursor()
    return conexao, cursor


def fechar_bd(conexao, cursor):
    """
    Fecha o cursor e a conexao aberta com o banco de dados.

    Args:
        conexao (mysql.connector.connection.MySQLConnection): Conexao ativa com o MySQL.
        cursor (mysql.connector.cursor.MySQLCursor): Cursor usado nas consultas SQL.

    Returns:
        None: A funcao apenas encerra os recursos recebidos.
    """
    cursor.close()
    conexao.close()
