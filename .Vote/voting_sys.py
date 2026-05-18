from datetime import datetime
import uuid

from banco import conectar_bd, fechar_bd


def votacao():
    conexao, cursor = conectar_bd()

    titulo_eleitor = input("Digite o titulo de eleitor: ").strip()
    cpf_inicio = input("Digite os 4 primeiros digitos do CPF: ").strip()
    chave_de_acesso = input("Digite sua chave de acesso: ").strip()

    if not titulo_eleitor or not cpf_inicio or not chave_de_acesso:
        print("Todos os campos sao obrigatorios.")
        fechar_bd(conexao, cursor)
        return

    cursor.execute(
        """
        SELECT Nome_Completo, Ja_votou
        FROM Eleitores
        WHERE Titulo_de_eleitor = %s
          AND SUBSTRING(CPF, 1, 4) = %s
          AND Chave_de_acesso = %s
        """,
        (titulo_eleitor, cpf_inicio, chave_de_acesso)
    )
    eleitor = cursor.fetchone()

    if eleitor is None:
        print("Dados invalidos!")
        fechar_bd(conexao, cursor)
        return

    if eleitor[1]:
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

    protocolo = str(uuid.uuid4())
    data_hora = datetime.now()

    cursor.execute(
        """
        INSERT INTO votos (protocolo, titulo_eleitor, numero_candidato, data_hora)
        VALUES (%s, %s, %s, %s)
        """,
        (protocolo, titulo_eleitor, numero_candidato, data_hora)
    )
    cursor.execute(
        "UPDATE Eleitores SET Ja_votou = TRUE WHERE Titulo_de_eleitor = %s",
        (titulo_eleitor,)
    )
    conexao.commit()

    print("")
    print("Voto confirmado com sucesso!")
    print("Seu numero de protocolo e:", protocolo)
    print("Data e hora do voto:", data_hora.strftime("%d/%m/%Y %H:%M:%S"))
    print("")

    fechar_bd(conexao, cursor)


if __name__ == "__main__":
    votacao()
