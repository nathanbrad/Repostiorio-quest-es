SalarioF = float(input("Digite o salário fixo recebido:"))
ValorVendas = int(input("Digite o valor das vendas:"))

if ValorVendas <= 1500:
    Comisao = ValorVendas * 0.03
    SalarioT = SalarioF + Comisao
    print(f"O salário total do vendedor é: {SalarioT}")
else:
    Comisao = ValorVendas * 0.05
    SalarioT = SalarioF + Comisao
    print(f"O salário total do vendedor é :{SalarioT}")
