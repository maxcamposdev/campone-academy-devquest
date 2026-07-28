"""Telas gerais reutilizáveis da Engine."""

def tela_boas_vindas():
    print("=" * 60)
    print("        🏕️  CAMPONE ACADEMY")
    print("=" * 60)
    print("Construa sua jornada no universo da tecnologia.")
    print()
    print("AGÊNCIA: CampOne Academy")
    print("FUNÇÃO: recrutar, preparar e conectar devs")
    print("a empresas parceiras.")
    print()
    print("FASE ATUAL: Recrutamento CampOne")
    print("PROGRAMA: Treinamento de Sobrevivência")
    print("OBJETIVO: Concluir as etapas iniciais para desbloquear oportunidades no mundo real da tecnologia.")
    print()
    print("-" * 60)
    print("1 - Novo jogo")
    print("2 - Carregar jogo 🔒")
    print("3 - Configurações 🔒")
    print("4 - Sair")
    print("-" * 60)

    escolha = input("Escolha uma opção: ")
    return escolha
