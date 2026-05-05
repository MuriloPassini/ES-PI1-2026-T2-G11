from Management import iniciar_management
from busca_eleitores import iniciar_votacao
def iniciar_hub():
    while True:
        print('='*15,'H U B','='*15)
        print(f'{"Bem-vindo ao Hub de Gerenciamento e Votação!":^35}')
        print(f'{"Selecione uma opção para continuar:":^35}')
        print("\t1. Gerenciamento")
        print("\t2. Votação")
        print("\t0. Sair")
        escolha = input('Digite o número da opção desejada: ')
        match escolha:
            case '1':
                iniciar_management()
            case '2':
                iniciar_votacao()
            case '0':
                print("Saindo...")
                break
            case _:
                print('Opção inválida. Por favor, tente novamente.')
iniciar_hub()
