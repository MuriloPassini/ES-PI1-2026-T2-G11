from Management import iniciar_management
from voting_sys import votacao

def iniciar_hub():
    hub_aberto = True
    while hub_aberto:
        print("=" * 15, "H U B", "=" * 15)
        print(f'{"Bem-vindo ao menu principal!":^35}')
        print(f'{"Selecione uma opcao para continuar:":^35}')
        print("1. Gerenciamento")
        print("2. Votação")
        print("0. Sair")

        escolha = input("Digite o numero da opcao desejada: ").strip()

        match escolha:
            case "1":
                iniciar_management()
            case "2":
                votacao()
            case "0":
                print("Saindo...")
                hub_aberto = False
            case _:
                print("Opcao invalida. Por favor, tente novamente.")

if __name__ == "__main__":
    iniciar_hub()

