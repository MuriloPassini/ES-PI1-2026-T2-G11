

def iniciar_management():
    print('='*15,'G E R E N C I A M E N T O','='*15)
    print(f'{"Área administrativa acessada!":^57}')
    print(f'{'\t1. Cadastrar eleitor':^55}')
    print(f'{'\t2. Editar eleitor':^51}')
    print(f'{'\t3. Cadastrar candidato':^57}')
    print(f'{'\t4. Mesário':^45}')
    escolha = input('Digite o número da opção desejada: ')
    match escolha:
        case '1':
            from cadastro_eleitor import cadastrar_eleitor
            cadastrar_eleitor()
        case '2':
            from busca_eleitores import iniciar_login
            iniciar_login()
        case '3':
            from cadastro_candidato import cadastro_candidato
            cadastro_candidato()
        case '4':
            print('Função de mesário em desenvolvimento. Aguarde atualizações futuras.')
        case _:
            print('Opção inválida. Por favor, tente novamente.')


iniciar_management()