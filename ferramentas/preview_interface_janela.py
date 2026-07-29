"""Preview visual da interface da CampOne em janela.

Este arquivo NÃO altera o jogo principal.
Ele serve apenas para visualizar como a interface pode ficar fora do terminal.
"""

import tkinter as tk


COR_FUNDO = "#0f172a"
COR_CARD = "#111827"
COR_BORDA = "#38bdf8"
COR_TEXTO = "#e5e7eb"
COR_TEXTO_FRACO = "#94a3b8"
COR_DESTAQUE = "#22c55e"
COR_BOTAO = "#1d4ed8"
COR_BOTAO_HOVER = "#2563eb"
COR_ALERTA = "#facc15"


def limpar_tela():
    for widget in app.winfo_children():
        widget.destroy()


def criar_titulo(parent, titulo, subtitulo):
    tk.Label(
        parent,
        text=titulo,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 26, "bold"),
    ).pack(pady=(0, 4))

    tk.Label(
        parent,
        text=subtitulo,
        bg=COR_FUNDO,
        fg=COR_TEXTO_FRACO,
        font=("Arial", 13),
    ).pack(pady=(0, 22))


def criar_card(parent, titulo, linhas):
    card = tk.Frame(
        parent,
        bg=COR_CARD,
        highlightbackground=COR_BORDA,
        highlightthickness=2,
        padx=22,
        pady=18,
    )
    card.pack(fill="x", pady=12)

    tk.Label(
        card,
        text=titulo,
        bg=COR_CARD,
        fg=COR_DESTAQUE,
        font=("Arial", 15, "bold"),
        anchor="w",
    ).pack(fill="x", pady=(0, 10))

    for linha in linhas:
        tk.Label(
            card,
            text=linha,
            bg=COR_CARD,
            fg=COR_TEXTO,
            font=("Arial", 12),
            anchor="w",
            justify="left",
            wraplength=820,
        ).pack(fill="x", pady=2)

    return card


def criar_botao(parent, texto, comando):
    botao = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=COR_BOTAO,
        fg="white",
        activebackground=COR_BOTAO_HOVER,
        activeforeground="white",
        relief="flat",
        padx=18,
        pady=10,
        font=("Arial", 12, "bold"),
        cursor="hand2",
    )
    botao.pack(fill="x", pady=6)
    return botao


def aviso(texto):
    janela = tk.Toplevel(root)
    janela.title("CampOne Academy")
    janela.geometry("520x220")
    janela.configure(bg=COR_FUNDO)

    tk.Label(
        janela,
        text="🎙️ COORDENADORA DA JORNADA",
        bg=COR_FUNDO,
        fg=COR_DESTAQUE,
        font=("Arial", 14, "bold"),
    ).pack(pady=(26, 12))

    tk.Label(
        janela,
        text=texto,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 12),
        wraplength=440,
        justify="center",
    ).pack(pady=10)

    criar_botao(janela, "OK", janela.destroy)


def mostrar_tela_inicial():
    limpar_tela()

    criar_titulo(
        app,
        "🏕️ CAMPONE ACADEMY DEVQUEST",
        "Formação profissional em tecnologia — agora em interface visual",
    )

    criar_card(
        app,
        "Bem-vindo à CampOne",
        [
            "Construa sua jornada no universo da tecnologia.",
            "AGÊNCIA: CampOne Academy",
            "FUNÇÃO: recrutar, preparar e conectar devs a empresas parceiras.",
            "",
            "FASE ATUAL: Recrutamento CampOne",
            "PROGRAMA: Treinamento de Sobrevivência",
            "OBJETIVO: concluir as etapas iniciais para desbloquear oportunidades no mundo real.",
        ],
    )

    menu = tk.Frame(app, bg=COR_FUNDO)
    menu.pack(fill="x", pady=18)

    criar_botao(menu, "1 - Novo jogo", mostrar_menu_jogador)
    criar_botao(menu, "2 - Carregar jogo 🔒", lambda: aviso("Carregar jogo ainda está bloqueado."))
    criar_botao(menu, "3 - Configurações 🔒", lambda: aviso("Configurações ainda estão bloqueadas."))
    criar_botao(menu, "4 - Sair", root.destroy)

    tk.Label(
        app,
        text="Preview visual: esta janela é uma demonstração. O jogo oficial ainda roda pelo main.py.",
        bg=COR_FUNDO,
        fg=COR_TEXTO_FRACO,
        font=("Arial", 10),
    ).pack(pady=(18, 0))


def mostrar_menu_jogador():
    limpar_tela()

    criar_titulo(
        app,
        "MENU DO JOGADOR",
        "Trainee Dev — CampOne Academy",
    )

    criar_card(
        app,
        "Status atual",
        [
            "Cargo atual: Desenvolvedor Trainee",
            "Origem: Academy concluída",
            "Próxima fase: Mundo Prático",
            "Empresa disponível: Loja do Dev",
            "Missão disponível: 01 — O Primeiro Dia",
        ],
    )

    menu = tk.Frame(app, bg=COR_FUNDO)
    menu.pack(fill="x", pady=18)

    criar_botao(menu, "1 - Ver status", lambda: aviso("Aqui entraria a tela de status do jogador."))
    criar_botao(menu, "2 - Ver mapa", lambda: aviso("Aqui entraria o mapa da jornada."))
    criar_botao(menu, "3 - Entrar no Mundo Prático", mostrar_missao_01)
    criar_botao(menu, "0 - Voltar", mostrar_tela_inicial)


def mostrar_missao_01():
    limpar_tela()

    criar_titulo(
        app,
        "MISSÃO 01 — O PRIMEIRO DIA",
        "Módulo 1 • Pilar 1 — Dados e Estado",
    )

    criar_card(
        app,
        "🏢 Loja do Dev",
        [
            "Empresa parceira: E-commerce de eletrônicos",
            "Mentor: Marcos — Líder Técnico",
            "Problema real: preço aparece errado no catálogo.",
            "Produto: Teclado Mecânico RGB",
        ],
    )

    criar_card(
        app,
        "👨‍💼 Marcos",
        [
            '"Bom, vou ser direto. A gente tá com um problema."',
            '"Nosso catálogo de produtos tá bugado."',
            '"O cliente abre a página do Teclado Mecânico RGB e às vezes o preço aparece certo, às vezes errado."',
        ],
    )

    criar_card(
        app,
        "📄 backend/produto.py",
        [
            "# Buscar produto no banco",
            'produto = banco.buscar("Teclado Mecanico RGB")',
            "preco = produto.preco        # 249.90",
            'desconto = "10"',
            "preco_final = preco - desconto",
        ],
    )

    criar_card(
        app,
        "🛑 Decisão do jogador",
        [
            "[1] A busca pode estar errada.",
            "[2] Algo errado na conta preco - desconto.",
            "[3] O envio para a tela pode estar corrompendo.",
        ],
    )

    menu = tk.Frame(app, bg=COR_FUNDO)
    menu.pack(fill="x", pady=18)

    criar_botao(menu, "Escolher [2] — identificar o bug", lambda: aviso("Você encontrou o bug: desconto está como texto, não número."))
    criar_botao(menu, "Voltar ao menu do jogador", mostrar_menu_jogador)


root = tk.Tk()
root.title("CampOne Academy DevQuest — Preview de Interface")
root.geometry("980x720")
root.minsize(840, 620)
root.configure(bg=COR_FUNDO)

app = tk.Frame(root, bg=COR_FUNDO, padx=36, pady=30)
app.pack(fill="both", expand=True)

mostrar_tela_inicial()

root.mainloop()
