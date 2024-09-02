import tkinter as tk
from tkinter import messagebox, simpledialog
import Gerar_questao
from operator import itemgetter

# Versão com interface 

class JogoDeCalculoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Cálculo")
        self.leaderboard = {}

        # Criando os widgets da interface
        self.label_nome = tk.Label(root, text="Digite seu nome:")
        self.entry_nome = tk.Entry(root)

        self.label_dificuldade = tk.Label(root, text="Escolha a dificuldade do jogo:")
        self.dificuldade_var = tk.IntVar(value=1)
        self.radio_facil = tk.Radiobutton(root, text="Fácil", variable=self.dificuldade_var, value=1)
        self.radio_normal = tk.Radiobutton(root, text="Normal", variable=self.dificuldade_var, value=2)
        self.radio_dificil = tk.Radiobutton(root, text="Difícil", variable=self.dificuldade_var, value=3)
        self.radio_expert = tk.Radiobutton(root, text="Expert", variable=self.dificuldade_var, value=4)
        self.radio_sair = tk.Radiobutton(root, text="Sair do jogo", variable=self.dificuldade_var, value=5)

        self.button_iniciar = tk.Button(root, text="Iniciar Jogo", command=self.iniciar_jogo)

        # Posicionando os widgets na janela
        self.label_nome.grid(row=0, column=0, pady=10)
        self.entry_nome.grid(row=0, column=1, pady=10)

        self.label_dificuldade.grid(row=1, column=0, pady=10)
        self.radio_facil.grid(row=2, column=0, sticky="w")
        self.radio_normal.grid(row=3, column=0, sticky="w")
        self.radio_dificil.grid(row=4, column=0, sticky="w")
        self.radio_expert.grid(row=5, column=0, sticky="w")
        self.radio_sair.grid(row=6, column=0, sticky="w")

        self.button_iniciar.grid(row=7, column=0, columnspan=2, pady=20)

    def iniciar_jogo(self):
        nome_jogador = self.entry_nome.get()
        dificuldade = self.dificuldade_var.get()

        if dificuldade == 5:
            self.root.quit()
            return

        if not nome_jogador:
            messagebox.showerror("Erro", "Por favor, insira seu nome.")
            return

        pontuacao = 0
        errado = 0

        while errado != 1:
            questao, resposta_correta = Gerar_questao.gerar_questao(dificuldade)
            resposta_usuario = simpledialog.askstring("Questão", f"Resolva a questão: {questao}")

            if resposta_usuario is None:  # Se o usuário cancelar a entrada
                messagebox.showinfo("Jogo cancelado", "Você cancelou o jogo.")
                return

            try:
                resposta_usuario = int(resposta_usuario)
            except ValueError:
                messagebox.showerror("Erro", "Resposta inválida. Por favor, insira um número.")
                continue

            if resposta_usuario == resposta_correta:
                messagebox.showinfo("Correto!", "Você acertou!")
                pontuacao += 1
            else:
                messagebox.showinfo("Errado!", f"Resposta errada! A resposta correta era {resposta_correta}")
                errado = 1

        # Atualizar o leaderboard com a pontuação do jogador
        if nome_jogador in self.leaderboard:
            self.leaderboard[nome_jogador] += pontuacao
        else:
            self.leaderboard[nome_jogador] = pontuacao

        self.mostrar_leaderboard(nome_jogador, pontuacao)

    def mostrar_leaderboard(self, nome_jogador, pontuacao):
        leaderboard_text = "---- Leaderboard ----\n"
        for nome, pontos in sorted(self.leaderboard.items(), key=itemgetter(1), reverse=True):
            leaderboard_text += f"{nome}: {pontos} pontos\n"

        messagebox.showinfo(f"Fim do jogo, {nome_jogador}!", f"Sua pontuação final foi: {pontuacao}\n\n{leaderboard_text}")
        continuar = messagebox.askquestion("Continuar", "Você quer jogar novamente?")

        if continuar.lower() == 'yes':
            self.entry_nome.delete(0, tk.END)
        else:
            self.root.quit()

# Inicializando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDeCalculoApp(root)
    root.mainloop()
