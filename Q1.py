AV = {"avaliação 1": float(input("Digite a primeira nota:")),
      "Avaliação 2": float(input("Digite a segunda nota:"))}

Media = (AV["avaliação 1"] + AV["Avaliação 2"]) / 2

print(f"A media aritimética do aluno foi {Media}")
if Media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reporvado")
