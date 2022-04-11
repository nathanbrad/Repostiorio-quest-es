IdadeH1 = int(input("Digite a idade do primeiro homem:"))
IdadeH2 = int(input("Digite a idade do segundo homem:"))
IdadeM1 = int(input("Digite a idade da primeira mulher:"))
IdadeM2 = int(input("Ditite a idade da segunda mulher:"))

if IdadeH1 == IdadeH2 or IdadeM1 == IdadeM2 or IdadeH1 == IdadeH2 and IdadeM1 == IdadeM2:
    print("idades devem ser diferentes!!!")
elif IdadeH1 > IdadeH2 and IdadeM1 > IdadeM2:
    SomaIdades = IdadeH1 + IdadeM2
    ProdutoIdades = IdadeH2*IdadeM1
elif IdadeH1 > IdadeH2 and IdadeM2 > IdadeM1:
    SomaIdades = IdadeH1 + IdadeM1
    ProdutoIdades = IdadeH2 * IdadeM2
elif IdadeH2 > IdadeH1 and IdadeM2 > IdadeM1:
    SomaIdades = IdadeH2 + IdadeM1
    ProdutoIdades = IdadeH1 * IdadeM2
elif IdadeH2 > IdadeH1 and IdadeM1 > IdadeM2:
    SomaIdades = IdadeH2 + IdadeM2
    ProdutoIdades = IdadeH1 * IdadeM1


print(f"A soma das idades do homen mais velho com a mulher mais nova é {SomaIdades} e o produto das idades do homen "
      f"mais novo com a mulher mais velha é {ProdutoIdades}")
