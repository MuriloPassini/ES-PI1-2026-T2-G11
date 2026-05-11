import mysql.connector
from banco import conectar_bd


def editar_eleitor():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    mostrar_eleitores = input(
        'Mostrar todos os eleitores? S/N: ').strip().upper()
    if mostrar_eleitores == 'S':
        cursor.execute('SELECT * FROM Eleitores;')
        eleitores = cursor.fetchall()
        for e in eleitores:
            print(f'Nome: {e[0]} | CPF: {e[1]} | Título: {e[2]}')
