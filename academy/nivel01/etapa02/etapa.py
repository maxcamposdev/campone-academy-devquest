"""Etapa 02 — Explorando o Motor Oculto."""

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
