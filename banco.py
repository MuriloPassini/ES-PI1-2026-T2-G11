import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="BD-ACD",
        user="xxxxxxxxxx",
        password="xxxxxxx",
        database="xxxxxxxxxx"
    )
