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


def mostrar_etapas_nivel_1():
    print()
    print("=" * 60)
    print("ETAPAS DO NÍVEL 1: A FORJA DO CÓDIGO")
    print("=" * 60)
    print("01. Decifrando a Grande Rede")
    print("02. Explorando o Motor Oculto")
    print("03. Arquivando a História do Mundo")
    print("04. Construindo a Ponte dos Mundos")
    print("05. Forjando a Interface Visual")
    print("06. Erguendo os Escudos de Defesa")
    print("07. Dominando as Linhas do Tempo")
    print("08. O Rito da Grande Implantação")
    print("09. Desenhando a Planta-Mestra")
    print("=" * 60)


def topico_internet():
    print()
    print("=" * 60)
    print("📡 TÓPICO 1: INTERNET")
    print("=" * 60)
    print("Max Campos aparece na tela e olha diretamente para você.")
    print()
    print('"Antes de qualquer código, você precisa entender a estrada."')
    print()
    print("A internet é uma rede gigante de computadores conectados.")
    print("Antes dela, cada computador era quase uma ilha.")
    print()
    print("Quando você abre um site ou aplicativo, seu dispositivo")
    print("envia um pedido por essa rede.")
    print()
    print("Esse pedido viaja até outro computador, chamado servidor,")
    print("e depois volta com uma resposta.")
    print()
    print("Resumo de sobrevivência:")
    print("- Internet = a estrada por onde os pedidos viajam.")
    print("- Cliente = quem faz o pedido.")
    print("- Servidor = quem responde.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def entrar_etapa_1():
    while True:
        print()
        print("=" * 60)
        print("01. DECIFRANDO A GRANDE REDE")
        print("=" * 60)
        print("Tema real: Fundamentos da Internet")
        print("Tipo: Treinamento de Sobrevivência")
        print("Status: Disponível")
        print()
        print("Objetivo:")
        print("Entender como um pedido sai da tela, viaja pela internet,")
        print("chega ao servidor e volta como resposta.")
        print()
        print("TÓPICOS DESTA ETAPA")
        print("-" * 60)
        print("1 - Internet")
        print("2 - Cliente e servidor")
        print("3 - HTTP e HTTPS")
        print("4 - DNS")
        print("5 - Endereço IP")
        print("6 - Requisição HTTP")
        print("0 - Voltar ao Nível 1")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_internet()
        elif escolha == "2":
            print()
            print("Tópico 2: Cliente e servidor")
            print("Aqui vamos entender quem faz o pedido e quem responde.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "3":
            print()
            print("Tópico 3: HTTP e HTTPS")
            print("Aqui vamos entender a língua da conversa na web e o cadeado de segurança.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "4":
            print()
            print("Tópico 4: DNS")
            print("Aqui vamos entender a agenda que transforma nome de site em endereço real.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "5":
            print()
            print("Tópico 5: Endereço IP")
            print("Aqui vamos entender o endereço numérico que identifica uma máquina na rede.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "6":
            print()
            print("Tópico 6: Requisição HTTP")
            print("Aqui vamos entender o pedido que sai do cliente e a resposta que volta do servidor.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


def entrar_nivel_1():
    while True:
        print()
        print("=" * 60)
        print("🔓 NÍVEL 1: A FORJA DO CÓDIGO")
        print("=" * 60)
        print("Fase: Treinamento de Sobrevivência")
        print()
        print("1 - Ver etapas do Nível 1")
        print("2 - Entrar na etapa 01: Decifrando a Grande Rede")
        print("0 - Voltar ao menu do jogador")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_etapas_nivel_1()
        elif escolha == "2":
            entrar_etapa_1()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


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
            entrar_nivel_1()
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