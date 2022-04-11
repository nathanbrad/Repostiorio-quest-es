QuantidadeAt = int(input("Digite a quantidade atual em estoque:"))
QuantidadeMa = int(input("Digite a quatidade máxima em estoque:"))
QuantidadeMi = int(input("Digite a quantidade mínima em estoque:"))

QuantidadeMe = (QuantidadeMa + QuantidadeMi)/2
print(f"A quantidade média do estoque é {QuantidadeMe}")

if QuantidadeAt >= QuantidadeMe:
    print("Não efetuar compra")
else:
    print("Efetuar compra")