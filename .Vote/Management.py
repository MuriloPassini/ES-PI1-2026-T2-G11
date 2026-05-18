from Abertura_votação import abrir_votacao
from cadastro_candidato import menu_candidatos
from cadastro_eleitor import cadastrar_eleitor
from editar_eleitor import editar_eleitor


def iniciar_management():
    while True:
        print("=" * 15, "G E R E N C I A M E N T O", "=" * 15)
        print(f'{"Area administrativa acessada!":^57}')
        print("1. Cadastrar eleitor")
        print("2. Editar eleitor")
        print("3. Gerenciar candidatos")
        print("4. Abrir votacao (mesario)")
        print("0. Voltar")

        escolha = input("Digite o numero da opcao desejada: ").strip()

        match escolha:
            case "1":
                cadastrar_eleitor()
            case "2":
                editar_eleitor()
            case "3":
                menu_candidatos()
            case "4":
                abrir_votacao()
            case "0":
                break
            case _:
                print("Opcao invalida. Por favor, tente novamente.")


if __name__ == "__main__":
    iniciar_management()
