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


def criar_jogador():
    print()
    print("CRIAÇÃO DO JOGADOR")
    print("-" * 60)

    nome = input("Digite seu nome de jogador: ")

    if nome == "":
        nome = "Trainee Dev"

    jogador = {
        "nome": nome,
        "fase": "Recrutamento CampOne",
        "programa": "Treinamento de Sobrevivência",
        "nivel": "Trainee",
        "xp": 0,
        "energia": 100,
        "reputacao": 0,
    }

    print()
    print(f"Bem-vindo(a), {jogador['nome']}!")
    print("Seu recrutamento na CampOne Academy começou.")

    return jogador


def mostrar_status(jogador):
    print()
    print("=" * 60)
    print("STATUS DO JOGADOR")
    print("=" * 60)
    print(f"Nome: {jogador['nome']}")
    print(f"Fase: {jogador['fase']}")
    print(f"Programa: {jogador['programa']}")
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
    print("01. Decifrando a Grande Rede ✅")
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
    print("01. Decifrando a Grande Rede ✅")
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
    print("Eloisa aparece na tela e olha diretamente para você.")
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


def topico_cliente_servidor():
    print()
    print("=" * 60)
    print("🧭 TÓPICO 2: CLIENTE E SERVIDOR")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Toda conversa na web tem dois lados: quem pede e quem responde."')
    print()
    print("Cliente é quem faz o pedido.")
    print("Na maioria das vezes, o cliente é o navegador ou o aplicativo.")
    print()
    print("Servidor é quem recebe o pedido, processa e devolve uma resposta.")
    print("Ele fica em outro computador, preparado para atender muitas pessoas.")
    print()
    print("Exemplo simples:")
    print("- Você abre um app e toca em um botão.")
    print("- O app faz um pedido.")
    print("- O servidor recebe, trabalha e responde.")
    print("- A resposta volta para aparecer na tela.")
    print()
    print("Resumo de sobrevivência:")
    print("- Cliente = quem pede.")
    print("- Servidor = quem responde.")
    print("- A web funciona porque esses dois lados conversam.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def topico_http_https():
    print()
    print("=" * 60)
    print("🔐 TÓPICO 3: HTTP E HTTPS")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Cliente e servidor precisam falar a mesma língua."')
    print()
    print("HTTP é o conjunto de regras da conversa na web.")
    print("É ele que organiza pedidos e respostas entre cliente e servidor.")
    print()
    print("Quando você abre uma página, o cliente envia um pedido.")
    print("O servidor entende esse pedido porque os dois seguem o mesmo combinado.")
    print()
    print("HTTPS é a versão segura dessa conversa.")
    print("Ele coloca um cadeado na troca de informações.")
    print()
    print("Isso protege dados importantes, como senhas, dados pessoais")
    print("e informações bancárias.")
    print()
    print("Resumo de sobrevivência:")
    print("- HTTP = a língua da conversa na web.")
    print("- HTTPS = a mesma conversa, mas protegida por um cadeado.")
    print("- Todo sistema sério precisa usar comunicação segura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def topico_dns():
    print()
    print("=" * 60)
    print("📖 TÓPICO 4: DNS")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Na internet, nomes fáceis precisam virar endereços reais."')
    print()
    print("DNS é como a agenda da internet.")
    print("Ele transforma nomes de sites em endereços que as máquinas entendem.")
    print()
    print("Quando você digita um nome como campone.com,")
    print("o navegador precisa descobrir onde esse sistema mora de verdade.")
    print()
    print("O DNS faz essa tradução.")
    print("Ele responde qual é o endereço real do servidor.")
    print()
    print("Sem DNS, você teria que decorar números difíceis")
    print("em vez de nomes simples.")
    print()
    print("Resumo de sobrevivência:")
    print("- DNS = agenda da internet.")
    print("- Nome do site = nome fácil para humanos.")
    print("- Endereço real = lugar onde o servidor mora.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def topico_endereco_ip():
    print()
    print("=" * 60)
    print("📍 TÓPICO 5: ENDEREÇO IP")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Depois que a agenda encontra o nome, ainda falta saber o número da casa."')
    print()
    print("Endereço IP é o número que identifica uma máquina dentro da rede.")
    print("Ele funciona como o endereço real de um computador ou servidor.")
    print()
    print("Quando você digita um nome de site, o DNS ajuda a encontrar")
    print("o endereço IP do servidor onde aquele sistema mora.")
    print()
    print("Sem IP, o pedido não saberia para onde viajar.")
    print("Seria como uma carta sem endereço.")
    print()
    print("Resumo de sobrevivência:")
    print("- IP = endereço numérico de uma máquina na rede.")
    print("- DNS = agenda que encontra esse endereço.")
    print("- Sem IP, o pedido não chega ao destino.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def topico_requisicao_http():
    print()
    print("=" * 60)
    print("📨 TÓPICO 6: REQUISIÇÃO HTTP")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Agora vamos juntar a estrada, os dois lados, a língua, a agenda e o endereço."')
    print()
    print("Requisição HTTP é o pedido que o cliente envia para o servidor.")
    print("Resposta HTTP é o que o servidor devolve para o cliente.")
    print()
    print("Quando você toca em um botão, abre uma página ou envia um formulário,")
    print("o sistema cria uma requisição.")
    print()
    print("Essa requisição viaja pela internet até o servidor.")
    print("O servidor entende o pedido, trabalha e devolve uma resposta.")
    print()
    print("Resumo de sobrevivência:")
    print("- Requisição = pedido que sai do cliente.")
    print("- Resposta = retorno que vem do servidor.")
    print("- Todo sistema web funciona nesse vai e volta.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def resumo_etapa_1():
    print()
    print("=" * 60)
    print("🧩 RESUMO DA ETAPA 01")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Agora você já consegue enxergar o caminho invisível."')
    print()
    print("Quando você usa um site ou aplicativo, nada acontece por mágica.")
    print()
    print("O cliente faz um pedido.")
    print("Esse pedido usa a linguagem HTTP ou HTTPS.")
    print("O DNS ajuda a encontrar o endereço real do servidor.")
    print("O IP aponta para a máquina certa na rede.")
    print("A internet carrega o pedido até lá.")
    print("O servidor responde.")
    print("E a resposta volta para aparecer na tela.")
    print()
    print("Fluxo de sobrevivência:")
    print("Cliente → Internet → Servidor → Resposta → Tela")
    print()
    print("Você concluiu a visão inicial da Grande Rede.")
    print("Ainda não há recompensa ou progresso salvo nesta versão.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def cena_abertura_etapa_1():
    print()
    print("=" * 60)
    print("🎬 CENA DA ETAPA 01")
    print("=" * 60)
    print("Eloisa aparece na entrada da CampOne Academy.")
    print("Ela olha para você como quem reconhece um novo começo.")
    print()
    print('"Bem-vindo(a) à CampOne Academy."')
    print()
    print('"Eu sou Eloisa."')
    print('"Faço parte da equipe de recrutamento da CampOne."')
    print()
    print('"A CampOne Academy é uma agência que recruta, prepara e avalia devs."')
    print('"Ela acompanha sua evolução e abre portas para empresas parceiras."')
    print()
    print("Você ainda não foi contratado.")
    print("Neste momento, você participa do recrutamento da CampOne.")
    print()
    print("Nosso objetivo é avaliar sua lógica,")
    print("sua interpretação de problemas")
    print("e sua compreensão sobre como os sistemas realmente funcionam.")
    print()
    print("Ao concluir este treinamento,")
    print("você estará preparado para buscar novas oportunidades em empresas parceiras.")
    print()
    print('"Antes de qualquer código, você precisa enxergar o território."')
    print('"Todo aplicativo, site ou sistema esconde um caminho invisível."')
    print()
    print('"Nesta etapa, sua missão é decifrar a Grande Rede."')
    print('"Você vai entender como um pedido sai da tela, atravessa a internet,')
    print('chega ao servidor e volta como resposta."')
    print()
    print("Missão atual: Decifrando a Grande Rede")
    print("Tema real: Fundamentos da Internet")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def conceito_etapa_1():
    while True:
        print()
        print("=" * 60)
        print("💡 CONCEITO: O TERRITÓRIO")
        print("=" * 60)
        print("Aqui ficam os fundamentos da Grande Rede.")
        print()
        print("1 - Internet")
        print("2 - Cliente e servidor")
        print("3 - HTTP e HTTPS")
        print("4 - DNS")
        print("5 - Endereço IP")
        print("6 - Requisição HTTP")
        print("7 - Ver resumo do conceito")
        print("0 - Voltar à etapa 01")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_internet()
        elif escolha == "2":
            topico_cliente_servidor()
        elif escolha == "3":
            topico_http_https()
        elif escolha == "4":
            topico_dns()
        elif escolha == "5":
            topico_endereco_ip()
        elif escolha == "6":
            topico_requisicao_http()
        elif escolha == "7":
            resumo_etapa_1()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


def pratica_caminho_clique():
    print()
    print("=" * 60)
    print("🛠 PRÁTICA: O CAMINHO DE UM CLIQUE")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Agora vamos caminhar por dentro de um clique."')
    print()
    print("Imagine que você abriu o aplicativo da CampOne Academy")
    print("e tocou em um botão para ver uma lista de produtos.")
    print()
    print("O caminho invisível começa assim:")
    print()
    print("1. Seu toque acontece na tela.")
    print("2. A tela monta um pedido.")
    print("3. O pedido viaja pela internet.")
    print("4. O servidor recebe esse pedido.")
    print("5. O sistema busca ou processa as informações.")
    print("6. O servidor envia uma resposta.")
    print("7. A tela mostra o resultado para você.")
    print()
    print("Esse é o primeiro caminho que todo dev precisa enxergar.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def experimentacao_etapa_1():
    print()
    print("=" * 60)
    print("🧪 EXPERIMENTAÇÃO: E SE ALGO QUEBRAR?")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Quando tudo funciona, o caminho parece invisível."')
    print('"Mas quando algo quebra, o dev precisa descobrir onde o pedido parou."')
    print()
    print("Vamos olhar alguns pontos onde a Grande Rede pode falhar:")
    print()
    print("1. O DNS falha")
    print("- O nome do site não encontra o endereço real do servidor.")
    print()
    print("2. O servidor não responde")
    print("- O pedido chega, mas ninguém devolve resposta.")
    print()
    print("3. O endereço não existe")
    print("- O cliente pediu algo que o servidor não encontrou.")
    print()
    print("4. O banco demora ou falha")
    print("- O servidor precisa de informação, mas a despensa não responde.")
    print()
    print("5. O cadeado seguro falha")
    print("- A conversa protegida pelo HTTPS não passa confiança.")
    print()
    print("Resumo de sobrevivência:")
    print("- Erro não é fim de jogo.")
    print("- Erro é pista.")
    print("- Um dev aprende a perguntar: onde o pedido parou?")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def aplicacao_vida_real_etapa_1():
    print()
    print("=" * 60)
    print("🏢 APLICAÇÃO NA VIDA REAL")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Agora você vai perceber que a Grande Rede está em todo lugar."')
    print()
    print("O caminho invisível não acontece só na CampOne Academy.")
    print("Ele aparece nos aplicativos que você usa todos os dias.")
    print()
    print("Exemplos:")
    print()
    print("1. WhatsApp")
    print("- Você envia uma mensagem.")
    print("- O app manda um pedido pela internet.")
    print("- O servidor recebe, guarda e entrega a mensagem.")
    print()
    print("2. App do banco")
    print("- Você pede para ver seu saldo.")
    print("- O app envia um pedido.")
    print("- O servidor busca a informação e devolve para a tela.")
    print()
    print("3. Netflix")
    print("- Você abre um filme.")
    print("- O app pede informações ao servidor.")
    print("- A resposta volta com capa, título, descrição e episódios.")
    print()
    print("4. iFood")
    print("- Você faz um pedido.")
    print("- O app envia os dados.")
    print("- O servidor processa e confirma a compra.")
    print()
    print("Resumo de sobrevivência:")
    print("- Todo app conectado usa pedidos e respostas.")
    print("- A tela é só a parte visível.")
    print("- A Grande Rede trabalha por trás.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def prova_dominio_etapa_1():
    while True:
        print()
        print("=" * 60)
        print("🧠 PROVA DE DOMÍNIO")
        print("=" * 60)
        print("Eloisa aparece na tela e olha diretamente para você.")
        print()
        print('"Vamos confirmar se você enxerga o caminho invisível."')
        print()
        print("Quando você toca em um botão de um app")
        print("e uma informação aparece na tela, o que acontece por trás?")
        print()
        print("1 - O botão faz tudo sozinho dentro da tela.")
        print("2 - O app cria um pedido, envia pela internet, o servidor responde e a tela mostra o resultado.")
        print("3 - A internet guarda a informação e mostra direto para o usuário.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "2":
            print("Eloisa sorri.")
            print('"Exato. Você enxergou o caminho principal."')
            print('"A tela não faz tudo sozinha: ela envia um pedido, o servidor responde e a tela mostra o resultado."')
            print()
            print("Prova de Domínio concluída nesta versão.")
            print("Ainda não há XP, recompensa ou progresso salvo.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print("Eloisa levanta a mão com calma.")
            print('"Quase, mas cuidado: o botão não faz tudo sozinho."')
            print('"O botão inicia o pedido. Depois esse pedido precisa viajar até o servidor."')
            print()
            print("Tente de novo pensando no caminho:")
            print("tela → pedido → internet → servidor → resposta → tela")
        elif escolha == "3":
            print("Eloisa aponta para o caminho da Grande Rede.")
            print('"A internet não é a despensa que guarda tudo."')
            print('"Ela é a estrada por onde o pedido viaja. Quem responde é o servidor."')
            print()
            print("Tente de novo pensando no papel de cada parte.")
        else:
            print("Eloisa inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def registro_etapa_1():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Toda missão importante precisa deixar um registro."')
    print()
    print("Nesta etapa, você passou pelos fundamentos da Grande Rede:")
    print()
    print("- entendeu que a internet é a estrada dos pedidos;")
    print("- viu que cliente pede e servidor responde;")
    print("- conheceu HTTP, HTTPS, DNS, IP e requisição;")
    print("- caminhou por dentro de um clique;")
    print("- viu que erro é pista, não fim de jogo;")
    print("- aplicou o caminho invisível em apps reais;")
    print("- concluiu a Prova de Domínio.")
    print()
    print("Registro atual:")
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_1():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL")
    print("=" * 60)
    print("Eloisa aparece na tela e olha diretamente para você.")
    print()
    print('"Antes de seguir, revise o que você acabou de dominar."')
    print()
    print("Relatório da missão: Decifrando a Grande Rede")
    print()
    print("Você agora sabe que:")
    print()
    print("- a internet conecta computadores pelo mundo;")
    print("- cliente é quem faz o pedido;")
    print("- servidor é quem responde;")
    print("- HTTP organiza a conversa;")
    print("- HTTPS protege a conversa;")
    print("- DNS encontra o endereço real do servidor;")
    print("- IP identifica uma máquina na rede;")
    print("- requisição é o pedido;")
    print("- resposta é o retorno do servidor;")
    print("- erro é pista para descobrir onde o caminho parou.")
    print()
    print("Conclusão:")
    print("Você começou a enxergar o sistema por trás da tela.")
    print()
    print("A etapa ainda não marca conclusão permanente nesta versão.")
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
        print("Status: Operacional")
        print()
        print("CENTRO DE OPERAÇÕES")
        print("-" * 60)
        print("1 - Iniciar Missão")
        print("2 - Reconhecimento")
        print("3 - Campo de Treinamento")
        print("4 - Laboratório de Falhas")
        print("5 - Missão em Produção")
        print("6 - Prova de Domínio")
        print("7 - Registrar Experiência")
        print("8 - Relatório Final")
        print("0 - Retornar ao Nível 1")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cena_abertura_etapa_1()
        elif escolha == "2":
            conceito_etapa_1()
        elif escolha == "3":
            pratica_caminho_clique()
        elif escolha == "4":
            experimentacao_etapa_1()
        elif escolha == "5":
            aplicacao_vida_real_etapa_1()
        elif escolha == "6":
            prova_dominio_etapa_1()
        elif escolha == "7":
            registro_etapa_1()
        elif escolha == "8":
            relatorio_final_etapa_1()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


def cena_abertura_etapa_2():
    print()
    print("=" * 60)
    print("🎬 CENA DA ETAPA 02")
    print("=" * 60)
    print("Eloisa aparece ao lado da entrada do Motor Oculto.")
    print("Ela olha diretamente para você.")
    print()
    print('"Você já percorreu a Grande Rede."')
    print('"Agora precisa entender o que acontece quando o pedido chega ao servidor."')
    print()
    print("Eloisa olha para David, que está diante de uma sala cheia de painéis.")
    print()
    print('"David, ele está pronto para conhecer o motor por trás da tela."')
    print()
    print("David se aproxima e olha diretamente para você.")
    print()
    print('"Eu sou David."')
    print('"Cuido do backend: a parte invisível que recebe pedidos, aplica regras e prepara respostas."')
    print()
    print('"A Eloisa te mostrou como um pedido viaja pela Grande Rede."')
    print('"Agora eu vou te mostrar o motor que trabalha quando esse pedido chega ao servidor."')
    print()
    print('"Bem-vindo ao Motor Oculto."')
    print()
    print('"Toda tela bonita precisa de um motor trabalhando por trás."')
    print('"Esse motor é o backend."')
    print()
    print("Missão atual: Explorando o Motor Oculto")
    print("Tema real: Backend")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def topico_backend():
    print()
    print("=" * 60)
    print("⚙️ TÓPICO 1: O QUE É BACKEND")
    print("=" * 60)
    print("David aparece na tela e olha diretamente para você.")
    print()
    print('"Backend é a parte do sistema que trabalha por trás da tela."')
    print()
    print("Quando o jogador toca em um botão, a tela não resolve tudo sozinha.")
    print("Ela envia um pedido para o servidor.")
    print()
    print("No servidor, o backend recebe esse pedido, aplica regras,")
    print("busca ou organiza informações e prepara uma resposta.")
    print()
    print("É por isso que ele é chamado de motor oculto:")
    print("o usuário não vê, mas sem ele o sistema não funciona.")
    print()
    print("Resumo de sobrevivência:")
    print("- Backend = parte invisível que processa pedidos.")
    print("- Ele roda no servidor.")
    print("- Ele aplica regras e prepara respostas para a tela.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def topico_servidor_web():
    print()
    print("=" * 60)
    print("🖥️ TÓPICO 2: SERVIDOR WEB")
    print("=" * 60)
    print("David aparece na tela e olha diretamente para você.")
    print()
    print('"Todo motor precisa de um lugar para ficar ligado."')
    print()
    print("Servidor web é o programa que fica esperando pedidos chegarem.")
    print("Ele recebe requisições vindas da internet e devolve respostas.")
    print()
    print("Quando muita gente acessa um sistema ao mesmo tempo,")
    print("o servidor web precisa organizar esse fluxo de entrada e saída.")
    print()
    print("Ele é como uma porta de atendimento sempre aberta.")
    print("O usuário não vê, mas todo sistema online depende dele.")
    print()
    print("Resumo de sobrevivência:")
    print("- Servidor web = programa que recebe pedidos na internet.")
    print("- Ele entrega respostas para clientes, navegadores ou aplicativos.")
    print("- Sem ele, o backend não teria uma porta de entrada.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def entrar_etapa_2():
    while True:
        print()
        print("=" * 60)
        print("02. EXPLORANDO O MOTOR OCULTO")
        print("=" * 60)
        print("Tema real: Backend")
        print("Tipo: Treinamento de Sobrevivência")
        print("Status: Disponível")
        print()
        print("Objetivo:")
        print("Entender o motor invisível que processa pedidos,")
        print("aplica regras e responde para a tela.")
        print()
        print("TÓPICOS DESTA ETAPA")
        print("-" * 60)
        print("1 - Iniciar cena da etapa")
        print("2 - O que é Backend")
        print("3 - Servidor Web")
        print("4 - Lógica de Negócio")
        print("5 - API")
        print("6 - API REST")
        print("7 - Endpoints")
        print("8 - Rotas")
        print("9 - JSON")
        print("0 - Voltar ao Nível 1")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cena_abertura_etapa_2()
        elif escolha == "2":
            topico_backend()
        elif escolha == "3":
            topico_servidor_web()
        elif escolha == "4":
            print()
            print("Tópico 3: Lógica de Negócio")
            print("Aqui vamos entender onde vivem as regras específicas da empresa.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "5":
            print()
            print("Tópico 4: API")
            print("Aqui vamos entender o balcão de conversa entre sistemas.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "6":
            print()
            print("Tópico 5: API REST")
            print("Aqui vamos entender um padrão comum para organizar APIs.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "7":
            print()
            print("Tópico 6: Endpoints")
            print("Aqui vamos entender os endereços específicos de uma API.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "8":
            print()
            print("Tópico 7: Rotas")
            print("Aqui vamos entender como o backend decide para onde cada pedido vai.")
            print("Conteúdo completo será construído em partes.")
        elif escolha == "9":
            print()
            print("Tópico 8: JSON")
            print("Aqui vamos entender o formato usado para trocar dados entre sistemas.")
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
        print("Fase: Recrutamento CampOne")
        print("Programa: Treinamento de Sobrevivência")
        print()
        print("1 - Ver etapas do Nível 1")
        print("2 - Entrar na etapa 01: Decifrando a Grande Rede")
        print("3 - Entrar na etapa 02: Explorando o Motor Oculto")
        print("0 - Voltar ao menu do jogador")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_etapas_nivel_1()
        elif escolha == "2":
            entrar_etapa_1()
        elif escolha == "3":
            entrar_etapa_2()
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