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
    while True:
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
        print("Pergunta de domínio:")
        print("O que é a internet dentro do caminho invisível dos sistemas?")
        print()
        print("1 - Um aplicativo específico que guarda todos os sites.")
        print("2 - Uma rede de computadores conectados por onde pedidos e respostas viajam.")
        print("3 - Um banco de dados gigante onde ficam salvas todas as informações.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "2":
            print("Eloisa confirma.")
            print('"Isso. A internet é a estrada da Grande Rede."')
            print('"É por ela que os pedidos saem do cliente, chegam ao servidor e voltam como resposta."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print("Eloisa reancora.")
            print('"Um aplicativo pode usar a internet, mas ele não é a internet."')
            print('"O app é uma porta que você usa. A internet é a rede por onde o pedido viaja."')
            print()
            print('"Tenta de novo pensando na estrada, não no aplicativo."')
        elif escolha == "3":
            print("Eloisa reancora.")
            print('"Guardar informações é papel de bancos de dados e servidores."')
            print('"A internet não é a despensa. Ela é o caminho por onde as informações viajam."')
            print()
            print('"Tenta de novo pensando no caminho entre máquinas."')
        else:
            print("Eloisa inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_cliente_servidor():
    while True:
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
        print("Pergunta de domínio:")
        print("Na conversa entre cliente e servidor, quem faz o pedido e quem responde?")
        print()
        print("1 - O cliente faz o pedido, e o servidor recebe, processa e responde.")
        print("2 - O servidor faz o pedido, e o cliente guarda tudo no banco.")
        print("3 - O cliente e o servidor fazem a mesma função ao mesmo tempo.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Eloisa valida.")
            print('"Exato. Cliente é quem pede. Servidor é quem responde."')
            print('"Essa divisão é uma das bases dos sistemas web."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Eloisa reancora.")
            print('"O servidor não é quem começa o pedido nesse fluxo."')
            print('"Normalmente, quem inicia é o cliente: navegador, app ou tela."')
            print('"O servidor fica do outro lado, preparado para responder."')
        elif escolha == "3":
            print("Eloisa reancora.")
            print('"Eles conversam, mas não fazem a mesma função."')
            print('"Um lado pede. O outro responde."')
            print()
            print('"Tenta de novo separando os papéis."')
        else:
            print("Eloisa inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_http_https():
    while True:
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
        print("HTTPS é a versão segura dessa conversa.")
        print("Ele coloca um cadeado na troca de informações.")
        print()
        print("Pergunta de domínio:")
        print("Para que servem HTTP e HTTPS na comunicação web?")
        print()
        print("1 - Para escolher a cor e o formato dos botões da tela.")
        print("2 - Para transformar o nome de um site em endereço real.")
        print("3 - Para organizar a conversa entre cliente e servidor, sendo HTTPS a versão protegida.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "3":
            print("Eloisa confirma.")
            print('"Isso. HTTP organiza a conversa."')
            print('"HTTPS faz essa mesma conversa acontecer com proteção."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print("Eloisa reancora.")
            print('"Cores e botões pertencem à parte visual, ao frontend."')
            print('"HTTP e HTTPS não cuidam da aparência."')
            print('"Eles cuidam da conversa entre cliente e servidor."')
        elif escolha == "2":
            print("Eloisa reancora.")
            print('"Transformar nome em endereço é papel do DNS."')
            print('"HTTP e HTTPS entram depois, quando cliente e servidor já precisam conversar."')
            print()
            print('"Tenta de novo pensando na língua da conversa."')
        else:
            print("Eloisa inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



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
    while True:
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
        print("Pergunta de domínio:")
        print("O que o backend faz dentro de um sistema?")
        print()
        print("1 - Desenha os botões, cores e textos que aparecem na tela.")
        print("2 - Recebe pedidos, aplica regras e prepara respostas para a tela.")
        print("3 - Guarda todos os dados permanentes sem precisar de banco.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "2":
            print("David confirma com a cabeça.")
            print('"Isso. Agora cravou."')
            print('"O backend é o motor invisível do sistema."')
            print('"Ele recebe pedidos, aplica regras e prepara respostas para a tela."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print("David aponta para a tela.")
            print('"Essa opção fala do frontend."')
            print('"O frontend cuida da parte visível: botões, cores, textos e telas."')
            print()
            print('"Pensa assim: o frontend é o painel que o usuário toca."')
            print('"O backend é o motor que trabalha quando esse toque vira um pedido."')
            print()
            print('"Tenta de novo pensando no motor invisível."')
        elif escolha == "3":
            print("David aponta para a despensa do sistema.")
            print('"Essa opção mistura backend com banco de dados."')
            print('"Guardar dados permanentes é papel do banco."')
            print()
            print('"O backend pode pedir dados ao banco, mas ele não é a despensa."')
            print('"Ele é quem recebe o pedido, aplica regras e prepara a resposta."')
            print()
            print('"Tenta de novo pensando em quem processa o pedido."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_servidor_web():
    while True:
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
        print("Pergunta de domínio:")
        print("Qual é o papel do servidor web em um sistema online?")
        print()
        print("1 - Receber pedidos vindos da internet e devolver respostas.")
        print("2 - Escolher as cores, fontes e botões que aparecem na tela.")
        print("3 - Guardar permanentemente todos os dados da empresa.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("David confirma.")
            print('"Isso. O servidor web é a porta de entrada dos pedidos na internet."')
            print('"Ele fica esperando requisições chegarem e devolve respostas para clientes, navegadores ou aplicativos."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("David aponta para a interface.")
            print('"Essa opção fala da aparência da tela."')
            print('"Cores, fontes e botões pertencem ao frontend."')
            print('"O servidor web não desenha a tela; ele recebe pedidos que chegam pela internet."')
            print()
            print('"Tenta de novo pensando na porta de entrada do sistema."')
        elif escolha == "3":
            print("David aponta para a despensa do sistema.")
            print('"Guardar dados permanentes é papel do banco de dados."')
            print('"O servidor web pode receber um pedido que depois leva o backend até o banco, mas ele não é o lugar onde tudo fica guardado."')
            print()
            print('"Tenta de novo pensando em quem recebe os pedidos primeiro."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_logica_negocio():
    while True:
        print()
        print("=" * 60)
        print("🧠 TÓPICO 3: LÓGICA DE NEGÓCIO")
        print("=" * 60)
        print("David aparece na tela e olha diretamente para você.")
        print()
        print('"Todo sistema precisa saber quais regras seguir."')
        print()
        print("Lógica de negócio é o conjunto de regras específicas de uma empresa.")
        print("Ela define como o sistema deve agir em cada situação.")
        print()
        print("Exemplo simples:")
        print("- Se o cliente compra acima de um valor, ganha desconto.")
        print("- Se o produto está sem estoque, não pode ser vendido.")
        print("- Se o usuário não tem permissão, não acessa aquela área.")
        print()
        print("Essas regras normalmente vivem no backend,")
        print("porque é ali que o sistema toma decisões importantes.")
        print()
        print("Pergunta de domínio:")
        print("O que é lógica de negócio dentro de um sistema?")
        print()
        print("1 - As regras da empresa transformadas em comportamento do sistema.")
        print("2 - A cor, o tamanho e a posição dos botões na tela.")
        print("3 - O endereço específico de uma API onde um pedido chega.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("David confirma.")
            print('"Isso. Lógica de negócio é a regra real da empresa funcionando dentro do sistema."')
            print('"Quando o sistema calcula desconto, bloqueia venda sem estoque ou limita acesso, ele está aplicando lógica de negócio."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("David aponta para a tela.")
            print('"Essa opção fala da aparência da interface."')
            print('"Cores, tamanhos e posição dos botões são trabalho do frontend."')
            print('"Lógica de negócio é outra coisa: são as regras que decidem o que pode ou não acontecer."')
            print()
            print('"Tenta de novo pensando nas regras da empresa."')
        elif escolha == "3":
            print("David aponta para o caminho da API.")
            print('"Essa opção fala de endpoint."')
            print('"Endpoint é o endereço onde um pedido chega."')
            print('"Lógica de negócio é o que o sistema faz depois que o pedido chega: aplicar regras, validar condições e decidir a resposta."')
            print()
            print('"Tenta de novo pensando na decisão que o sistema precisa tomar."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_api():
    while True:
        print()
        print("=" * 60)
        print("🔌 TÓPICO 4: API")
        print("=" * 60)
        print("David aparece na tela e olha diretamente para você.")
        print()
        print('"O backend não conversa com o mundo de qualquer jeito."')
        print()
        print("API é o canal organizado por onde sistemas conversam.")
        print("Ela define como um pedido deve chegar e como a resposta deve voltar.")
        print()
        print("Pense na API como um balcão:")
        print("- o frontend faz um pedido no balcão;")
        print("- o backend entende o pedido;")
        print("- o backend devolve uma resposta organizada.")
        print()
        print("A API esconde a bagunça interna do sistema.")
        print("Quem usa a API não precisa saber como a cozinha funciona por dentro.")
        print()
        print("Pergunta de domínio:")
        print("Qual é o papel de uma API na comunicação entre frontend e backend?")
        print()
        print("1 - Ser o canal organizado por onde sistemas fazem pedidos e recebem respostas.")
        print("2 - Guardar os dados permanentes da empresa em tabelas.")
        print("3 - Desenhar a aparência visual da tela para o usuário.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("David confirma.")
            print('"Isso. API é o canal organizado da conversa."')
            print('"Ela permite que o frontend peça algo ao backend sem precisar conhecer a bagunça interna do sistema."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("David aponta para a despensa do sistema.")
            print('"Essa opção fala do banco de dados."')
            print('"O banco guarda informações. A API não é onde os dados moram; ela é o caminho organizado para pedir e receber dados."')
            print()
            print('"Tenta de novo pensando no canal de conversa."')
        elif escolha == "3":
            print("David aponta para a tela.")
            print('"Essa opção fala do frontend."')
            print('"A aparência visual pertence à tela. A API trabalha na comunicação entre partes do sistema."')
            print()
            print('"Tenta de novo pensando no balcão onde o pedido passa."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_api_rest():
    while True:
        print()
        print("=" * 60)
        print("🧱 TÓPICO 5: API REST")
        print("=" * 60)
        print("David aparece na tela e olha diretamente para você.")
        print()
        print('"Quando muitos sistemas conversam, eles precisam de um padrão."')
        print()
        print("API REST é um jeito organizado de criar APIs.")
        print("Ela usa endereços e métodos da web para separar recursos e ações.")
        print()
        print("Na prática, cada coisa importante do sistema ganha um caminho.")
        print("Produtos, clientes, pedidos e reservas podem ter seus próprios endereços.")
        print()
        print("Assim, o backend sabe com clareza o que está sendo pedido.")
        print("Buscar, criar, atualizar ou apagar deixam de ser bagunça.")
        print()
        print("Pergunta de domínio:")
        print("Para que serve o padrão REST em uma API?")
        print()
        print("1 - Para organizar os caminhos e ações da API de um jeito previsível.")
        print("2 - Para deixar a tela mais bonita com cores e espaçamentos.")
        print("3 - Para guardar os produtos e clientes dentro do banco de dados.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("David confirma.")
            print('"Isso. REST ajuda a organizar a API."')
            print('"Com ele, recursos como produtos, clientes e pedidos podem ter caminhos claros, e o backend entende melhor o que está sendo pedido."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("David aponta para a interface.")
            print('"Essa opção fala de aparência visual."')
            print('"Cores e espaçamentos são trabalho do frontend."')
            print('"REST organiza a conversa da API, não a aparência da tela."')
            print()
            print('"Tenta de novo pensando na organização dos pedidos."')
        elif escolha == "3":
            print("David aponta para a despensa.")
            print('"Essa opção fala do banco de dados."')
            print('"O banco guarda produtos e clientes."')
            print('"REST não é onde os dados moram; é um padrão para organizar como a API recebe pedidos."')
            print()
            print('"Tenta de novo pensando nos caminhos da API."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_endpoints():
    while True:
        print()
        print("=" * 60)
        print("📍 TÓPICO 6: ENDPOINTS")
        print("=" * 60)
        print("David aparece na tela e olha diretamente para você.")
        print()
        print('"Dentro de uma API, cada serviço precisa ter um endereço claro."')
        print()
        print("Endpoint é um endereço específico dentro de uma API.")
        print("É o lugar onde um pedido chega para buscar ou executar alguma coisa.")
        print()
        print("Exemplos simples:")
        print("- um endpoint para listar produtos;")
        print("- um endpoint para cadastrar cliente;")
        print("- um endpoint para buscar uma reserva.")
        print()
        print("Sem endpoints claros, o frontend não sabe onde pedir")
        print("e o backend não sabe qual parte deve responder.")
        print()
        print("Pergunta de domínio:")
        print("O que é um endpoint dentro de uma API?")
        print()
        print("1 - Um endereço específico onde um pedido chega para buscar ou executar alguma coisa.")
        print("2 - A regra da empresa que decide se uma compra tem desconto.")
        print("3 - O arquivo onde todos os dados ficam guardados permanentemente.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("David confirma.")
            print('"Isso. Endpoint é um endereço específico dentro da API."')
            print('"Ele ajuda o pedido a chegar na parte certa do backend."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("David aponta para as regras do sistema.")
            print('"Essa opção fala de lógica de negócio."')
            print('"Regra de desconto é uma decisão da empresa dentro do sistema."')
            print('"Endpoint é outra coisa: é o endereço por onde o pedido chega."')
            print()
            print('"Tenta de novo pensando no ponto de chegada do pedido."')
        elif escolha == "3":
            print("David aponta para a despensa.")
            print('"Essa opção fala do banco de dados."')
            print('"O banco guarda dados."')
            print('"Endpoint não guarda tudo; ele é um endereço específico da API para receber pedidos."')
            print()
            print('"Tenta de novo pensando em endereço, não em armazenamento."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_rotas():
    while True:
        print()
        print("=" * 60)
        print("🛣️ TÓPICO 7: ROTAS")
        print("=" * 60)
        print("David aparece na tela e olha diretamente para você.")
        print()
        print('"Quando o pedido chega, o backend precisa saber para onde mandar."')
        print()
        print("Rota é o caminho que liga um pedido a uma parte específica do backend.")
        print("Ela ajuda o sistema a decidir qual função deve responder.")
        print()
        print("Exemplo simples:")
        print("- pedido para ver produtos vai para a rota de produtos;")
        print("- pedido para cadastrar cliente vai para a rota de clientes;")
        print("- pedido para buscar reserva vai para a rota de reservas.")
        print()
        print("Sem rotas, o backend receberia pedidos,")
        print("mas não saberia qual parte do sistema deveria agir.")
        print()
        print("Pergunta de domínio:")
        print("Qual é o papel de uma rota dentro do backend?")
        print()
        print("1 - Direcionar o pedido para a parte certa do sistema responder.")
        print("2 - Guardar todos os dados do sistema de forma permanente.")
        print("3 - Definir a cor e o estilo dos botões na tela.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("David confirma.")
            print('"Isso. A rota ajuda o backend a mandar cada pedido para o lugar certo."')
            print('"Sem rota, o pedido chega, mas o sistema não sabe qual parte deve agir."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("David aponta para a despensa.")
            print('"Essa opção fala do banco de dados."')
            print('"Guardar dados permanentes é papel do banco."')
            print('"A rota não guarda dados; ela direciona o pedido para a ação certa."')
            print()
            print('"Tenta de novo pensando no caminho interno do pedido."')
        elif escolha == "3":
            print("David aponta para a tela.")
            print('"Essa opção fala do frontend."')
            print('"Cores e estilo dos botões são parte visual."')
            print('"Rota é uma peça do backend para organizar para onde o pedido vai."')
            print()
            print('"Tenta de novo pensando no caminho que o pedido segue dentro do sistema."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def topico_json():
    while True:
        print()
        print("=" * 60)
        print("📦 TÓPICO 8: JSON")
        print("=" * 60)
        print("David aparece na tela e olha diretamente para você.")
        print()
        print('"Quando o backend responde, ele precisa entregar dados de um jeito organizado."')
        print()
        print("JSON é um formato simples para transportar informações entre sistemas.")
        print("Ele organiza dados em pares de nome e valor.")
        print()
        print("Exemplo de ideia:")
        print("- nome: Teclado Mecânico")
        print("- preço: 249.90")
        print("- estoque: 15")
        print()
        print("O frontend recebe esses dados e consegue montar a tela para o usuário.")
        print("Por isso JSON aparece tanto em APIs.")
        print()
        print("Pergunta de domínio:")
        print("Por que o backend costuma enviar dados em JSON para o frontend?")
        print()
        print("1 - Porque JSON organiza informações em um formato que o frontend consegue entender e usar.")
        print("2 - Porque JSON é uma imagem pronta da tela que o usuário vai ver.")
        print("3 - Porque JSON é o banco de dados onde os produtos ficam guardados para sempre.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("David confirma.")
            print('"Isso. JSON é um formato organizado para transportar dados."')
            print('"Com ele, o backend entrega informações de um jeito que o frontend consegue ler e transformar em tela."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("David aponta para a interface.")
            print('"Essa opção confunde dado com tela pronta."')
            print('"JSON não é uma imagem nem uma tela desenhada."')
            print('"Ele carrega informações organizadas, como nome, preço e estoque."')
            print('"Depois o frontend usa esses dados para montar a tela."')
            print()
            print('"Tenta de novo pensando em dados, não em imagem."')
        elif escolha == "3":
            print("David aponta para a despensa.")
            print('"Essa opção fala do banco de dados."')
            print('"O banco guarda os produtos de forma permanente."')
            print('"JSON não é a despensa; ele é o pacote organizado que transporta os dados na resposta."')
            print()
            print('"Tenta de novo pensando no pacote que viaja entre backend e frontend."')
        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')



def reconhecimento_etapa_2():
    while True:
        print()
        print("=" * 60)
        print("💡 RECONHECIMENTO: O MOTOR OCULTO")
        print("=" * 60)
        print("David organiza os primeiros conceitos do Backend.")
        print()
        print("1 - O que é Backend")
        print("2 - Servidor Web")
        print("3 - Lógica de Negócio")
        print("4 - API")
        print("5 - API REST")
        print("6 - Endpoints")
        print("7 - Rotas")
        print("8 - JSON")
        print("0 - Voltar à etapa 02")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_backend()
        elif escolha == "2":
            topico_servidor_web()
        elif escolha == "3":
            topico_logica_negocio()
        elif escolha == "4":
            topico_api()
        elif escolha == "5":
            topico_api_rest()
        elif escolha == "6":
            topico_endpoints()
        elif escolha == "7":
            topico_rotas()
        elif escolha == "8":
            topico_json()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


def campo_treinamento_etapa_2():
    print()
    print("=" * 60)
    print("🛠 CAMPO DE TREINAMENTO: O PEDIDO ENTRA NO MOTOR")
    print("=" * 60)
    print("David aparece na tela e olha diretamente para você.")
    print()
    print('"Agora vamos seguir um pedido quando ele chega ao backend."')
    print()
    print("Imagine que o jogador abriu uma tela e pediu uma lista de produtos.")
    print()
    print("O caminho dentro do motor começa assim:")
    print()
    print("1. O servidor web recebe o pedido.")
    print("2. A rota identifica para onde esse pedido deve ir.")
    print("3. O endpoint certo é acionado.")
    print("4. O backend aplica as regras necessárias.")
    print("5. Se precisar, o backend busca dados no banco.")
    print("6. O backend organiza a resposta em JSON.")
    print("7. A resposta volta para a tela.")
    print()
    print("Esse é o caminho básico do Motor Oculto.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def laboratorio_falhas_etapa_2():
    print()
    print("=" * 60)
    print("🧪 LABORATÓRIO DE FALHAS: QUANDO O MOTOR ENGASGA")
    print("=" * 60)
    print("David aparece na tela e olha diretamente para você.")
    print()
    print('"Backend também falha. E quando falha, ele deixa pistas."')
    print()
    print("Alguns problemas comuns dentro do Motor Oculto:")
    print()
    print("1. Rota inexistente")
    print("- O pedido chega, mas o backend não encontra o caminho.")
    print()
    print("2. Regra de negócio incorreta")
    print("- O sistema aplica uma regra errada e devolve resultado errado.")
    print()
    print("3. Banco de dados indisponível")
    print("- O backend precisa de dados, mas a despensa não responde.")
    print()
    print("4. Resposta mal formatada")
    print("- O backend responde, mas a tela não consegue entender.")
    print()
    print("Resumo de sobrevivência:")
    print("- Falha no backend não é chute.")
    print("- O dev segue o pedido até descobrir onde o motor engasgou.")
    print("- Cada erro aponta para uma parte do caminho.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def missao_producao_etapa_2():
    print()
    print("=" * 60)
    print("🏢 MISSÃO EM PRODUÇÃO: BACKEND NO DIA A DIA")
    print("=" * 60)
    print("David aparece na tela e olha diretamente para você.")
    print()
    print('"Agora vamos tirar o backend da teoria e olhar para o uso real."')
    print()
    print("Imagine um e-commerce recebendo pedidos de clientes.")
    print()
    print("Quando alguém compra um produto, o backend precisa:")
    print()
    print("1. receber o pedido;")
    print("2. conferir as regras da compra;")
    print("3. verificar informações importantes;")
    print("4. conversar com o banco quando necessário;")
    print("5. preparar uma resposta para a tela.")
    print()
    print("Se uma regra estiver errada, o cliente pode pagar errado.")
    print("Se a resposta vier mal organizada, a tela pode quebrar.")
    print()
    print("Resumo de sobrevivência:")
    print("- Backend aparece em compras, cadastros, login e relatórios.")
    print("- Ele transforma regras reais em respostas do sistema.")
    print("- Quando o backend erra, o impacto chega no usuário.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def registro_etapa_2():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA — MOTOR OCULTO")
    print("=" * 60)
    print("David aparece na tela e olha diretamente para você.")
    print()
    print('"Todo motor entendido deixa um rastro de aprendizado."')
    print()
    print("Nesta etapa, você começou a reconhecer o backend:")
    print()
    print("- entendeu que ele trabalha por trás da tela;")
    print("- viu que ele roda no servidor;")
    print("- conheceu servidor web, regras, API, REST, endpoints, rotas e JSON;")
    print("- caminhou pelo caminho interno de um pedido;")
    print("- viu falhas comuns do Motor Oculto;")
    print("- observou o backend em situações reais de uso.")
    print()
    print("Registro atual:")
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_2():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL — MOTOR OCULTO")
    print("=" * 60)
    print("David aparece na tela e olha diretamente para você.")
    print()
    print('"Antes de seguir, revise o que você encontrou dentro do servidor."')
    print()
    print("Relatório da missão: Explorando o Motor Oculto")
    print()
    print("Você agora sabe que:")
    print()
    print("- backend é a parte invisível que processa pedidos;")
    print("- servidor web recebe requisições e devolve respostas;")
    print("- lógica de negócio guarda regras da empresa;")
    print("- API organiza a conversa entre sistemas;")
    print("- REST ajuda a estruturar APIs;")
    print("- endpoints são endereços específicos;")
    print("- rotas direcionam pedidos para a ação certa;")
    print("- JSON organiza dados para trafegar entre backend e frontend.")
    print()
    print("Conclusão:")
    print("Você começou a entender o motor que trabalha por trás da tela.")
    print()
    print("A etapa ainda não marca conclusão permanente nesta versão.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def prova_dominio_etapa_2():
    tentativas = 0

    while True:
        print()
        print("=" * 60)
        print("🧠 PROVA DE DOMÍNIO — MOTOR OCULTO")
        print("=" * 60)
        print("David aparece na tela e olha diretamente para você.")
        print()
        print("Um cliente abre a tela de produtos e o sistema precisa buscar a lista no backend.")
        print("Qual caminho representa melhor o Motor Oculto trabalhando?")
        print()
        print("1 - A tela acessa o banco diretamente, pega os produtos e monta tudo sozinha.")
        print("2 - O pedido chega ao servidor web, passa pela rota e endpoint corretos, o backend aplica regras, busca dados se precisar, organiza a resposta em JSON e devolve para a tela.")
        print("3 - A API guarda os produtos, escolhe as cores da tela e envia tudo direto para o usuário.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")
        tentativas += 1

        print()

        if escolha == "2":
            print("David confirma.")
            print('"Isso. Agora você conectou as peças."')
            print('"Servidor web, rota, endpoint, backend, regras, banco, JSON e resposta fazem parte do caminho completo."')
            print('"Você não decorou nomes. Você enxergou o motor funcionando."')
            print()
            print("Prova de Domínio concluída nesta versão.")
            print("Ainda não há XP, recompensa ou progresso salvo.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break

        elif escolha == "1":
            print("David aponta para a divisão entre tela e servidor.")
            print('"Essa opção pula o Motor Oculto."')
            print('"A tela não deve entrar direto no banco."')
            print('"Ela faz o pedido. O backend recebe, decide, busca dados se precisar e responde."')
            print()
            print('"Tenta de novo seguindo o caminho completo do pedido."')

        elif escolha == "3":
            print("David levanta a mão com calma.")
            print('"Essa opção mistura papéis."')
            print('"A API não guarda produtos, não escolhe cores e não substitui o backend."')
            print('"Ela organiza a conversa."')
            print()
            print('"Quem guarda é o banco. Quem processa é o backend. Quem mostra a tela é o frontend."')

        else:
            print("David inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')
            tentativas -= 1

        if tentativas >= 3:
            print()
            print("David se aproxima da tela.")
            print('"Vamos fechar juntos."')
            print('"A resposta certa é a opção 2."')
            print()
            print('"Quando a tela precisa de produtos, ela faz um pedido."')
            print('"O servidor web recebe, a rota direciona, o endpoint certo é acionado,"')
            print('"o backend aplica regras, busca dados se precisar, organiza em JSON e devolve a resposta."')
            print()
            print('"Esse é o Motor Oculto trabalhando."')
            print()
            print("A prova segue sem punição nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break




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
            cena_abertura_etapa_2()
        elif escolha == "2":
            reconhecimento_etapa_2()
        elif escolha == "3":
            campo_treinamento_etapa_2()
        elif escolha == "4":
            laboratorio_falhas_etapa_2()
        elif escolha == "5":
            missao_producao_etapa_2()
        elif escolha == "6":
            prova_dominio_etapa_2()
        elif escolha == "7":
            registro_etapa_2()
        elif escolha == "8":
            relatorio_final_etapa_2()
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