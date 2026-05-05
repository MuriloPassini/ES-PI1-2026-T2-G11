import mysql.connector


def conectar_bd():
    connect = mysql.connector.connect(
        host="BD-ACD",
        user="BD250226129",
        password="Gcpop08",
        database="Candidato"
    )
    return connect
