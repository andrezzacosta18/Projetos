
#Crie um programa em Python que simule um jogo de Par ou Ímpar entre o usuário e o computador.

# Regras do Jogo:
#O jogador escolhe se quer Par (P) ou Ímpar (I).
#O jogador escolhe um número de 0 a 10.
#O computador sorteia automaticamente um número de 0 a 10.
#O programa soma os dois números.
#O programa verifica se o resultado da soma é par ou ímpar.
#O programa informa:
#O número do jogador e do computador
#A soma 
#Se o resultado foi par ou ímpar
#Quem venceu a rodada
#Se a soma for par e o usuário escolheu "Par" → o usuário vence
#Se a soma for ímpar e o usuário escolheu "Ímpar" → o usuário vence
#Caso contrário, o computador vence

tipo_num = input("Jogador escolha entre par (P) e ímpar (I): ")
num_j = int(input("Digite um número entre 0 e 10: "))

import random
num_c = random.randint(0,11)


print(f"O número escolhido pelor jogador foi: {num_j}")
print(f"O número escolhido pelo computador foi: {num_c}")

soma = num_j + num_c
print(f"A soma dos números foi: {soma}")

if (tipo_num.upper() == "P" and soma % 2 == 0) or (tipo_num.upper() == "I" and soma % 2 != 0):
    print("O jogador venceu!")
else:
    print("O computador venceu!")




if soma %2 ==0:

    print("A soma dos dois números é par!")

else:
    print("A soma dos dois números é ímpar!")











