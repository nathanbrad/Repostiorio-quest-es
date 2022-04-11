Codigo = int(input("Digite o código de acesso."))
CodigoA = 123456
SenhaA = "C3c@9999#"

if Codigo != CodigoA:
    print("Usuário inválido.")
else:
    Senha = str(input("Digite a senha de acesso:"))
    if Senha == SenhaA:
        print("Acesso permitido.")
    else:
        print("Senha incorreta.")
