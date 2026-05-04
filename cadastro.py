def cadastrar_eleitor():
    primeiro_nome = str(input("Digite o primeiro nome do eleitor: "))
    sobrenome = str(input("Digite o sobrenome do eleitor: "))
    cpf = str(input("Digite o CPF do eleitor: "))
    eleitor = {"primeiro_nome": primeiro_nome, "sobrenome": sobrenome, "cpf": cpf}
    mesario = str(input("Atuará como mesário? (S/N): ")).strip().upper()
    if mesario == 'S':
        eleitor["mesario"] = True
    else:        
        eleitor["mesario"] = False
    return eleitor