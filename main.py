def tela_boas_vindas():
    print("=" * 60)
    print("        🏕️  CAMPONE ACADEMY")
    print("=" * 60)
    print("Construa sua jornada no universo da tecnologia.")
    print()
    print("FASE ATUAL: Treinamento de Sobrevivência")
    print("OBJETIVO: Dominar as mecânicas básicas do código antes de entrar no mundo real da tecnologia.")
    print()
    print("-" * 60)
    print("1 - Novo jogo")
    print("2 - Carregar jogo 🔒")
    print("3 - Configurações 🔒")
    print("4 - Sair")
    print("-" * 60)

    escolha = input("Escolha uma opção: ")
    return escolha


def criar_jogador():
    print()
    print("CRIAÇÃO DO JOGADOR")
    print("-" * 60)

    nome = input("Digite seu nome de jogador: ")

    if nome == "":
        nome = "Trainee Dev"

    jogador = {
        "nome": nome,
        "fase": "Treinamento de Sobrevivência",
        "nivel": "Trainee",
        "xp": 0,
        "energia": 100,
        "reputacao": 0,
    }

    print()
    print(f"Bem-vindo(a), {jogador['nome']}!")
    print("Seu treinamento de sobrevivência na CampOne Academy começou.")

    return jogador


def mostrar_status(jogador):
    print()
    print("=" * 60)
    print("STATUS DO JOGADOR")
    print("=" * 60)
    print(f"Nome: {jogador['nome']}")
    print(f"Fase: {jogador['fase']}")
    print(f"Nível: {jogador['nivel']}")
    print(f"XP: {jogador['xp']}")
    print(f"Energia: {jogador['energia']}")
    print(f"Reputação: {jogador['reputacao']}")
    print("=" * 60)


def mostrar_mapa():
    print()
    print("=" * 60)
    print("🗺️  MAPA DA CAMPONE ACADEMY")
    print("=" * 60)
    print("🔓 Nível 1: A Forja do Código")
    print()
    print("01. Decifrando a Grande Rede")
    print("02. Explorando o Motor Oculto")
    print("03. Arquivando a História do Mundo")
    print("04. Construindo a Ponte dos Mundos")
    print("05. Forjando a Interface Visual")
    print("06. Erguendo os Escudos de Defesa")
    print("07. Dominando as Linhas do Tempo")
    print("08. O Rito da Grande Implantação")
    print("09. Desenhando a Planta-Mestra")
    print()
    print("🔒 Nível 2: Mundo CampOne — bloqueado")
    print("🔒 Nível 3: Missões da Guilda — bloqueado")
    print("🔒 Nível 4: Comunidade Central — bloqueado")
    print("=" * 60)


def menu_jogador(jogador):
    while True:
        print()
        print("=" * 60)
        print("MENU DO JOGADOR")
        print("=" * 60)
        print("1 - Ver status")
        print("2 - Ver mapa")
        print("3 - Entrar no Nível 1: A Forja do Código")
        print("4 - Sair")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_status(jogador)
        elif escolha == "2":
            mostrar_mapa()
        elif escolha == "3":
            print()
            print("Nível 1: A Forja do Código")
            print("Introdução do nível ainda será criada e validada.")
        elif escolha == "4":
            print()
            print("Saindo da CampOne Academy. Até logo!")
            break
        else:
            print()
            print("Opção inválida.")


escolha = tela_boas_vindas()

if escolha == "1":
    jogador = criar_jogador()
    mostrar_status(jogador)
    mostrar_mapa()
    menu_jogador(jogador)
elif escolha == "2":
    print()
    print("Carregar jogo ainda está bloqueado.")
elif escolha == "3":
    print()
    print("Configurações ainda estão bloqueadas.")
elif escolha == "4":
    print()
    print("Saindo da CampOne Academy. Até logo!")
else:
    print()
    print("Opção inválida.")