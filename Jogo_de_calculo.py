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
        pontuacao = 0

        while errado != 1:
            questao, resposta_correta = Gerar_questao.gerar_questao(dificuldade)
            print(f"Resolva a questão: {questao}")

            resposta_valida = False
            while not resposta_valida:
                try:
                    resposta_usuario = int(input("Digite sua resposta: "))
                    resposta_valida = True  # A resposta é válida se a conversão para int for bem-sucedida
                except ValueError:
                    print("Entrada inválida! Por favor, insira um número.")

            if resposta_usuario == resposta_correta:
                print("Você acertou!")
                pontuacao += 1
                print(f"Pontuação atual: {pontuacao}")
            else:
                print(f"Resposta errada! A resposta correta era {resposta_correta}")
                errado = 1

        # Atualizar o leaderboard com a maior pontuação do jogador
        if nome_jogador in leaderboard:
            # Se o jogador já existir, mantém a maior pontuação
            if pontuacao > leaderboard[nome_jogador]:
                leaderboard[nome_jogador] = pontuacao
        else:
            leaderboard[nome_jogador] = pontuacao

        print("---- Fim do jogo ----")
        print(f"Sua pontuação final foi: {pontuacao}")

        # Exibir o leaderboard
        print("---- Leaderboard ----")
        for nome, pontos in sorted(leaderboard.items(), key=itemgetter(1), reverse=True):
            print(f"{nome}: {pontos} pontos")

        continuar = input("Você quer jogar novamente? (s/n): ").lower()

    print("Obrigado por jogar")

if __name__ == "__main__":
    main()
