import mysql.connector


def conectar_bd():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="198765432AbGF",
        database="testes"
    )

    cursor = conexao.cursor()
    return conexao, cursor
