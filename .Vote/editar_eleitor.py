import mysql.connector
from banco import conectar_bd


def editar_eleitor():
    conexao, cursor = conectar_bd()

    mostrar_eleitores = input(
        'Mostrar todos os eleitores? S/N: ').strip().upper()
    if mostrar_eleitores == 'S':
        cursor.execute('SELECT * FROM eleitores;')
        eleitores = cursor.fetchall()
        for e in eleitores:
            print(f'Nome: {e[0]} | CPF: {e[1]} | Título: {e[2]}')
    # edições
    nome_eleitor = input('Digite o eleitor o qual gostaria de editar:  ')

    cursor.execute(
        '''
        SELECT nome, cpf, titulo FROM eleitores WHERE nome = %s
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
        UPDATE eleitores
        SET nome = %s,
        cpf  = %s,
        titulo = %s
        WHERE nome = %s
        ''',
        (novo_nome, novo_cpf, novo_titulo, nome_eleitor)
    )

    conexao.commit()
    print('Eleitor atualizado com sucesso!')

    cursor.close()
    conexao.close()
