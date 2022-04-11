from math import fabs

HoraInicio = int(input("Digite a hora em que começou o jogo:"))
HoraFim = int(input("Digite a hora que terminou o jogo:"))
DuracaoJogo = fabs(HoraFim - HoraInicio)
if DuracaoJogo > 24:
    print("Duração do jogo não pode exceder as 24 horas")
else:
    if HoraInicio >= 0 and HoraFim < 6:
        print(f"A partida teve duração de {DuracaoJogo} horas e acabou no período da madrugada")
    elif HoraInicio >= 6 and HoraFim < 12:
        print(f"A partida teve duração de {DuracaoJogo} horas e acabou no período da manhan")
    elif HoraInicio >= 12 and HoraFim < 18:
        print(f"A partida teve duração de {DuracaoJogo} horas e acabou no período da Tarde")
    else:
        print(f"A partida teve duração de {DuracaoJogo} horas e acabou no período da noite")
