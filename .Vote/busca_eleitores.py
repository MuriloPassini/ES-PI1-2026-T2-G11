# manutenção feita por cauã

from banco import conectar_bd
from busca_eleitores import iniciar_votacao

def iniciar_login():
    print('='*9,'L O G I N','='*9)
    # Validação do eleitor, conferência do título de eleitor, CPF e chave de acesso, além da verificação se o eleitor é mesário ou não.
    connection = conectar_bd()
    cursor = connection.cursor()
    titulo_eleitor = int(input('Digite o seu título de eleitor: '))
    cpf = int(input('Digite os quatro primeiros dígitos do seu CPF: '))
    chave = int(input('Digite a sua chave de acesso: '))
    mesario = str(input('É mesário? (S/N): ')).upper()
# Consulta SQL para validar o eleitor.
    sql = """
    SELECT mesario 
    FROM eleitores
    WHERE titulo_eleitor = %s 
    AND SUBSTRING(cpf, 1, 4) = %s 
    AND chave_acesso = %s
    """
# Execução da consulta SQL com os dados fornecidos pelo usuário.
    cursor.execute(sql, (titulo_eleitor, cpf, chave))
    resultado = cursor.fetchone()
# Verificação do resultado da consulta para determinar se o eleitor é válido e se é mesário ou não, exibindo as mensagens apropriadas.
    if resultado is None:
        print('Dados inválidos. Acesso negado.')
    elif mesario == 'S':
        if resultado[0] == '1':
            print('Bem-vindo, mesário! Você pode acessar as funções de mesário.')
        else:
            print('Acesso negado. Você não é um mesário registrado.')
    else:
        print('Usuário validado com sucesso! Você pode votar normalmente.')
        iniciar_votacao()
    cursor.close()
    connection.close()

    

