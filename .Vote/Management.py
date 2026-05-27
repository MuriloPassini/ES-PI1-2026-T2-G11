from Abertura_votação import abrir_votacao
from cadastro_candidato import menu_candidatos
from cadastro_eleitor import cadastrar_eleitor
from editar_eleitor import editar_eleitor
from Encerramento_votação import fechar_votacao


def iniciar_management():
    selecao_management = 0
    while selecao_management == 0:
        print("=" * 15, "G E R E N C I A M E N T O", "=" * 15)
        print(f'{"Area administrativa acessada!":^57}')
        print("1. Cadastrar eleitor")
        print("2. Editar eleitor")
        print("3. Gerenciar candidatos")
        print("4. Abrir votacao (mesario)")
        print("5. Fechar votação (mesario)")
        print("0. Voltar")

        escolha = input("Digite o numero da opcao desejada: ").strip()

        match escolha:
            case "1":
                cadastrar_eleitor()
                selecao_management += 1
            case "2":
                editar_eleitor()
                selecao_management += 1
            case "3":
                menu_candidatos()
                selecao_management += 1
            case "4":
                abrir_votacao()
                selecao_management += 1
            case "5":
                fechar_votacao()
                selecao_management += 1
            case "0":
                selecao_management += 1
                break
            case _:
                print("Opcao invalida. Por favor, tente novamente.")


if __name__ == "__main__":
    iniciar_management()
