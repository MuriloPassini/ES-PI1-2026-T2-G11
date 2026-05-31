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
        host=os.getenv("VOTE_DB_HOST", "localhost"),
        user=os.getenv("VOTE_DB_USER", "root"),
        password=os.getenv("VOTE_DB_PASSWORD", "198765432AbGF"),
        database=os.getenv("VOTE_DB_NAME", "testes")
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
