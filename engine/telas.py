"""Telas gerais reutilizáveis da Engine."""

from engine.ui import caixa, menu, titulo


def tela_boas_vindas():
    titulo("🏕️  CAMPONE ACADEMY", "DevQuest")

    caixa([
        "Construa sua jornada no universo da tecnologia.",
        "",
        "AGÊNCIA: CampOne Academy",
        "FUNÇÃO: recrutar, preparar e conectar devs",
        "a empresas parceiras.",
        "",
        "FASE ATUAL: Recrutamento CampOne",
        "PROGRAMA: Treinamento de Sobrevivência",
        "OBJETIVO: concluir as etapas iniciais",
        "para desbloquear oportunidades no mundo real.",
    ])

    print()
    menu([
        ("1", "Novo jogo"),
        ("2", "Carregar jogo 🔒"),
        ("3", "Configurações 🔒"),
        ("4", "Sair"),
    ])

    escolha = input("Escolha uma opção: ")
    return escolha
