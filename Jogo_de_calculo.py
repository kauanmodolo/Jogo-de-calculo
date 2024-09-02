import Gerar_questao
from operator import itemgetter

# Versão sem interface

leaderboard = {}

def main():
    continuar = 's'

    while continuar == 's':
        print("----- Bem vindo ao Jogo de Cálculo -----")
        nome_jogador = input("Digite seu nome: ")
        print("Escolha a dificuldade do jogo:")
        print("1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        print("4. Expert")
        print("5. Sair do jogo")
        dificuldade = int(input("Digite sua opção (1-5): "))

        if dificuldade == 5:
         break

        errado = 0
        pontuação = 0


        while errado !=1:
         questão, resposta_correta = Gerar_questao.gerar_questao(dificuldade)
         print(f"Resolva a questão: {questão}")
         resposta_usuario = int(input("Digite sua resposta: "))
         if resposta_usuario == resposta_correta:
          print("Você acertou!")
          pontuação +=1
          print(f"Pontuação atual: {pontuação}")

         else:
          print(f"Resposta errada! A resposta correta era {resposta_correta}")
          errado = 1
          
          leaderboard[nome_jogador] = pontuação

          print("---- Fim do jogo ----")
          print(f"Sua pontuação final foi: {pontuação}")
        
          print("---- Leaderboard ----")
          for nome, pontos in sorted(leaderboard.items(), key=itemgetter(1), reverse=True):
           print(f"{nome}: {pontos} pontos")
           
          continuar = input("Você quer jogar novamente? (s/n): ").lower()

print("Obrigado por jogar")


if __name__ == "__main__":
   main()

        