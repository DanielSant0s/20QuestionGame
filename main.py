import random as rnd
import re

guess = 0
questions = 0

print("Regras do jogo:\n\nInsira o número máximo, depois disso o código vai gerar um número entre 0 e o que você digitou, a partir disso faça perguntas ao código:\n\nEx1.: O número é maior que 30\nEx2.: é menor que 12\n\nE quando estiver seguro da sua resposta, diga ao código o número que você acha que seja:\n\nEx.: O número é igual a 6\n\nCaso você acerte o jogo termina, então vamos começar!\n")

def exp_check(expression):
    print("Sim" if expression is True else "Não") 

maxnumber = input("Insira o número máximo para iniciar o jogo: ")

secretnumber = rnd.randrange(0, int(maxnumber))

higher = ["maior", ">", "maior que"]
lower = ["menor", "<", "menor que"]
higherequal = ["maior igual", ">=", "maior ou igual", "≥"]
lowerequal = ["menor igual", "<=", "menor ou igual", "≤"]
equal = ["igual", "=", "igual a"]

while guess != secretnumber:
    question = input("Questione o programa: ")
    numbers = re.findall(r'\d+', question)
    if any(word in question for word in higher):
        questions+=1
        exp_check(secretnumber > int(numbers[0]))
    elif any(word in question for word in lower):
        questions+=1
        exp_check(secretnumber < int(numbers[0]))
    if any(word in question for word in higherequal):
        questions+=1
        exp_check(secretnumber >= int(numbers[0]))
    elif any(word in question for word in lowerequal):
        questions+=1
        exp_check(secretnumber <= int(numbers[0]))
    elif any(word in question for word in equal):
        questions+=1
        if secretnumber == int(numbers[0]):
            guess = int(numbers[0])
            print("Parabéns, você acertou o número!\n")
        else:
            print("Você errou, experimente perguntar mais vezes!\n")

print("Você precisou de " + str(questions) + " palpites para acertar o número, " + ("parabéns!" if questions < 20 else "da próxima vez tente acertar com menos de 20 perguntas!"))
