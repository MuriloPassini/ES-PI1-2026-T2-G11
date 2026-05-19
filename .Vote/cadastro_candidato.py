import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="198765432AbGF",
    database="testes"
)

cursor = conexao.cursor()

#=============================== funções =====================================================
def listar():
        cursor.execute("select * from candidatos")
        resultados=cursor.fetchall()
        print(f'{'Lista de Candidatos':^57}')
        for i in resultados:
                print(f" Nome: {i[0]}  Número: {i[1]}  Partido: {i[2]}")
def cadastrar():
        nome_candidato = input("Digite o seu nome de candidato: ").strip()
        while not nome_candidato.replace(' ','').isalpha():
                print("Nome inválido! Digite apenas letras.")
                nome_candidato = input("Digite o seu nome de candidato: ")

        numcandidato = input("Digite o seu numero de candidato: ").strip()
        while not (numcandidato.isdigit() and len(numcandidato) == 2):
                print("Número de candidato inválido! digite novamente ")
                numcandidato = input("Digite o seu número de candidato: ")
        
        partidocandidato = input("Digite qual o seu partido: ").strip()
        while not partidocandidato.replace(' ','').isalpha():
                print("Partido inválido! Digite apenas letras.")
                partidocandidato = input("Digite qual o seu partido: ")

        sql = """
        INSERT INTO candidatos (nome, numero, partido)
        VALUES (%s, %s, %s)
        """

        valores = (nome_candidato, int(numcandidato), partidocandidato)

        try:
                cursor.execute(sql, valores)
                conexao.commit()
                print("Candidato cadastrado com sucesso!")
        except mysql.connector.Error as erro:
                if erro.errno == 1062:
                        print("Erro: número de candidato já existe!")
                else:
                        print("Erro:", erro)

def buscar():
        print('Escolha uma opção para buscar o(s) candidato(s): ')
        print('1. Nome')
        print('2. Número')
        print('3. Partido')
        opcao=int(input('Digite sua opção: '))
        if opcao==1:
                nome_buscar=input("Digite o nome do candidato: ")
                sql = "SELECT nome, numero, partido FROM candidatos WHERE nome = %s"
                cursor.execute(sql, (nome_buscar,))
                resultado = cursor.fetchall()
                if resultado:
                        print("="*30)
                        print(f"Nome     : {resultado[0]}")
                        print(f"Número   : {resultado[1]}")
                        print(f"Partido  : {resultado[2]}")
                        print("="*30)
                else:
                        print("Candidato não encontrado.")
        elif opcao==2:
                numero_busca=input('Digite o número do candidato: ')
                sql="select nome, numero, partido from candidatos where numero=%s"
                cursor.execute(sql,(numero_busca,))
                resultado=cursor.fetchall()
                if resultado:
                        print("="*30)
                        print(f"Nome     : {resultado[0]}")
                        print(f"Número   : {resultado[1]}")
                        print(f"Partido  : {resultado[2]}")
                        print("="*30)
                else:
                        print("Candidato não encontrado.")

        elif opcao==3:
                partido_buscar=input('Digite o partido do candidatos que deseja buscar: ')
                sql="select nome, numero, partido from candidatos where partido=%s"
                cursor.execute(sql,(partido_buscar,))
                resultado=cursor.fetchall()
                if resultado:
                        print("="*30)
                        print(f"Nome     : {resultado[0]}")
                        print(f"Número   : {resultado[1]}")
                        print(f"Partido  : {resultado[2]}")
                        print("="*30)
                else:
                        print("Candidato não encontrado.")
        else:
                print('Opção inválida!')

def deletarcandi():
        numero_busca=input("Digite o número do candidato que deseja excluir: ")
        sql="select nome,numero partido where numero=%s"
        cursor.execute(sql,(numero_busca,))
        resultado=cursor.fetchone()
        if resultado:
                print('\nCandidato encontrado!')
                print('='*30)
                print(f'Nome: {resultado[0]}')
                print(f'Número: {resultado[1]}')
                print(f'Partido: {resultado[2]}')
                print('='*30)
                confirmar=input('Deseja confirmar? (s/n):').strip().lower()
                if confirmar=='s':
                        sql_deletar='delete from candidatos where numero=%s'
                        cursor.execute(sql_deletar,(numero_busca,))
                        conexao.commit()
                        print('\nCandidato deletado com sucesso!')
                else:
                        print('Operação cancelada!')
        else:
                print('Candidato não encontrado')
#======================Menuzão=================================================
executando=True
while executando:
                print("\n" + "="*30)
                print("   SISTEMA DE CANDIDATOS")
                print("="*30)
                print("1 - Cadastrar")
                print("2 - Listar")
                print("3 - Buscar")
                print("4 - Deletar")
                print("5 - Sair")
                opcao = input("Escolha: ")

                if opcao == "1":
                        cadastrar()
                elif opcao == "2":
                        listar()
                elif opcao == "3":
                        buscar()
                elif opcao == "4":
                        deletarcandi()
                elif opcao == "5":
                        print("Saindo...")
                        executando = False
                else:
                        print("Opção inválida!")
                              
cursor.close()
conexao.close()