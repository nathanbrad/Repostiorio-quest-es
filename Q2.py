N1 = int(input("Digite o primeiro valor:"))
N2 = int(input("Digite o segundo valor:"))
N3 = int(input("Digite o terceiro valor:"))
Vetor = [N1, N2, N3]

if(N1 > N2 and N1> N3 and N2 > N3):
    Vetor[0] = N1
    Vetor[1] = N2
    Vetor[2] = N3
elif(N1 > N2 and N1 > N3 and N3 > N2):
    Vetor[0] = N1
    Vetor[1] = N3
    Vetor[2] = N2
elif(N2 > N1 and N2 > N3 and N1 > N3):
    Vetor[0] = N2
    Vetor[1] = N1
    Vetor[2] = N3
elif(N2 > N1 and N2 > N3 and N3 > N1):
    Vetor[0] = N2
    Vetor[1] = N3
    Vetor[2] = N1
elif(N3 > N1 and N3 > N2 and N1 > N2):
    Vetor[0] = N3
    Vetor[1] = N1
    Vetor[2] = N2
else:
    Vetor[0] = N3
    Vetor[1] = N2
    Vetor[2] = N1
print(Vetor)