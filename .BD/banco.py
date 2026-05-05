import mysql.connector


def conectar_bd():
    connect = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha",
        database="seu_banco"
    )
    return connect
