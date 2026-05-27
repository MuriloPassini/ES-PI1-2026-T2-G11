from datetime import datetime
import random

from banco import conectar_bd, fechar_bd
import criptografia


def gerar_protocolo(numero_candidato):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letra1 = random.choice(letras)
    letra2 = random.choice(letras)
    numero_candidato = str(numero_candidato).zfill(2)
    digitos = '1234567890'
    digito1 = ''
    for i in range(5):
        digito1 += random.choice(digitos)
    return "V" + letra1 + letra2 + "26" + numero_candidato + digito1




def votacao():
    conexao, cursor = conectar_bd()

    cursor.execute("SELECT aberta FROM status_votacao WHERE id = 1")
    status = cursor.fetchone()

    if status is None or not status[0]:
        print("ERRO! O sistema de votacao nao esta aberto.")
        fechar_bd(conexao, cursor)
        return

    titulo_eleitor = input("Digite o titulo de eleitor: ").strip()
    cpf_inicio = input("Digite os 4 primeiros digitos do CPF: ").strip()
    chave_de_acesso = input("Digite sua chave de acesso: ").strip()

    if not titulo_eleitor or not cpf_inicio or not chave_de_acesso:
        print("Todos os campos sao obrigatorios.")
        fechar_bd(conexao, cursor)
        return

    cursor.execute(
        """
        SELECT Nome_Completo, CPF, Chave_de_acesso, Ja_votou
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
        """,
        (titulo_eleitor,)
    )
    eleitor = cursor.fetchone()

    if eleitor is None:
        print("Dados invalidos!")
        fechar_bd(conexao, cursor)
        return

    cpf_banco = criptografia.descriptografar(eleitor[1])
    chave_banco = criptografia.descriptografar(eleitor[2])

    if cpf_banco[:4] != cpf_inicio or chave_banco != chave_de_acesso:
        print("Dados invalidos!")
        fechar_bd(conexao, cursor)
        return

    if eleitor[3]:
        print("Esse eleitor ja realizou a votacao!")
        fechar_bd(conexao, cursor)
        return

    numero_candidato = None
    while numero_candidato is None:
        entrada = input("Digite o numero do seu candidato: ").strip()
        if not entrada.isdigit():
            print("Numero invalido.")
            continue

        cursor.execute(
            """
            SELECT nome, numero, partido
            FROM candidatos
            WHERE numero = %s
            """,
            (entrada,)
        )
        candidato = cursor.fetchone()

        if candidato is None:
            print("Candidato nao encontrado.")
            continue

        print("Candidato:")
        print("Nome:", candidato[0])
        print("Numero:", candidato[1])
        print("Partido:", candidato[2])

        confirmar = input("Deseja confirmar seu voto (S/N): ").strip().upper()
        if confirmar == "S":
            numero_candidato = candidato[1]
    protocolo=gerar_protocolo(numero_candidato)
    protocolo_criptografado = criptografia.criptografar(protocolo)
    data_hora = datetime.now()

    cursor.execute("INSERT INTO votos (protocolo, titulo_eleitor, numero_candidato, data_hora) VALUES (%s, %s, %s, %s)", (protocolo, titulo_eleitor, numero_candidato, data_hora))
    cursor.execute("UPDATE eleitores SET ja_votou = TRUE WHERE titulo_eleitor = %s", (titulo_eleitor,))
    conexao.commit()

    print("")
    print("Voto confirmado com sucesso!")
    print("Seu numero de protocolo e:", protocolo)
    print("Data e hora do voto:", data_hora.strftime("%d/%m/%Y %H:%M:%S"))
    print("")

    fechar_bd(conexao, cursor)

