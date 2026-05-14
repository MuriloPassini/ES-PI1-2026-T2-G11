#from banco import conectar_bd
#Função responsável por abrir a votação
def abrir_votacao():
    #Faz a conexão com o banco e cria o cursor para execultar o sql
    conexao, cursor = conectar_bd()
    print('='*10, 'ABERTURA DA VOTAÇÃO', '='*10)
    #Dados do mesário para autenticação
    titulo = input('Digite o seu título de eleitor: ')
    cpf = input('Digite os 4 primeiros dígitos do seu CPF: ')
    while len(cpf) != 4:
        print ('errado')
        cpf = input('Digite os 4 primeiros dígitos do seu CPF: ')
    print('certo')
    chave = input('Digite a chave de acesso: ')
    #Comando SQL para verificar se o usuário existe
    sql = """
    SELECT Mesario
    FROM Eleitores
    WHERE Titulo_de_eleitor = %s
    AND SUBSTRING(CPF, 1, 4) = %s
    AND Chave_de_acesso = %s
    """
    #Executa o SQL no banco usando os dados digitados
    cursor.execute(sql, (titulo, cpf, chave))
    #Pega o resultado encontrado no banco
    resultado = cursor.fetchone()
    #Se não encontrar nenhum usuário com esses dados
    if resultado is None:
        print('ERRO: Validação falha.')
        #Fecha cursor e conexão
        cursor.close()
        conexao.close()
        return
    #Verifica se o usuário é um mesário
    if resultado[0] != 'S':
        print('ERRO: Usuário não está cadastrado como mesário.')
        #Fecha cursor e conexão
        cursor.close()
        conexao.close()
        return
    #Caso tudo esteja correto
    print('\nMesário autenticado com sucesso!')
    #Zerésima
    print('\nRealizando Zerésima...')
    #Remove todos os votos registrados
    cursor.execute("DELETE FROM votos")
    conexao.commit()
    print('\n=== ZERÉSIMA ===')
    #Busca todos os candidatos cadastrados
    cursor.execute("""
    SELECT nome, numero
    FROM candidatos
    """)
    #fetchall pega todos os resultados encontrados
    candidatos = cursor.fetchall()
    for candidato in candidatos:
        print(f'Candidato: {candidato[0]} | Número: {candidato[1]}')
    print('\nSistema liberado para votação!')
    print('\n1 - Votar')
    print('2 - Encerrar sistema')   
    #fecha o cursor e a conexão
    cursor.close()
    conexao.close()