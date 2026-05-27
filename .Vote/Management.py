from Abertura_votação import abrir_votacao
from cadastro_candidato import menu_candidatos
from cadastro_eleitor import menu_eleitores
from Encerramento_votacao import fechar_votacao
from resultado_votacao import menu_resultados


def iniciar_management():
    gerenciamento_aberto = True
    while gerenciamento_aberto:
        print("=" * 15, "G E R E N C I A M E N T O", "=" * 15)
        print(f'{"Area administrativa acessada!":^57}')
        print("1. Gerenciar eleitores")
        print("2. Gerenciar candidatos")
        print("3. Abrir votacao (mesario)")
        print("4. Fechar votação (mesario)")
        print("5. Resultados votação (mesario)")
        print("0. Voltar")

        escolha = input("Digite o numero da opcao desejada: ").strip()

        match escolha:
            case "1":
                menu_eleitores()
            case "2":
                menu_candidatos()
            case "3":
                abrir_votacao()
            case "4":
                fechar_votacao()
            case "5":
                menu_resultados()
            case "0":
                gerenciamento_aberto = False
            case _:
                print("Opcao invalida. Por favor, tente novamente.")
