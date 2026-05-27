from banco import conectar_bd, fechar_bd

def boletim_urna():
    #exibe os votos por candidato em ordem alfabetica e declara quem venceu

    conexao, cursor = conectar_bd()
 
    print("\n" + "=" * 10, "BOLETIM DE URNA", "=" * 10)
 
    #lista candidatos em ordem alfabetica com total de votos

    cursor.execute(
        """
        SELECT c.nome, c.numero, c.partido, COUNT(v.numero_candidato) AS total_votos
        FROM candidatos c
        LEFT JOIN votos v ON c.numero = v.numero_candidato
        GROUP BY c.nome, c.numero, c.partido
        ORDER BY c.nome ASC
        """
    )
    candidatos = cursor.fetchall()
 
    if not candidatos:
        print("Nenhum candidato cadastrado.")
        fechar_bd(conexao, cursor)
        return
    
    for candidato in candidatos:
        print(f"Nome: {candidato[0]} | Numero: {candidato[1]} | Partido: {candidato[2]} | Votos: {candidato[3]}")
 
    #declara o candidato com mais votos
    vencedor = max(candidatos, key=lambda c: c[3])
    print("\n" + "=" * 10, "VENCEDOR", "=" * 10)
    print(f"Nome   : {vencedor[0]}")
    print(f"Numero : {vencedor[1]}")
    print(f"Partido: {vencedor[2]}")
    print(f"Votos  : {vencedor[3]}")
 
    fechar_bd(conexao, cursor)

def estatistica_comparecimento():
    #mostra quantos eleitores votaram

    conexao, cursor = conectar_bd()
 
    print("\n" + "=" * 10, "ESTATISTICA DE COMPARECIMENTO", "=" * 10)
 
    #Total de eleitores e quantos votaram
    cursor.execute("SELECT COUNT(*) FROM Eleitores")
    total_eleitores = cursor.fetchone()[0]
 
    cursor.execute("SELECT COUNT(*) FROM Eleitores WHERE Ja_votou = TRUE")
    total_votaram = cursor.fetchone()[0]
 
    if total_eleitores == 0:
        print("Nenhum eleitor cadastrado.")
        fechar_bd(conexao, cursor)
        return
    
    percentual = (total_votaram / total_eleitores) * 100
 
    print(f"Total de eleitores aptos : {total_eleitores}")
    print(f"Total que compareceram   : {total_votaram}")
    print(f"Percentual de participacao: {percentual:.2f}%")
 
    fechar_bd(conexao, cursor)

def votos_por_partido():
    #exibe a soma de votos recebidos por partido

    conexao, cursor = conectar_bd()
        
    print("\n" + "=" * 10, "VOTOS POR PARTIDO", "=" * 10)
 
    #agrupa votos por partido
    cursor.execute(
        """
        SELECT c.partido, COUNT(v.numero_candidato) AS total_votos
        FROM candidatos c
        LEFT JOIN votos v ON c.numero = v.numero_candidato
        GROUP BY c.partido
        ORDER BY total_votos DESC
        """
    )
    partidos = cursor.fetchall()
 
    if not partidos:
        print("Nenhum dado encontrado.")
        fechar_bd(conexao, cursor)
        return
 
    for partido in partidos:
        print(f"Partido: {partido[0]} | Votos: {partido[1]}")
 
    fechar_bd(conexao, cursor)

def validacao_integridade():
    #compara a quantidade de votos cadastrados na urna pela quantidade de pessoas listadas com "ja_votou"
    
    conexao, cursor = conectar_bd()
 
    print("\n" + "=" * 10, "VALIDACAO DE INTEGRIDADE", "=" * 10)
 
    #compara votos registrados com eleitores marcados como Ja Votou

    cursor.execute("SELECT COUNT(*) FROM votos")
    total_votos = cursor.fetchone()[0]
 
    cursor.execute("SELECT COUNT(*) FROM Eleitores WHERE Ja_votou = TRUE")
    total_ja_votou = cursor.fetchone()[0]
 
    print(f"Total de votos na urna       : {total_votos}")
    print(f"Total de eleitores Ja Votou  : {total_ja_votou}")
 
    if total_votos == total_ja_votou:
        print("\nRELATORIO: Eleicao INTEGRA. Nenhuma inconsistencia encontrada.")
    else:
        print("\nALERTA: Inconsistencia detectada! Os numeros nao coincidem.")
 
    fechar_bd(conexao, cursor)

def menu_resultados():
    #exibe o menu de resultados da votacao e direciona para cada opcao disponivel.

    executando_menu = True
    while executando_menu:
        print("\n" + "=" * 10, "RESULTADOS DA VOTACAO", "=" * 10)
        print("1. Boletim de Urna")
        print("2. Estatistica de Comparecimento")
        print("3. Votos por Partido")
        print("4. Validacao de Integridade")
        print("0. Voltar")
    
        opcao = input("Escolha uma opcao: ").strip()
    
        match opcao:
            case "1":
                boletim_urna()
            case "2":
                estatistica_comparecimento()
            case "3":
                votos_por_partido()
            case "4":
                validacao_integridade()
            case "0":
                print("Voltando...")
                executando_menu = False
            case _:
                print("Opcao invalida!")
    
    
if __name__ == "__main__":
    menu_resultados()