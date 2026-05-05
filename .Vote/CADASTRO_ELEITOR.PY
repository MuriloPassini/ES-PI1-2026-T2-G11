import mysql.connector
from banco import conectar_bd
from validacoes import validacaotitulo, validacaocpf
from chave_acesso import chave_acesso


def cadastrar_eleitor():
    connect = conectar_bd()
    cursor = connect.cursor()
    nome = str(input('Insira o nome do eleitor: '))
    titulo = str(input('Insira o título de eleitor do mesmo: '))
    cpf = str(input('Insira o CPF do eleitor: '))
    mesario = str(input('O eleitor é mesário? S/N: ')).upper()
    titulo_valido = validacaotitulo(titulo)
    cpf_valido = validacaocpf(cpf)
    chave = chave_acesso(nome)

    if titulo_valido and cpf_valido:
        print('='*35)
        print(f'Eleitor cadastrado com sucesso!')
        print('Resumo do eleitor:')
        print(f'Nome: {nome}')
        print(f'Título de eleitor: {titulo}')
        print(f'CPF: {cpf}')
        print(f'É mesário?: {mesario}')
        print(f'Chave de acesso: {chave}')
        print(f'GUARDE SUA CHAVE DE ACESSO!')
        print('='*35)
        cursor.execute(
            'INSERT INTO Eleitores (Nome Completo, CPF, Titulo de eleitor, Chave de acesso, Mesario) VALUES (%s, %s, %s, %s, %s)',
            (nome, cpf, titulo, chave, mesario)
        )
        connect.commit()
    else:
        print('Dados inválidos! Verifique o CPF e o título de eleitor.')
