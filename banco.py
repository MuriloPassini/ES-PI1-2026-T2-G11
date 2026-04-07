import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="BD-ACD",
        user="BD250226129",
        password="Gcpop8",
        database="BD250226129"
    )