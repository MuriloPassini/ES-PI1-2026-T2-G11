import mysql.connector
import os


def conectar_bd():
    conexao = mysql.connector.connect(
        host=os.getenv("VOTE_DB_HOST", "localhost"),
        user=os.getenv("VOTE_DB_USER", "root"),
        password=os.getenv("VOTE_DB_PASSWORD", "198765432AbGF"),
        database=os.getenv("VOTE_DB_NAME", "testes")
    )
    cursor = conexao.cursor()
    return conexao, cursor


def fechar_bd(conexao, cursor):
    cursor.close()
    conexao.close()
