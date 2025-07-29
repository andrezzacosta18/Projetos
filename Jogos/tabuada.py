
import random

num1 = int(input("Digite um número de 1 a 10: "))
tentativas = 5
pontos = 0

def mult ():
    global pontos
    for tentativa in range(1, tentativas + 1 ):
        num2 = (random.randint(1,11))
        pergunta = int(input(f'Quanto é {num1} x {num2}? '))
        multiplicacao = num1*num2

        if pergunta == multiplicacao:
            print('Parabéns! Você acertou e ganhou 1 ponto!')
            pontos +=1
            
        else:
            print(f'Que pena, você errou e não ganhou ponto, a resposta certa era: {multiplicacao}!')
            
    return num1*num2

pontuacao_final = mult()
print("Tabuada Finalizada!")
print(f'Sua pontuação final foi: {pontuacao_final}!')