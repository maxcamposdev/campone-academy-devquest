"""Etapa 01 — Decifrando a Grande Rede."""

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
    while True:
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
        print("Pergunta de domínio:")
        print("Qual é o papel do DNS quando você digita o nome de um site?")
        print()
        print("1 - Traduzir um nome fácil, como campone.com, para o endereço real do servidor.")
        print("2 - Proteger senhas e dados pessoais com um cadeado.")
        print("3 - Processar as regras do sistema antes de responder para a tela.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Eloisa valida.")
            print('"Isso. O DNS funciona como a agenda da internet."')
            print('"Ele ajuda o navegador a encontrar onde o servidor mora."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Eloisa reancora.")
            print('"Proteção com cadeado lembra HTTPS."')
            print('"DNS não protege a conversa. Ele ajuda a encontrar o endereço certo."')
            print()
            print('"Tenta de novo pensando na agenda da internet."')
        elif escolha == "3":
            print("Eloisa reancora.")
            print('"Processar regras é papel do backend."')
            print('"O DNS não decide regra de sistema. Ele traduz nome em endereço."')
            print()
            print('"Tenta de novo pensando em encontrar o servidor."')
        else:
            print("Eloisa inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_endereco_ip():
    while True:
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
        print("Pergunta de domínio:")
        print("O que é um endereço IP na Grande Rede?")
        print()
        print("1 - O nome fácil que uma pessoa digita no navegador.")
        print("2 - O endereço numérico que identifica uma máquina ou servidor na rede.")
        print("3 - A senha usada para entrar em um sistema.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "2":
            print("Eloisa confirma.")
            print('"Isso. O IP é o endereço real da máquina na rede."')
            print('"Sem ele, o pedido não sabe para onde viajar."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print("Eloisa reancora.")
            print('"O nome fácil é o domínio, como campone.com."')
            print('"O IP é o endereço numérico que as máquinas usam."')
            print()
            print('"Tenta de novo separando nome fácil e endereço real."')
        elif escolha == "3":
            print("Eloisa reancora.")
            print('"Senha é assunto de login e segurança."')
            print('"IP não é senha. IP é endereço."')
            print()
            print('"Tenta de novo pensando no destino do pedido."')
        else:
            print("Eloisa inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_requisicao_http():
    while True:
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
        print("Pergunta de domínio:")
        print("O que é uma requisição HTTP?")
        print()
        print("1 - Um arquivo onde o sistema guarda dados para sempre.")
        print("2 - Uma imagem pronta que aparece na tela do usuário.")
        print("3 - Um pedido que sai do cliente para o servidor.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "3":
            print("Eloisa valida.")
            print('"Exato. Requisição é o pedido."')
            print('"Ela sai do cliente, viaja pela internet e chega ao servidor."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print("Eloisa reancora.")
            print('"Guardar dados para sempre lembra banco de dados."')
            print('"Requisição não é armazenamento. É movimento."')
            print('"É o pedido saindo de um lado para chegar ao outro."')
        elif escolha == "2":
            print("Eloisa reancora.")
            print('"A imagem na tela é o resultado visual."')
            print('"A requisição acontece antes: é o pedido que busca ou envia informações."')
            print()
            print('"Tenta de novo pensando no pedido que sai da tela."')
        else:
            print("Eloisa inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


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
