from banco import conectar_bd, fechar_bd
from chave_acesso import chave_acesso
from validacoes import validacaocpf, validar_titulo
import Management


def cadastrar_eleitor():
    conexao, cursor = conectar_bd()

    nome = input("Insira o nome do eleitor: ").strip()
    while nome == "" or not nome.replace(" ", "").isalpha():
        print("Nome invalido. O nome nao pode ficar vazio.")
        nome = input("Insira o nome do eleitor: ").strip()

    titulo = input("Insira o titulo de eleitor do mesmo: ").strip()
    while validar_titulo(titulo) is False:
        print("Titulo de eleitor invalido. O titulo deve conter apenas numeros e ter 12 digitos e ser válido.")
        titulo = input("Insira o titulo de eleitor do mesmo: ").strip()

    cpf = input("Insira o CPF do eleitor: ").strip().replace(".", "").replace("-", "")
    while validacaocpf(cpf) is False:
        print("CPF invalido. O CPF deve conter apenas numeros, ter 11 digitos e ser válido.")
        cpf = input("Insira o CPF do eleitor: ").strip().replace(".", "").replace("-", "")

    mesario = input("O eleitor e mesario? S/N: ").strip().upper()
    while mesario not in ("S", "N"):
        print("Opcao de mesario invalida. Use S ou N.")
        mesario = input("O eleitor e mesario? S/N: ").strip().upper()

    chave = chave_acesso(nome)

    #============================================== menuzão ==============================================

    print("=" * 35)
    print("Eleitor cadastrado com sucesso!")
    print("Resumo do eleitor:")
    print(f"Nome: {nome}")
    print(f"Titulo de eleitor: {titulo}")
    print(f"CPF: {cpf}")
    print(f"E mesario?: {mesario}")
    print(f"Chave de acesso: {chave}")
    print("GUARDE SUA CHAVE DE ACESSO!")
    print("=" * 35)

    cursor.execute(
            """
            INSERT INTO Eleitores
                (Nome_Completo, CPF, Titulo_de_eleitor, Chave_de_acesso, Mesario)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nome, cpf, titulo, chave, mesario)
        )
    conexao.commit()
    fechar_bd(conexao, cursor)
    input("Pressione Enter para continuar...")
    Management.iniciar_management()


cadastrar_eleitor()
