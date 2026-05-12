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
    # edições
    cursor.execute(
        '''
        SELECT nome, cpf, titulo FROM Eleitores WHERE nome = %s
        ''',
        (nome_eleitor,)
    )

    eleitor = cursor.fetchone()

    if eleitor is None:
        print('ELeitor não encontrado!')
        return

    nome_atual = eleitor[0]
    cpf_atual = eleitor[1]
    titulo_atual = eleitor[2]

    nome_eleitor = input('Digite o eleitor o qual gostaria de editar:  ')

    novo_nome = input(
        'Digite o novo nome do eleitor\n\t(caso queira  manter o atual, apenas pressione enter):')
    novo_cpf = input(
        'Digite o novo CPF do eleitor\n\t(caso queira  manter o atual, apenas pressione enter): ')
    novo_titulo = input(
        'Digite o novo título do eleitor\n\t(caso queira  manter o atual, apenas pressione enter):')

    if novo_nome == '':
        novo_nome = nome_atual

    if novo_cpf == '':
        novo_cpf = cpf_atual
    else:
        novo_cpf = int(novo_cpf)

    if novo_titulo == '':
        novo_titulo = titulo_atual
    else:
        novo_titulo = int(novo_titulo)

    cursor.execute(
        '''
        UPDATE Eleitores
        SET nome = %s,
        titulo  = %s
        cpf = %s
        WHERE nome = %s
        ''',
        (novo_nome, novo_titulo, novo_cpf, nome_eleitor)
    )

    conexao.commit()
    print('Eleitor atualizado com sucesso!')

    cursor.close()
    conexao.close()
