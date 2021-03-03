import random

print("--------------------------------------------------")
print('*        Bem vindo ao jogo de adivinhação        *')
print(' Chute um numero de 0 a 9, você tem 5 tentativas  ')
print(' ================= BOA SORTE ==================== ')
print("--------------------------------------------------")
# --------variaveis--------- #
numero_secreto = (random.randint(0, 9))
chute = int(0)
tentativas = 5
# --------CODE--------- #
while tentativas > 0 and chute != numero_secreto:
    # ---- VAR TEMP ---- #
    chute = input("Digite um numero: ")
    chute = int(chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    fim_tenta = tentativas == 0
    valido = 10 > chute >= 0
    # ---- VAR TEMP ---- #
    print("Você digitou: ", chute)
    if valido:
        if acertou:
            print("Parabéns, Você acertou!")
        else:
            tentativas = tentativas - 1
            if fim_tenta:
                print("!! YOU LOSE - O NUMERO ERA: ", numero_secreto, " ATE A PROXIMA !!")
            else:
                print("Errou!! Numero de Tentativas: ", tentativas)
                if maior:
                    print("Dica: Abaixa um pouco a bola ai campeão, ta alto demais!")
                if menor:
                    print("Dica: Um pouco mais! Um pouco mais Leonidas?!")
    else:
        print("O valor", chute, " é invalido informe um valor de 0 a 9!")
# Fim do While
# estou editando em tempo real aqui cara.... é lindo demais ver isso olha só...

# Fim do código.