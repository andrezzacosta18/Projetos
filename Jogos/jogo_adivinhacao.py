#Criar um jogo em que o computador sorteia um número entre 1 e 100, e o usuário tenta adivinhar.
#  A cada tentativa, o programa informa se o chute foi muito alto, muito baixo ou correto.

import random
numero = random.randint(1, 100)

while True:
    num_jogador = int(input("Digite um número: "))

    if num_jogador < numero:

        print("Chute muito baixo!")

    elif num_jogador > numero:
        print("Chute muito alto!")

    else:
        print("Você acertou!")
        break
  

# com tentativas limitadas:

import random

numero_secreto = random.randint(1, 100)
max_tentativas = 5

print("Tente adivinhar o número entre 1 e 100!")
print(f"Você tem {max_tentativas} tentativas.")

for tentativa in range(1, max_tentativas + 1):
    chute = int(input(f"Tentativa {tentativa}: "))

    if chute < numero_secreto:
        print("Muito baixo!")
    elif chute > numero_secreto:
        print("Muito alto!")
    else:
        print(f"🎉 Acertou! O número era {numero_secreto}.\nVocê usou {tentativa} tentativa(s).")
        break
else:
    print(f"❌ Suas {max_tentativas} tentativas acabaram. O número era {numero_secreto}.")

       
