import random

def gerar_questao(dificuldade):
 if dificuldade == 1:
  num1 = random.randint(1,10)
  num2 = random.randint(1,10)
  operação = random.choice(['+','-'])
  
 elif dificuldade ==2:
  num1 = random.randint(10,100)
  num2 = random.randint(10,100)
  operação = random.choice(['+','-'])

 elif dificuldade ==3:
  num1 = random.randint(10,100)
  num2 = random.randint(10,100)
  operação = '*'

 elif dificuldade ==4:
  num1 = random.randint(100,1000)
  num2 = random.randint(100,1000)
  operação = random.choice(['+','-','*'])

 else:
  print("Erro")

 if operação == '+':
  resposta = num1 + num2
 
 elif operação == '-':
  resposta = num1 - num2
 
 elif operação == '*':
  resposta = num1 * num2
 
 questao = f"{num1} {operação} {num2}"

 return questao, resposta
 
  
 