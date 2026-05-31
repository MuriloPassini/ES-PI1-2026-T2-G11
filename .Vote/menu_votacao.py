from voting_sys import votacao
from Abertura_votação import abrir_votacao
from Encerramento_votacao import fechar_votacao
from resultado_votacao import menu_resultados
from LOGS_VOTAÇÃO import menu_auditoria

def iniciar_menu_votacao():
    """
    Exibe o menu da area de votacao e direciona para votar, auditar ou consultar resultados.

    Args:
        Nenhum.

    Returns:
        None: A funcao controla o menu ate o usuario escolher voltar.
    """
    menu_votacao_aberto = True
    while menu_votacao_aberto:
        print("=" * 10, " V O T A Ç Ã O ", "=" * 10)
        print(f'{"Area de votação acessada!":^35}')
        print("1. Votar")
        print("2. Abrir votacao (mesario)")
        print("3. Fechar votação (mesario)")
        print("4. Resultados votação (mesario)")
        print("5. Auditoria")
        print("0. Voltar")

        escolha = input("Digite o numero da opcao desejada: ").strip()

        match escolha:
            case "1":
                votacao()
            case "2":
                abrir_votacao()
            case "3":
                fechar_votacao()
            case "4":
                menu_resultados()
            case "5":
                menu_auditoria()
            case "0":
                menu_votacao_aberto = False
            case _:
                print("Opcao invalida. Por favor, tente novamente.")
