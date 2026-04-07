from Management import iniciar_management
from Voting import iniciar_votacao
def iniciar_hub():
    print('='*15,'H U B','='*15)
    print(f'{"Bem-vindo ao Hub de Gerenciamento e Votação!":^35}')
    print(f'{"Selecione uma opção para continuar:":^35}')
    print("\t1. Gerenciamento")
    print("\t2. Votação")
    escolha = input('Digite o número da opção desejada: ')
    match escolha:
        case '1': iniciar_management()
        case '2': iniciar_votacao()
        case _: print('Opção inválida. Por favor, tente novamente.')

iniciar_hub()
