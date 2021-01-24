print("--------------------------------------------------")
print('*        Bem vindo ao jogo de adivinhação        *')
print(' Chute um numero de 0 a 10, você tem 5 tentativas ')
print(' ================= BOA SORTE ==================== ')
print("--------------------------------------------------")
# --------variaveis--------- #
numero_secreto = 9
chute = 0
tentativas = 5
# --------CODE--------- #
while tentativas > 0 and chute != numero_secreto:
    chute = input("Digite um numero: ")
    chute = int(chute)
    print("Você digitou: ", chute)
    if numero_secreto == chute:
        print("Parabéns, Você acertou!")
    else:
        tentativas = tentativas - 1
        if tentativas == 0:
            print("Você errou, acabaram suas tentativas :/ !")
        else:
            print("Você errou, tente novamente, você ainda tem ", tentativas, "Tentativas!")

# Fim do While

# Fim do código.
