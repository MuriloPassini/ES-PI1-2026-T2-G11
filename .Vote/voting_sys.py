#informações do usuário
info_completa = 0
while info_completa == 0:
    titulo_eleitor= input("Digite o título de eleitor: ")
    cpf = int(input("Digite os 4 primeiros dígitos do CPF: "))
    chave_de_acesso = int(input("Digite sua chave de acesso: "))
    if titulo_eleitor != "" or cpf != "" or chave_de_acesso != "":
        info_completa += 1
