print("--------------------------------------------------")
print('*        Bem vindo ao jogo de adivinhação        *')
print(' Chute um numero de 0 a 10, você tem 5 tentativas ')
print("--------------------------------------------------")

numero_secreto = 9

tentativas = 5

chute = input("Digite um numero: ")

# if (tentativas > 0 or chute != numero_secreto )

# chute = input("Digite um numero: ")

print("Você digitou: ",chute)

if (numero_secreto == chute):
    print("Parabéns, Você acertou!")
else:
    tentativas = tentativas - 1
    print("Você errou, tente novamente")

#fim do código.