from engine.telas import tela_boas_vindas
from jogador.perfil import criar_jogador, mostrar_status
from engine.mapa import mostrar_mapa, mostrar_etapas_nivel_1
from academy.nivel01.etapa01.etapa import entrar_etapa_1
from academy.nivel01.etapa02.etapa import entrar_etapa_2
from academy.nivel01.etapa03.etapa import entrar_etapa_3
from academy.nivel01.etapa04.etapa import entrar_etapa_4




































































































































































def topico_frontend_etapa_5():
    while True:
        print()
        print("=" * 60)
        print('🖥️ TÓPICO 1: O QUE É FRONTEND')
        print("=" * 60)
        print('Frontend é a parte do sistema que o usuário vê e usa.')
        print()
        print('É a tela, os botões, os textos, as imagens, os campos e as interações.')
        print()
        print('Irlene aparece na tela e olha diretamente para você.')
        print()
        print('"Se o backend trabalha por trás, o frontend olha para o usuário."')
        print('"Ele precisa ser claro, organizado e fácil de usar."')
        print()
        print('Ideia de sobrevivência:')
        print('frontend é a frente visível do sistema.')
        print()
        print("PERGUNTA:")
        print('O que melhor descreve o frontend em um sistema?')
        print()
        print('1 - A parte escondida que processa regras e conversa com o banco de dados.')
        print('2 - A parte que o usuário vê, toca e usa: telas, botões, textos, campos e interações.')
        print('3 - O lugar onde os dados ficam guardados de forma organizada.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Irlene confirma.')
            print('"Isso. Frontend é a parte visível do sistema."')
            print('"É onde o usuário encontra a experiência de uso."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Irlene reancora com calma.')
            print('"Quase. Essa descrição combina mais com o backend, que trabalha por trás."')
            print('"Frontend é a parte visível, aquela que o usuário realmente usa na tela."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Irlene aponta para a separação das partes.')
            print('"Boa tentativa. Guardar dados é papel do banco de dados."')
            print('"Frontend é a frente visível do sistema, onde a pessoa lê, clica e interage."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_html_etapa_5():
    while True:
        print()
        print("=" * 60)
        print('🏗️ TÓPICO 2: HTML — ESTRUTURA DA PÁGINA')
        print("=" * 60)
        print('Antes de uma tela ficar bonita ou interativa, ela precisa existir.')
        print()
        print('O HTML organiza o que aparece na página:')
        print('títulos, textos, imagens, botões, links e campos.')
        print()
        print('Irlene aponta para uma tela simples.')
        print()
        print('"Pensa assim: primeiro a página precisa dizer o que existe nela."')
        print('"Depois outras partes cuidam da aparência e do comportamento."')
        print()
        print('Ideia de sobrevivência:')
        print('HTML define a estrutura do que existe na tela.')
        print()
        print("PERGUNTA:")
        print('Antes de uma tela ganhar cor, estilo ou reação,')
        print('ela precisa dizer o que existe nela. Qual peça faz esse papel?')
        print()
        print('1 - CSS, porque ele decide as cores e os espaços da tela.')
        print('2 - JavaScript, porque ele faz a tela reagir aos cliques.')
        print('3 - HTML, porque ele organiza a estrutura: títulos, textos, imagens, botões e campos.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Irlene confirma.')
            print('"Isso. HTML é a estrutura."')
            print('"Ele diz quais peças existem na página."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Irlene reancora com calma.')
            print('"Quase. CSS cuida da aparência visual."')
            print('"Mas antes de pintar ou organizar visualmente, a tela precisa ter estrutura."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Irlene aponta para a ordem das peças.')
            print('"Boa tentativa. JavaScript entra quando a tela precisa reagir."')
            print('"Mas primeiro a tela precisa saber quais peças existem nela."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_css_etapa_5():
    while True:
        print()
        print("=" * 60)
        print('🎨 TÓPICO 3: CSS — APARÊNCIA VISUAL')
        print("=" * 60)
        print('Depois que a estrutura existe, a tela precisa ganhar forma visual.')
        print()
        print('O CSS cuida da aparência:')
        print('cores, tamanhos, espaçamentos, fontes e organização visual.')
        print()
        print('Irlene mostra a mesma tela com e sem estilo.')
        print()
        print('"Sem aparência, a informação até existe, mas fica difícil de usar."')
        print('"Com estilo, a tela ganha clareza, identidade e conforto."')
        print()
        print('Ideia de sobrevivência:')
        print('CSS dá forma visual ao que o HTML colocou na tela.')
        print()
        print("PERGUNTA:")
        print('Uma tela tem título, imagem, botão e campo,')
        print('mas está sem cor, sem espaçamento e difícil de ler.')
        print('Qual peça provavelmente está faltando ou falhando?')
        print()
        print('1 - CSS, porque ele cuida da aparência visual e da organização da tela.')
        print('2 - HTML, porque ele apaga todos os dados quando a tela fica sem cor.')
        print('3 - Banco de Dados, porque cor e espaçamento ficam guardados em tabelas.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Irlene confirma.')
            print('"Isso. CSS dá forma visual ao que já existe na tela."')
            print('"Ele ajuda a tela ficar clara, organizada e confortável."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Irlene reancora com calma.')
            print('"Quase. HTML ajuda a estrutura existir."')
            print('"Se tudo aparece, mas está feio ou desorganizado, a estrutura provavelmente está lá."')
            print('"O problema aponta mais para a aparência."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Irlene aponta para a diferença entre dados e visual.')
            print('"Boa tentativa. Banco de dados guarda informações."')
            print('"Cor, espaçamento e organização visual pertencem à interface, não à despensa dos dados."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_javascript_etapa_5():
    while True:
        print()
        print("=" * 60)
        print('⚡ TÓPICO 4: JAVASCRIPT — COMPORTAMENTO DA TELA')
        print("=" * 60)
        print('Uma tela não precisa apenas aparecer.')
        print('Ela também precisa reagir ao usuário.')
        print()
        print('JavaScript entra quando algo precisa acontecer:')
        print('clicar, abrir, fechar, validar, mudar ou responder sem recarregar tudo.')
        print()
        print('Irlene toca em um botão da tela.')
        print()
        print('"Quando a tela reage ao seu clique, existe comportamento acontecendo."')
        print('"Essa é a parte viva da interface."')
        print()
        print('Ideia de sobrevivência:')
        print('JavaScript faz a tela reagir.')
        print()
        print("PERGUNTA:")
        print('A tela aparece bonita, mas o botão não responde quando o usuário clica.')
        print('Qual peça é a principal suspeita?')
        print()
        print('1 - CSS, porque ele sempre cria todas as reações da tela.')
        print('2 - JavaScript, porque ele adiciona comportamento e faz a tela reagir.')
        print('3 - HTML, porque ele guarda a senha do usuário.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Irlene confirma.')
            print('"Isso. JavaScript é a parte que faz a tela reagir."')
            print('"Ele transforma uma tela parada em uma interface viva."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Irlene reancora com calma.')
            print('"Quase. CSS cuida da aparência."')
            print('"Se a tela está bonita, mas nada reage, o problema não parece estar na pintura da tela."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Irlene aponta para a função de cada peça.')
            print('"Boa tentativa. HTML organiza o que existe na página."')
            print('"Mas reação ao clique é comportamento."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_dom_etapa_5():
    while True:
        print()
        print("=" * 60)
        print('🧩 TÓPICO 5: DOM — MAPA VIVO DA PÁGINA')
        print("=" * 60)
        print('Para mudar uma parte da tela, o sistema precisa encontrar essa parte.')
        print()
        print('O DOM é como um mapa vivo da página.')
        print('Ele permite que a tela encontre um botão, um texto, uma imagem ou um campo específico.')
        print()
        print('Irlene aponta para vários botões parecidos.')
        print()
        print('"Se existem dez botões, a tela precisa saber exatamente qual foi clicado."')
        print('"O DOM ajuda a encontrar a peça certa."')
        print()
        print('Ideia de sobrevivência:')
        print('DOM é o mapa que permite mexer em partes específicas da tela.')
        print()
        print("PERGUNTA:")
        print('Se existem dez botões parecidos na tela,')
        print('como o sistema consegue mexer só no botão que foi clicado?')
        print()
        print('1 - Ele muda todos os botões ao mesmo tempo, porque não consegue saber qual foi clicado.')
        print('2 - Ele pede ao banco de dados para escolher um botão aleatório.')
        print('3 - Ele usa o DOM como um mapa vivo da página para encontrar a peça certa.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Irlene confirma.')
            print('"Isso. O DOM funciona como um mapa vivo da página."')
            print('"Ele ajuda a encontrar e alterar uma parte específica da tela."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Irlene reancora com calma.')
            print('"Quase. Se a tela mudasse tudo ao mesmo tempo, a experiência ficaria confusa."')
            print('"O sistema precisa localizar a peça certa."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Irlene aponta para a própria página.')
            print('"Boa tentativa. O banco guarda dados, mas não escolhe botão visual na tela."')
            print('"Essa busca pela peça certa acontece dentro da própria página."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_responsividade_etapa_5():
    while True:
        print()
        print("=" * 60)
        print('📱 TÓPICO 6: RESPONSIVIDADE — TELA QUE SE ADAPTA')
        print("=" * 60)
        print('O usuário pode abrir o sistema no computador, tablet ou celular.')
        print()
        print('A tela precisa se reorganizar para continuar fácil de usar.')
        print()
        print('Responsividade é essa capacidade de adaptação.')
        print()
        print('Irlene coloca duas telas lado a lado.')
        print()
        print('"No computador, há mais espaço."')
        print('"No celular, tudo precisa se ajustar sem quebrar."')
        print()
        print('Ideia de sobrevivência:')
        print('uma interface boa se adapta ao tamanho da tela.')
        print()
        print("PERGUNTA:")
        print('Por que uma tela precisa se adaptar ao celular, tablet e computador?')
        print()
        print('1 - Porque a mesma interface precisa continuar clara e fácil de usar em tamanhos diferentes.')
        print('2 - Porque o celular sempre apaga o backend quando abre uma página.')
        print('3 - Porque responsividade serve apenas para trocar a senha do usuário.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Irlene confirma.')
            print('"Isso. Uma boa interface se reorganiza conforme o espaço disponível."')
            print('"Ela precisa funcionar bem no computador e no celular."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Irlene reancora com calma.')
            print('"Quase. O tamanho da tela não apaga o backend."')
            print('"O problema aqui é visual: a interface precisa caber e continuar usável."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Irlene aponta para outro território.')
            print('"Boa tentativa, mas senha e acesso pertencem ao tema de segurança."')
            print('"Responsividade fala sobre adaptação da tela."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_frontend_completo_etapa_5():
    while True:
        print()
        print("=" * 60)
        print('🧠 TÓPICO 7: FRONTEND COMPLETO')
        print("=" * 60)
        print('Agora juntamos as peças da interface visual.')
        print()
        print('HTML coloca a estrutura.')
        print('CSS cuida da aparência.')
        print('JavaScript adiciona comportamento.')
        print('DOM ajuda a encontrar e alterar partes da tela.')
        print('Responsividade faz tudo se adaptar ao dispositivo.')
        print()
        print('Irlene olha diretamente para você.')
        print()
        print('"Frontend não é só deixar bonito."')
        print('"É fazer a tela existir, ser clara, reagir e funcionar bem para quem usa."')
        print()
        print('Ideia de sobrevivência:')
        print('frontend é a experiência visível do sistema funcionando.')
        print()
        print("PERGUNTA:")
        print('Qual conjunto representa melhor uma interface visual funcionando bem?')
        print()
        print('1 - Só cores bonitas, mesmo que nada esteja organizado ou funcionando.')
        print('2 - Estrutura, aparência, comportamento, localização das peças e adaptação ao tamanho da tela.')
        print('3 - Apenas banco de dados e servidor, sem tela para o usuário.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Irlene confirma.')
            print('"Isso. Frontend completo não é só beleza."')
            print('"É a experiência visível funcionando com clareza, reação e adaptação."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Irlene reancora com calma.')
            print('"Quase. Beleza visual ajuda, mas não basta."')
            print('"Uma interface também precisa ter estrutura, reação e adaptação."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Irlene aponta para a experiência do usuário.')
            print('"Boa tentativa. Backend e banco são importantes, mas não substituem a tela."')
            print('"O usuário precisa de uma interface para usar o sistema."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def cena_abertura_etapa_5():
    print()
    print("=" * 60)
    print("🎬 INICIAR MISSÃO: A INTERFACE VISUAL")
    print("=" * 60)
    print("Você retorna ao Centro de Operações da CampOne.")
    print()
    print("Eloisa já tinha mostrado a Grande Rede.")
    print("David abriu o Motor Oculto.")
    print("Letícia organizou a memória do sistema.")
    print("Renato mostrou como a tela conversa com o backend.")
    print()
    print("Agora falta olhar para a própria tela.")
    print()
    print("Irlene aparece na tela e olha diretamente para você.")
    print()
    print('"Olá. Eu sou Irlene."')
    print()
    print('"Minha área é Frontend."')
    print('"Eu cuido da parte do sistema que o usuário vê, toca e usa."')
    print()
    print('"Botões, textos, campos, imagens, organização visual e interação')
    print('não aparecem por acaso."')
    print()
    print('"Uma tela precisa existir, ser clara, reagir e funcionar bem')
    print('em diferentes tamanhos de tela."')
    print()
    print('"Frontend não é só deixar bonito."')
    print('"É transformar o sistema em uma experiência que uma pessoa consegue usar."')
    print()
    print("Nesta etapa, você vai entender:")
    print()
    print("- o que é frontend;")
    print("- como a estrutura da página nasce;")
    print("- como a aparência visual é organizada;")
    print("- como a tela reage ao usuário;")
    print("- como a página encontra partes específicas para mudar;")
    print("- por que a interface precisa se adaptar ao celular, tablet e computador;")
    print("- e como tudo isso forma a experiência visual do sistema.")
    print()
    print("Irlene aponta para uma tela da CampOne.")
    print()
    print('"Antes de aprender a construir telas na prática,')
    print('você precisa entender o papel de cada peça."')
    print()
    print('"Sem decorar código."')
    print('"Sem sintaxe disfarçada."')
    print('"Primeiro a ideia. Depois a ferramenta."')
    print("=" * 60)

    input("Pressione Enter para voltar...")

def reconhecimento_etapa_5():
    while True:
        print()
        print("=" * 60)
        print("💡 RECONHECIMENTO: A INTERFACE VISUAL")
        print("=" * 60)
        print("Irlene organiza os primeiros conceitos de Frontend.")
        print()
        print("1 - O que é Frontend")
        print("2 - HTML — estrutura da página")
        print("3 - CSS — aparência visual")
        print("4 - JavaScript — comportamento da tela")
        print("5 - DOM — mapa vivo da página")
        print("6 - Responsividade — tela que se adapta")
        print("7 - Frontend completo")
        print("0 - Voltar à etapa 05")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_frontend_etapa_5()
        elif escolha == "2":
            topico_html_etapa_5()
        elif escolha == "3":
            topico_css_etapa_5()
        elif escolha == "4":
            topico_javascript_etapa_5()
        elif escolha == "5":
            topico_dom_etapa_5()
        elif escolha == "6":
            topico_responsividade_etapa_5()
        elif escolha == "7":
            topico_frontend_completo_etapa_5()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


def campo_treinamento_etapa_5():
    print()
    print("=" * 60)
    print("🛠️ CAMPO DE TREINAMENTO: A TELA POR DENTRO")
    print("=" * 60)
    print("Agora vamos olhar uma tela da CampOne por dentro.")
    print()
    print("Cena:")
    print("O aplicativo mostra uma página simples de produtos.")
    print()
    print("Na tela existem:")
    print("- um título;")
    print("- uma imagem;")
    print("- uma lista de produtos;")
    print("- um botão de detalhes;")
    print("- um campo de busca.")
    print()
    print("-" * 60)
    print("1. HTML — O QUE EXISTE")
    print("-" * 60)
    print("Primeiro, a tela precisa dizer quais peças existem.")
    print()
    print("O HTML marca a estrutura:")
    print("existe um título, existe uma imagem, existe um botão, existe um campo.")
    print()
    print("Sem estrutura, a página nem sabe o que precisa mostrar.")
    print()
    print("-" * 60)
    print("2. CSS — COMO APARECE")
    print("-" * 60)
    print("Depois, essas peças precisam ficar organizadas e legíveis.")
    print()
    print("O CSS cuida da aparência:")
    print("cores, tamanhos, fontes, espaços e posição dos elementos.")
    print()
    print("Sem aparência bem cuidada, a informação até aparece,")
    print("mas pode ficar confusa ou difícil de usar.")
    print()
    print("-" * 60)
    print("3. JAVASCRIPT — COMO REAGE")
    print("-" * 60)
    print("Agora imagine que o usuário toca no botão de detalhes.")
    print()
    print("A tela precisa reagir.")
    print("Pode abrir uma informação, mostrar um aviso ou atualizar uma parte da página.")
    print()
    print("JavaScript é a parte que dá comportamento para a interface.")
    print()
    print("-" * 60)
    print("4. DOM — COMO ENCONTRA A PEÇA CERTA")
    print("-" * 60)
    print("Se existem muitos botões na tela,")
    print("o sistema precisa saber exatamente qual botão foi tocado.")
    print()
    print("O DOM funciona como um mapa vivo da página.")
    print("Ele ajuda a encontrar a peça certa para mudar só aquilo que precisa mudar.")
    print()
    print("-" * 60)
    print("5. RESPONSIVIDADE — COMO SE ADAPTA")
    print("-" * 60)
    print("A mesma tela pode abrir no computador, no tablet ou no celular.")
    print()
    print("A interface precisa se reorganizar para continuar fácil de usar.")
    print()
    print("Responsividade é isso:")
    print("a tela se adapta ao tamanho do dispositivo sem perder clareza.")
    print()
    print("-" * 60)
    print("RESUMO DA TELA POR DENTRO")
    print("-" * 60)
    print("HTML cria a estrutura.")
    print("CSS organiza a aparência.")
    print("JavaScript faz reagir.")
    print("DOM ajuda a encontrar a peça certa.")
    print("Responsividade adapta a tela ao dispositivo.")
    print()
    print("Ideia de sobrevivência:")
    print("frontend é a experiência visível do sistema funcionando para uma pessoa.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def laboratorio_falhas_etapa_5():
    print()
    print("=" * 60)
    print("🧪 LABORATÓRIO DE FALHAS: O PLANTÃO DA INTERFACE")
    print("=" * 60)
    print("Irlene aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos olhar alguns problemas comuns em uma interface visual.")
    print()
    print("A ideia não é sair corrigindo tudo no escuro.")
    print("A ideia é olhar o sintoma e suspeitar da peça certa.")
    print()
    print("-" * 60)
    print("CHAMADO 1 — TELA SEM ESTILO")
    print("-" * 60)
    print("O usuário abriu o app.")
    print("Tudo aparece na tela, mas está sem cor, sem espaçamento e tudo empilhado.")
    print()
    print("Suspeita principal:")
    print("CSS.")
    print()
    print("Por quê?")
    print("A estrutura existe, então o HTML provavelmente apareceu.")
    print("Mas a aparência visual não chegou direito.")
    print()
    print("-" * 60)
    print("CHAMADO 2 — TELA BONITA, MAS NADA REAGE")
    print("-" * 60)
    print("A tela aparece bonita.")
    print("Os botões estão no lugar.")
    print("Mas quando o usuário clica, nada acontece.")
    print()
    print("Suspeita principal:")
    print("JavaScript.")
    print()
    print("Por quê?")
    print("A aparência está presente, mas o comportamento não está funcionando.")
    print("A tela virou quase uma imagem parada.")
    print()
    print("-" * 60)
    print("CHAMADO 3 — TELA QUEBRADA NO CELULAR")
    print("-" * 60)
    print("No computador, a tela está boa.")
    print("No celular, tudo fica apertado, sobreposto ou difícil de tocar.")
    print()
    print("Suspeita principal:")
    print("Responsividade.")
    print()
    print("Por quê?")
    print("A interface não está se adaptando bem ao tamanho da tela.")
    print()
    print("-" * 60)
    print("CHAMADO 4 — ERRO 500")
    print("-" * 60)
    print("O app nem mostra a tela esperada.")
    print("Aparece uma mensagem de erro 500.")
    print()
    print("Suspeita principal:")
    print("backend ou servidor.")
    print()
    print("Por quê?")
    print("Erro 500 aponta para problema interno do servidor.")
    print("Nesse caso, a falha provavelmente não nasceu na interface visual.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("Problema visual nem sempre é do mesmo lugar.")
    print()
    print("Se tudo existe, mas está feio: olhe para o CSS.")
    print("Se está bonito, mas não reage: olhe para o JavaScript.")
    print("Se quebra no celular: olhe para a responsividade.")
    print("Se aparece erro 500: talvez o problema esteja fora do frontend.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def missao_producao_etapa_5():
    print()
    print("=" * 60)
    print("🏢 MISSÃO EM PRODUÇÃO: A INTERFACE NO MUNDO REAL")
    print("=" * 60)
    print("Irlene aparece na tela e olha diretamente para você.")
    print()
    print("Agora a interface visual sai do treinamento e entra no mundo real.")
    print()
    print("Imagine uma tela de catálogo da CampOne.")
    print()
    print("O usuário abre o sistema e vê:")
    print()
    print("- o nome da página;")
    print("- cards de produtos;")
    print("- imagens;")
    print("- preços;")
    print("- botão de detalhes;")
    print("- campo de busca;")
    print("- layout adaptado ao tamanho da tela.")
    print()
    print("-" * 60)
    print("O QUE O HTML FAZ")
    print("-" * 60)
    print("O HTML define as peças que existem nessa tela.")
    print()
    print("Ele diz que existe um título,")
    print("que existem imagens,")
    print("que existem botões,")
    print("que existe um campo de busca")
    print("e que existem áreas para mostrar produtos.")
    print()
    print("-" * 60)
    print("O QUE O CSS FAZ")
    print("-" * 60)
    print("O CSS organiza a aparência dessas peças.")
    print()
    print("Ele cuida das cores, fontes, tamanhos, espaços e alinhamento.")
    print()
    print("É o que faz a tela parecer uma interface da CampOne,")
    print("e não um monte de informação jogada na página.")
    print()
    print("-" * 60)
    print("O QUE O JAVASCRIPT FAZ")
    print("-" * 60)
    print("Quando o usuário clica em detalhes,")
    print("digita no campo de busca")
    print("ou interage com um botão,")
    print("a tela precisa reagir.")
    print()
    print("JavaScript é a parte que faz a interface responder às ações do usuário.")
    print()
    print("-" * 60)
    print("O QUE O DOM AJUDA A FAZER")
    print("-" * 60)
    print("Se existem vários produtos na tela,")
    print("o sistema precisa encontrar exatamente qual card, botão ou texto deve mudar.")
    print()
    print("O DOM ajuda a localizar a peça certa dentro da página.")
    print()
    print("-" * 60)
    print("O QUE A RESPONSIVIDADE RESOLVE")
    print("-" * 60)
    print("A mesma tela pode abrir no computador, no tablet ou no celular.")
    print()
    print("No computador há mais espaço.")
    print("No celular, os elementos precisam se reorganizar.")
    print()
    print("Responsividade mantém a tela usável em tamanhos diferentes.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("Em produção, Frontend não é só aparência.")
    print()
    print("É a soma de estrutura, visual, comportamento, localização das peças")
    print("e adaptação para diferentes telas.")
    print()
    print("Uma boa interface ajuda a pessoa a entender, clicar, ler e agir sem se perder.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def prova_dominio_etapa_5():
    while True:
        print()
        print("=" * 60)
        print("✅ PROVA DE DOMÍNIO: A INTERFACE VISUAL")
        print("=" * 60)
        print("Irlene aparece na tela e olha diretamente para você.")
        print()
        print('"Agora vamos juntar os sintomas de uma interface real."')
        print()
        print("Um usuário abre uma tela de produtos.")
        print("Tudo aparece, mas está sem estilo.")
        print("Depois, em outra tela, tudo está bonito, mas os botões não reagem.")
        print("Em um celular, a tela fica apertada e difícil de usar.")
        print()
        print("PERGUNTA:")
        print("Qual leitura mostra melhor o diagnóstico?")
        print()
        print("1 - Todos os problemas são do banco de dados, porque a tela sempre depende só dele.")
        print("2 - Todos os problemas são do backend, porque frontend não tem responsabilidade sobre a experiência visual.")
        print("3 - A tela sem estilo aponta para CSS; a tela que não reage aponta para JavaScript; a tela ruim no celular aponta para responsividade.")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "3":
            print()
            print("Irlene confirma.")
            print('"Isso. Você leu os sintomas como dev:"')
            print('"aparência aponta para CSS,"')
            print('"reação aponta para JavaScript,"')
            print('"e tela ruim no celular aponta para responsividade."')
            print()
            print("A interface visual está dominada na teoria.")
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print()
            print("Irlene reancora com calma.")
            print('"Quase. O banco guarda informações, mas os sintomas citados são visuais e de interação."')
            print('"Eles apontam primeiro para a interface."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == "2":
            print()
            print("Irlene aponta para a responsabilidade do frontend.")
            print('"Boa tentativa. Backend é importante, mas frontend tem responsabilidade pela experiência visível."')
            print('"Aparência, reação e adaptação são sinais da interface."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def registro_etapa_5():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA — A INTERFACE VISUAL")
    print("=" * 60)
    print("Irlene aparece na tela e olha diretamente para você.")
    print()
    print('"Vamos registrar o que você enxergou por trás da tela."')
    print()
    print("Você reconheceu que:")
    print()
    print("- frontend é a parte visível do sistema;")
    print("- HTML define a estrutura do que existe na tela;")
    print("- CSS organiza a aparência visual;")
    print("- JavaScript faz a tela reagir;")
    print("- DOM ajuda a encontrar a peça certa da página;")
    print("- responsividade adapta a interface para diferentes tamanhos de tela;")
    print("- frontend completo não é só beleza;")
    print("- uma boa interface precisa ser clara, útil, reativa e adaptável.")
    print()
    print("Irlene confirma:")
    print()
    print('"Isso ainda não é programação prática."')
    print('"É visão de interface."')
    print()
    print('"Você agora entende a tela antes de aprender a construí-la com ferramentas profissionais."')
    print()
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_5():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL — A INTERFACE VISUAL")
    print("=" * 60)
    print("Irlene aparece na tela e olha diretamente para você.")
    print()
    print('"Antes de seguir, revise a interface inteira."')
    print()
    print("Relatório da missão: Forjando a Interface Visual")
    print()
    print("Você agora sabe que:")
    print()
    print("- frontend é a experiência visível do sistema;")
    print("- a tela precisa existir antes de ficar bonita ou interativa;")
    print("- HTML organiza a estrutura da página;")
    print("- CSS cuida da aparência, organização visual e adaptação;")
    print("- JavaScript adiciona comportamento e reação;")
    print("- DOM funciona como um mapa vivo da página;")
    print("- responsividade mantém a tela usável em computador, tablet e celular;")
    print("- problemas visuais podem ter causas diferentes;")
    print("- uma boa interface ajuda a pessoa a entender, clicar, ler e agir sem se perder.")
    print()
    print("Conclusão:")
    print()
    print("Você começou a enxergar que uma tela não é só decoração.")
    print()
    print("Ela é uma parte essencial do sistema.")
    print("É onde o usuário encontra o produto, entende o caminho e toma ações.")
    print()
    print("A etapa ainda não marca conclusão permanente nesta versão.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def entrar_etapa_5():
    while True:
        print()
        print("=" * 60)
        print("05. FORJANDO A INTERFACE VISUAL")
        print("=" * 60)
        print("Tema real: Frontend")
        print("Tipo: Treinamento de Sobrevivência")
        print("Status: Estrutura inicial")
        print("Mentora prevista: Irlene")
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
            cena_abertura_etapa_5()
        elif escolha == "2":
            reconhecimento_etapa_5()
        elif escolha == "3":
            campo_treinamento_etapa_5()
        elif escolha == "4":
            laboratorio_falhas_etapa_5()
        elif escolha == "5":
            missao_producao_etapa_5()
        elif escolha == "6":
            prova_dominio_etapa_5()
        elif escolha == "7":
            registro_etapa_5()
        elif escolha == "8":
            relatorio_final_etapa_5()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")



def topico_login_etapa_6():
    while True:
        print()
        print("=" * 60)
        print('🔐 TÓPICO 1: LOGIN')
        print("=" * 60)
        print('Um sistema sério precisa saber quem está tentando entrar.')
        print()
        print('Login é o momento em que a pessoa se apresenta ao sistema.')
        print()
        print('Débora aparece na tela e olha diretamente para você.')
        print()
        print('"Pensa na entrada de um prédio."')
        print('"Antes de liberar a catraca, alguém precisa saber quem você é."')
        print()
        print('Ideia de sobrevivência:')
        print('login é o começo da identificação do usuário.')
        print()
        print("PERGUNTA:")
        print('Quando uma pessoa abre um app e informa quem ela é para tentar entrar,')
        print('qual ideia está começando ali?')
        print()
        print('1 - Autorização, porque o sistema já decidiu tudo que ela pode fazer.')
        print('2 - Login, porque a pessoa está se apresentando ao sistema.')
        print('3 - Banco de dados, porque a tela está criando uma tabela nova.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Débora confirma.')
            print('"Isso. Login é o momento em que a pessoa se apresenta ao sistema."')
            print('"É o começo da portaria digital."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Débora reancora com calma.')
            print('"Quase. Autorização vem depois, quando o sistema decide o que a pessoa pode acessar."')
            print('"Antes disso, a pessoa precisa começar se apresentando."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Débora aponta para a entrada.')
            print('"Boa tentativa. Banco de dados guarda informações, mas login não é criar tabela."')
            print('"Login é o começo da entrada da pessoa no sistema."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_autenticacao_etapa_6():
    while True:
        print()
        print("=" * 60)
        print('🪪 TÓPICO 2: AUTENTICAÇÃO')
        print("=" * 60)
        print('Não basta dizer quem você é.')
        print('O sistema precisa conferir se aquilo é verdade.')
        print()
        print('Autenticação é essa conferência.')
        print()
        print('Pode acontecer com senha, digital, código no celular ou outro tipo de prova.')
        print()
        print('Débora aponta para uma lista de entrada.')
        print()
        print('"Dizer o nome é uma coisa."')
        print('"Provar que é você é outra."')
        print()
        print('Ideia de sobrevivência:')
        print('autenticação responde: quem é você?')
        print()
        print("PERGUNTA:")
        print('Depois que a pessoa informa quem diz ser, o que a autenticação faz?')
        print()
        print('1 - Escolhe as cores da tela de login.')
        print('2 - Decide se a pessoa pode acessar todas as áreas internas.')
        print('3 - Confere se a prova apresentada combina com a identidade da pessoa.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Débora confirma.')
            print('"Isso. Autenticação é a conferência da identidade."')
            print('"Ela responde: quem é você?"')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Débora reancora com calma.')
            print('"Quase. Cores e aparência pertencem à interface visual."')
            print('"Autenticação não cuida da aparência; ela confere identidade."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Débora separa as perguntas da portaria.')
            print('"Boa tentativa. Decidir o que a pessoa pode acessar é autorização."')
            print('"Autenticação responde primeiro: essa pessoa é quem diz ser?"')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_autorizacao_etapa_6():
    while True:
        print()
        print("=" * 60)
        print('🚪 TÓPICO 3: AUTORIZAÇÃO')
        print("=" * 60)
        print('Entrar no sistema não significa poder mexer em tudo.')
        print()
        print('Autorização define o que a pessoa pode acessar ou fazer.')
        print()
        print('Um cliente pode ver o próprio pedido.')
        print('Um funcionário pode ver ferramentas internas.')
        print('Um administrador pode ter mais permissões.')
        print()
        print('Débora aponta para portas diferentes dentro da CampOne.')
        print()
        print('"Depois de saber quem você é, o sistema pergunta: o que você pode?"')
        print()
        print('Ideia de sobrevivência:')
        print('autorização responde: o que você pode fazer?')
        print()
        print("PERGUNTA:")
        print('Uma pessoa conseguiu entrar no sistema, mas não pode abrir a área financeira.')
        print('Qual peça explica melhor isso?')
        print()
        print('1 - Autorização, porque ela define o que a pessoa pode acessar ou fazer.')
        print('2 - Login, porque entrar sempre libera todas as áreas.')
        print('3 - CSS, porque área financeira bloqueada é problema de aparência.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Débora confirma.')
            print('"Isso. Autorização define o que a pessoa pode fazer depois que entra."')
            print('"Passar pela porta não significa abrir todas as salas."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Débora reancora com calma.')
            print('"Quase. Entrar no sistema não significa poder mexer em tudo."')
            print('"Depois da entrada, o sistema ainda verifica permissões."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Débora aponta para outra área.')
            print('"Boa tentativa, mas CSS cuida da aparência visual."')
            print('"Área restrita é assunto de permissão, não de cor ou layout."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_cookies_etapa_6():
    while True:
        print()
        print("=" * 60)
        print('🍪 TÓPICO 4: COOKIES')
        print("=" * 60)
        print('A web tem um problema:')
        print('cada pedido pode chegar como se fosse a primeira visita.')
        print()
        print('Cookies ajudam o navegador a guardar pequenas informações.')
        print()
        print('No contexto de login, eles podem ajudar o sistema a lembrar')
        print('que aquela pessoa já passou por uma identificação.')
        print()
        print('Débora mostra uma pulseira de entrada.')
        print()
        print('"Depois que você entra, não precisa mostrar documento a cada porta."')
        print('"Mas existe um lembrete acompanhando você."')
        print()
        print('Ideia de sobrevivência:')
        print('cookie é um pequeno lembrete guardado pelo navegador.')
        print()
        print("PERGUNTA:")
        print('Por que cookies podem ajudar depois que a pessoa entra em um sistema?')
        print()
        print('1 - Porque cookies substituem toda segurança e deixam qualquer pessoa entrar.')
        print('2 - Porque podem guardar pequenos lembretes no navegador, ajudando o sistema a reconhecer uma visita.')
        print('3 - Porque cookies apagam automaticamente todas as senhas do usuário.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Débora confirma.')
            print('"Isso. Cookie pode funcionar como um lembrete guardado pelo navegador."')
            print('"Ele ajuda o sistema a reconhecer algumas informações entre pedidos."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Débora reancora com calma.')
            print('"Quase. Cookie não substitui toda a segurança."')
            print('"Ele pode ajudar como lembrete, mas o sistema ainda precisa de regras de proteção."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Débora aponta para a função do lembrete.')
            print('"Boa tentativa, mas cookie não é uma borracha de senha."')
            print('"Aqui a ideia é guardar um pequeno lembrete no navegador."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_sessao_etapa_6():
    while True:
        print()
        print("=" * 60)
        print('⏳ TÓPICO 5: SESSÃO')
        print("=" * 60)
        print('Depois que a pessoa entra, o sistema mantém esse acesso por um tempo.')
        print()
        print('Esse período é a sessão.')
        print()
        print('Sessão não deve durar para sempre.')
        print('Ela pode expirar por segurança, principalmente em sistemas sensíveis.')
        print()
        print('Débora olha diretamente para você.')
        print()
        print('"Se alguém pega seu celular desbloqueado, uma sessão eterna vira perigo."')
        print()
        print('Ideia de sobrevivência:')
        print('sessão é o tempo em que o sistema continua reconhecendo você.')
        print()
        print("PERGUNTA:")
        print('Por que uma sessão não deve durar para sempre?')
        print()
        print('1 - Porque toda sessão serve para mudar a cor da tela.')
        print('2 - Porque sessão eterna deixa o banco de dados sem tabelas.')
        print('3 - Porque manter acesso aberto para sempre pode colocar a conta em risco.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Débora confirma.')
            print('"Isso. Sessão precisa ter limite."')
            print('"Se o acesso ficasse aberto para sempre, outra pessoa poderia aproveitar isso."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Débora reancora com calma.')
            print('"Quase. Cor da tela é assunto de interface."')
            print('"Sessão fala sobre o tempo em que o sistema continua reconhecendo a pessoa."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Débora aponta para o risco real.')
            print('"Boa tentativa, mas sessão não apaga tabelas do banco."')
            print('"O ponto aqui é segurança do acesso."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_token_etapa_6():
    while True:
        print()
        print("=" * 60)
        print('🎟️ TÓPICO 6: TOKEN')
        print("=" * 60)
        print('Depois de entrar, o sistema pode entregar uma prova temporária.')
        print()
        print('Essa prova acompanha os próximos pedidos.')
        print()
        print('Token é como um crachá digital temporário.')
        print('Ele ajuda o sistema a reconhecer que aquele pedido vem de alguém já conferido.')
        print()
        print('Débora mostra um crachá com validade.')
        print()
        print('"O crachá ajuda na passagem, mas não deve valer para sempre."')
        print()
        print('Ideia de sobrevivência:')
        print('token é uma prova temporária usada para reconhecer pedidos.')
        print()
        print("PERGUNTA:")
        print('Depois que a pessoa já foi conferida,')
        print('por que um token pode acompanhar os próximos pedidos?')
        print()
        print('1 - Porque funciona como uma prova temporária de que aquele pedido vem de alguém já reconhecido.')
        print('2 - Porque token é uma imagem decorativa que aparece no botão de login.')
        print('3 - Porque token substitui todas as permissões e libera tudo para qualquer pessoa.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Débora confirma.')
            print('"Isso. Token funciona como um crachá digital temporário."')
            print('"Ele ajuda o sistema a reconhecer pedidos depois do login."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Débora reancora com calma.')
            print('"Quase. Imagem decorativa é assunto de interface visual."')
            print('"Token não é decoração; é uma prova temporária usada nos pedidos."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Débora aponta para os limites da portaria.')
            print('"Boa tentativa, mas token não deve liberar tudo para qualquer pessoa."')
            print('"Ele ajuda a reconhecer pedidos, mas o sistema ainda precisa respeitar permissões."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_seguranca_completa_etapa_6():
    while True:
        print()
        print("=" * 60)
        print('🛡️ TÓPICO 7: SEGURANÇA COMPLETA')
        print("=" * 60)
        print('Agora juntamos as peças da portaria digital.')
        print()
        print('Login inicia a entrada.')
        print('Autenticação confere quem é a pessoa.')
        print('Autorização define o que ela pode fazer.')
        print('Cookies podem guardar pequenos lembretes no navegador.')
        print('Sessão mantém o reconhecimento por um tempo.')
        print('Token pode funcionar como uma prova temporária nos pedidos.')
        print()
        print('Débora cruza os braços com calma.')
        print()
        print('"Segurança não é impedir tudo."')
        print('"É deixar a pessoa certa entrar, pelo tempo certo, no lugar certo."')
        print()
        print('Ideia de sobrevivência:')
        print('segurança organiza identidade, permissão e tempo de acesso.')
        print()
        print("PERGUNTA:")
        print('Qual frase resume melhor a portaria digital de um sistema?')
        print()
        print('1 - Segurança é impedir todo mundo de entrar, mesmo quem tem permissão.')
        print('2 - Segurança é deixar a pessoa certa entrar, pelo tempo certo, no lugar certo.')
        print('3 - Segurança é trocar cores da tela e aumentar o tamanho dos botões.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Débora confirma.')
            print('"Isso. Segurança é equilíbrio."')
            print('"A pessoa certa, no lugar certo, pelo tempo certo."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Débora reancora com calma.')
            print('"Quase. Segurança não é travar tudo."')
            print('"Ela precisa proteger sem impedir a pessoa certa de usar o sistema."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Débora aponta para outro território.')
            print('"Boa tentativa, mas cores e botões pertencem à interface visual."')
            print('"Segurança organiza identidade, permissão e tempo de acesso."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def cena_abertura_etapa_6():
    print()
    print("=" * 60)
    print("🎬 INICIAR MISSÃO: A PORTARIA DIGITAL")
    print("=" * 60)
    print("Você chega à entrada da CampOne.")
    print()
    print("Depois de atravessar a Grande Rede,")
    print("entender o Motor Oculto,")
    print("organizar a memória do sistema,")
    print("cruzar a ponte entre tela e backend")
    print("e enxergar a interface visual,")
    print("uma nova pergunta aparece:")
    print()
    print("quem pode entrar no sistema?")
    print("e o que essa pessoa pode fazer depois que entra?")
    print()
    print("Débora aparece na tela e olha diretamente para você.")
    print()
    print('"Olá. Eu sou Débora."')
    print()
    print('"Minha área é Login e Segurança."')
    print('"Eu cuido da portaria digital da CampOne."')
    print()
    print('"Todo sistema sério precisa fazer duas perguntas:"')
    print()
    print('"Quem é você?"')
    print('"E o que você pode acessar?"')
    print()
    print("Débora aponta para uma catraca digital.")
    print()
    print('"Login, autenticação, autorização, sessão, cookies e tokens"')
    print('"não são palavras para decorar."')
    print()
    print('"São partes de uma mesma ideia:"')
    print('"deixar a pessoa certa entrar, pelo tempo certo, no lugar certo."')
    print()
    print("Nesta etapa, você vai entender:")
    print()
    print("- por que sistemas pedem login;")
    print("- como o sistema confirma quem é a pessoa;")
    print("- por que entrar não significa poder fazer tudo;")
    print("- como o navegador pode guardar pequenos lembretes;")
    print("- por que uma sessão não deve durar para sempre;")
    print("- como uma prova temporária pode acompanhar os pedidos;")
    print("- e por que segurança também é cuidado com o usuário.")
    print()
    print("Débora conclui:")
    print()
    print('"Segurança não é travar tudo."')
    print('"É proteger o caminho sem impedir a pessoa certa de trabalhar."')
    print()
    print('"Sem sintaxe disfarçada."')
    print('"Primeiro você entende a portaria."')
    print('"Depois, no mundo prático, aprende a operar as ferramentas."')
    print("=" * 60)

    input("Pressione Enter para voltar...")

def reconhecimento_etapa_6():
    while True:
        print()
        print("=" * 60)
        print("💡 RECONHECIMENTO: A PORTARIA DIGITAL")
        print("=" * 60)
        print("Débora organiza os primeiros conceitos de Login e Segurança.")
        print()
        print("1 - Login")
        print("2 - Autenticação")
        print("3 - Autorização")
        print("4 - Cookies")
        print("5 - Sessão")
        print("6 - Token")
        print("7 - Segurança completa")
        print("0 - Voltar à etapa 06")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_login_etapa_6()
        elif escolha == "2":
            topico_autenticacao_etapa_6()
        elif escolha == "3":
            topico_autorizacao_etapa_6()
        elif escolha == "4":
            topico_cookies_etapa_6()
        elif escolha == "5":
            topico_sessao_etapa_6()
        elif escolha == "6":
            topico_token_etapa_6()
        elif escolha == "7":
            topico_seguranca_completa_etapa_6()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


def campo_treinamento_etapa_6():
    print()
    print("=" * 60)
    print("🛠️ CAMPO DE TREINAMENTO: O CAMINHO DO LOGIN")
    print("=" * 60)
    print("Débora aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos acompanhar uma entrada segura por dentro do sistema.")
    print()
    print("Cena:")
    print("Uma pessoa abre o app da CampOne e tenta entrar na própria conta.")
    print()
    print("-" * 60)
    print("1. A PESSOA SE APRESENTA")
    print("-" * 60)
    print("A pessoa informa quem ela diz ser.")
    print()
    print("No mundo real, isso pode ser e-mail, senha, digital, código no celular")
    print("ou outra forma de identificação.")
    print()
    print("Ideia:")
    print("o sistema precisa saber quem está tentando entrar.")
    print()
    print("-" * 60)
    print("2. O SISTEMA CONFERE")
    print("-" * 60)
    print("Não basta a pessoa dizer quem é.")
    print("O sistema precisa conferir se a prova combina.")
    print()
    print("Essa conferência é a autenticação.")
    print()
    print("Ideia:")
    print("autenticação responde: quem é você?")
    print()
    print("-" * 60)
    print("3. O SISTEMA LIBERA OU RECUSA")
    print("-" * 60)
    print("Se a prova não confere, a entrada é recusada.")
    print()
    print("Se confere, a pessoa entra.")
    print()
    print("Mas entrar não significa poder mexer em tudo.")
    print()
    print("-" * 60)
    print("4. O SISTEMA VERIFICA PERMISSÕES")
    print("-" * 60)
    print("Depois de reconhecer a pessoa, o sistema olha o que ela pode fazer.")
    print()
    print("Um cliente pode ver a própria conta.")
    print("Um funcionário pode ver ferramentas internas.")
    print("Um administrador pode ter mais acesso.")
    print()
    print("Essa parte é a autorização.")
    print()
    print("Ideia:")
    print("autorização responde: o que você pode fazer?")
    print()
    print("-" * 60)
    print("5. O SISTEMA LEMBRA POR UM TEMPO")
    print("-" * 60)
    print("Depois da entrada, o sistema pode manter a pessoa reconhecida por um período.")
    print()
    print("Esse período é a sessão.")
    print()
    print("Ela existe para a pessoa não precisar provar quem é a cada clique.")
    print("Mas ela não deve durar para sempre.")
    print()
    print("-" * 60)
    print("6. OS PRÓXIMOS PEDIDOS LEVAM UMA PROVA")
    print("-" * 60)
    print("Enquanto a sessão está válida, os próximos pedidos podem levar uma prova temporária.")
    print()
    print("Essa prova ajuda o sistema a reconhecer que o pedido vem de alguém já conferido.")
    print()
    print("Essa ideia aparece no token.")
    print()
    print("-" * 60)
    print("RESUMO DO CAMINHO")
    print("-" * 60)
    print("A pessoa tenta entrar.")
    print("O sistema confere quem ela é.")
    print("O sistema verifica o que ela pode fazer.")
    print("O acesso vale por um tempo.")
    print("Os pedidos seguintes carregam uma prova temporária.")
    print()
    print("Ideia de sobrevivência:")
    print("segurança é deixar a pessoa certa entrar, pelo tempo certo, no lugar certo.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def laboratorio_falhas_etapa_6():
    print()
    print("=" * 60)
    print("🧪 LABORATÓRIO DE FALHAS: OCORRÊNCIAS DA PORTARIA")
    print("=" * 60)
    print("Débora aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos olhar ocorrências comuns de segurança.")
    print()
    print("A ideia não é chamar tudo de erro.")
    print("Às vezes, a portaria está apenas fazendo o trabalho dela.")
    print()
    print("-" * 60)
    print("OCORRÊNCIA 1 — SENHA ERRADA")
    print("-" * 60)
    print("Uma pessoa tenta entrar no app e digita a senha errada.")
    print()
    print("O sistema recusa a entrada.")
    print()
    print("Peça em jogo:")
    print("autenticação.")
    print()
    print("Por quê?")
    print("O sistema está conferindo se a pessoa é mesmo quem diz ser.")
    print("Se a prova não confere, a entrada não deve ser liberada.")
    print()
    print("Diagnóstico:")
    print("não é bug por padrão; é a portaria funcionando.")
    print()
    print("-" * 60)
    print("OCORRÊNCIA 2 — SESSÃO EXPIRADA")
    print("-" * 60)
    print("A pessoa entrou de manhã, usou o app e voltou horas depois.")
    print("O app pediu login novamente.")
    print()
    print("Peça em jogo:")
    print("sessão.")
    print()
    print("Por quê?")
    print("O reconhecimento da pessoa não deve durar para sempre.")
    print("Em sistemas sensíveis, expirar a sessão protege o usuário.")
    print()
    print("Diagnóstico:")
    print("não é bug por padrão; é uma regra de segurança.")
    print()
    print("-" * 60)
    print("OCORRÊNCIA 3 — ÁREA RESTRITA")
    print("-" * 60)
    print("Um funcionário consegue entrar no sistema,")
    print("mas não consegue acessar o módulo financeiro.")
    print()
    print("Peça em jogo:")
    print("autorização.")
    print()
    print("Por quê?")
    print("Ele provou quem é, mas talvez não tenha permissão para aquela área.")
    print()
    print("Diagnóstico:")
    print("não é bug por padrão; pode ser a permissão funcionando corretamente.")
    print()
    print("-" * 60)
    print("OCORRÊNCIA 4 — PEDIDO SEM CRACHÁ")
    print("-" * 60)
    print("Um pedido chega ao backend pedindo dados protegidos,")
    print("mas não traz nenhuma prova temporária de quem está pedindo.")
    print()
    print("Peça em jogo:")
    print("token ou sessão ausente.")
    print()
    print("Por quê?")
    print("O sistema não deve entregar dados protegidos sem reconhecer a pessoa.")
    print()
    print("Diagnóstico:")
    print("a resposta pode ser uma recusa de segurança, como falta de identificação.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("Nem toda recusa é defeito.")
    print()
    print("Às vezes, segurança é justamente dizer:")
    print("não posso liberar isso sem saber quem você é,")
    print("sem saber o que você pode fazer,")
    print("ou depois que seu acesso expirou.")
    print()
    print("Uma boa portaria protege sem virar bagunça.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def missao_producao_etapa_6():
    print()
    print("=" * 60)
    print("🏢 MISSÃO EM PRODUÇÃO: SEGURANÇA NO APP REAL")
    print("=" * 60)
    print("Débora aparece na tela e olha diretamente para você.")
    print()
    print("Agora a portaria digital sai do treinamento e entra em produção.")
    print()
    print("Imagine o app da CampOne sendo usado por três pessoas:")
    print()
    print("- um cliente;")
    print("- um funcionário;")
    print("- uma pessoa administradora.")
    print()
    print("Todas podem entrar no sistema,")
    print("mas cada uma deve enxergar e fazer coisas diferentes.")
    print()
    print("-" * 60)
    print("CENA 1 — CLIENTE ENTRANDO")
    print("-" * 60)
    print("O cliente abre o app e informa suas credenciais.")
    print()
    print("O sistema confere quem ele é.")
    print()
    print("Se a prova estiver correta, o cliente entra.")
    print()
    print("Depois disso, ele pode ver a própria conta,")
    print("os próprios pedidos")
    print("e informações liberadas para ele.")
    print()
    print("Ideia:")
    print("autenticação confirma quem é a pessoa.")
    print()
    print("-" * 60)
    print("CENA 2 — FUNCIONÁRIO COM ACESSO LIMITADO")
    print("-" * 60)
    print("Um funcionário entra no sistema.")
    print()
    print("Ele consegue abrir o painel de atendimento,")
    print("mas não consegue abrir uma área financeira restrita.")
    print()
    print("Isso não precisa ser bug.")
    print()
    print("Pode ser autorização funcionando.")
    print()
    print("Ideia:")
    print("entrar no sistema não significa poder mexer em tudo.")
    print()
    print("-" * 60)
    print("CENA 3 — SESSÃO EXPIRADA")
    print("-" * 60)
    print("Uma pessoa fica muito tempo sem usar o app.")
    print()
    print("Quando volta, o sistema pede login novamente.")
    print()
    print("Isso pode incomodar,")
    print("mas protege a conta se outra pessoa pegar o dispositivo.")
    print()
    print("Ideia:")
    print("sessão tem prazo por segurança.")
    print()
    print("-" * 60)
    print("CENA 4 — PEDIDO PROTEGIDO")
    print("-" * 60)
    print("A tela tenta pedir dados protegidos ao backend.")
    print()
    print("Esse pedido precisa levar alguma prova de que a pessoa já foi conferida.")
    print()
    print("Se essa prova não aparece,")
    print("o sistema não deve entregar os dados.")
    print()
    print("Ideia:")
    print("token ou sessão ajudam a reconhecer pedidos depois do login.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("Em produção, segurança não é só uma tela de login.")
    print()
    print("É um conjunto de cuidados:")
    print("confirmar identidade,")
    print("respeitar permissões,")
    print("limitar o tempo de acesso")
    print("e proteger pedidos sensíveis.")
    print()
    print("A portaria digital existe para proteger pessoas, dados e sistemas.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def prova_dominio_etapa_6():
    while True:
        print()
        print("=" * 60)
        print("✅ PROVA DE DOMÍNIO: A PORTARIA DIGITAL")
        print("=" * 60)
        print("Débora aparece na tela e olha diretamente para você.")
        print()
        print('"Agora vamos juntar a portaria inteira em uma cena só."')
        print()
        print("Uma pessoa entra no app,")
        print("prova quem é,")
        print("recebe acesso por um tempo,")
        print("tenta abrir uma área restrita")
        print("e depois faz pedidos protegidos ao backend.")
        print()
        print("PERGUNTA:")
        print("Qual leitura mostra melhor o que está acontecendo?")
        print()
        print("1 - A tela está apenas mudando de cor, então tudo é problema de CSS.")
        print("2 - O banco de dados está aparecendo direto para o usuário e decidindo todos os acessos sozinho.")
        print("3 - O sistema autentica a pessoa, verifica permissões, mantém uma sessão por tempo limitado e usa uma prova temporária nos pedidos protegidos.")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "3":
            print()
            print("Débora confirma.")
            print('"Isso. Você juntou a portaria inteira:"')
            print('"identidade, permissão, tempo de acesso e prova temporária nos pedidos."')
            print()
            print("A base teórica de Login e Segurança está dominada.")
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print()
            print("Débora reancora com calma.")
            print('"Quase. Cor e aparência pertencem ao frontend."')
            print('"Aqui estamos falando de entrada, permissão e proteção de pedidos."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == "2":
            print()
            print("Débora aponta para a portaria digital.")
            print('"Boa tentativa. O banco guarda dados, mas não deve decidir sozinho o acesso direto do usuário."')
            print('"A portaria digital organiza quem entra, o que pode e por quanto tempo."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def registro_etapa_6():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA — A PORTARIA DIGITAL")
    print("=" * 60)
    print("Débora aparece na tela e olha diretamente para você.")
    print()
    print("Vamos registrar o que você entendeu sobre os escudos de defesa.")
    print()
    print("Você reconheceu que:")
    print()
    print("- login é o começo da entrada no sistema;")
    print("- autenticação confirma quem a pessoa é;")
    print("- autorização define o que a pessoa pode fazer;")
    print("- cookies podem guardar pequenos lembretes no navegador;")
    print("- sessão mantém o reconhecimento por um tempo limitado;")
    print("- token pode funcionar como uma prova temporária nos pedidos;")
    print("- nem toda recusa é defeito;")
    print("- segurança protege pessoas, dados e sistemas.")
    print()
    print("Débora confirma:")
    print("Isso ainda não é programação prática.")
    print("É visão de segurança.")
    print()
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_6():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL — A PORTARIA DIGITAL")
    print("=" * 60)
    print("Débora aparece na tela e olha diretamente para você.")
    print()
    print("Relatório da missão: Erguendo os Escudos de Defesa")
    print()
    print("Você agora sabe que:")
    print()
    print("- todo sistema sério precisa saber quem está tentando entrar;")
    print("- login inicia a entrada;")
    print("- autenticação confere identidade;")
    print("- autorização controla permissões;")
    print("- cookies podem guardar pequenos lembretes no navegador;")
    print("- sessão limita o tempo de reconhecimento;")
    print("- token pode acompanhar pedidos protegidos;")
    print("- segurança não é travar tudo;")
    print("- segurança é permitir a pessoa certa, no lugar certo, pelo tempo certo.")
    print()
    print("Conclusão:")
    print()
    print("Login não é só uma tela com senha.")
    print("É uma portaria digital.")
    print("Ela protege o caminho entre pessoa, sistema, dados e permissões.")
    print()
    print("A etapa ainda não marca conclusão permanente nesta versão.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def entrar_etapa_6():
    while True:
        print()
        print("=" * 60)
        print("06. ERGUENDO OS ESCUDOS DE DEFESA")
        print("=" * 60)
        print("Tema real: Login e Segurança")
        print("Tipo: Treinamento de Sobrevivência")
        print("Status: Estrutura inicial")
        print("Mentora prevista: Débora")
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
            cena_abertura_etapa_6()
        elif escolha == "2":
            reconhecimento_etapa_6()
        elif escolha == "3":
            campo_treinamento_etapa_6()
        elif escolha == "4":
            laboratorio_falhas_etapa_6()
        elif escolha == "5":
            missao_producao_etapa_6()
        elif escolha == "6":
            prova_dominio_etapa_6()
        elif escolha == "7":
            registro_etapa_6()
        elif escolha == "8":
            relatorio_final_etapa_6()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")



def topico_git_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('📘 TÓPICO 1: GIT')
        print("=" * 60)
        print('Git é como um caderno de mudanças do projeto.')
        print()
        print('Ele registra o que mudou, quando mudou e ajuda a voltar no histórico.')
        print()
        print('Richard aparece na tela e olha diretamente para você.')
        print()
        print('"Antes do Git, muita gente salvava versões no improviso:"')
        print('"arquivo final, final mesmo, final corrigido."')
        print()
        print('"Git nasceu para transformar bagunça em histórico organizado."')
        print()
        print('Ideia de sobrevivência:')
        print('Git guarda a história das mudanças do projeto.')
        print()
        print("PERGUNTA:")
        print('Por que o Git ajuda um projeto a não virar uma bagunça de arquivos')
        print('final, final2 e agora vai?')
        print()
        print('1 - Porque ele escolhe automaticamente qual tela do sistema fica mais bonita.')
        print('2 - Porque ele guarda a história das mudanças do projeto de forma organizada.')
        print('3 - Porque ele substitui o backend e o banco de dados.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Richard confirma.')
            print('"Isso. Git é o caderno da história do projeto."')
            print('"Ele ajuda o time a saber o que mudou, quando mudou e por quê."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Aparência da tela é outro assunto."')
            print('"Git não escolhe visual. Ele cuida da história das mudanças."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Richard aponta para a função do caderno.')
            print('"Boa tentativa, mas Git não substitui backend nem banco."')
            print('"Ele registra a evolução do projeto para o time entender o caminho."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_commit_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('📸 TÓPICO 2: COMMIT')
        print("=" * 60)
        print('Commit é como uma fotografia de um momento do projeto.')
        print()
        print('Quando algo importante muda, o dev registra essa mudança.')
        print()
        print('Esse registro ajuda o time a entender o que foi feito e por quê.')
        print()
        print('Richard aponta para uma linha do tempo.')
        print()
        print('"Um commit não é só salvar."')
        print('"É deixar uma marca compreensível na história do projeto."')
        print()
        print('Ideia de sobrevivência:')
        print('commit registra uma mudança com sentido.')
        print()
        print("PERGUNTA:")
        print('Quando uma parte importante do projeto muda, por que o commit é útil?')
        print()
        print('1 - Porque ele registra uma mudança com sentido dentro da história do projeto.')
        print('2 - Porque ele apaga automaticamente todas as versões antigas sem perguntar.')
        print('3 - Porque ele muda a senha de todos os usuários do sistema.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Richard confirma.')
            print('"Isso. Commit é uma fotografia com sentido."')
            print('"Ele deixa uma marca clara do que mudou no projeto."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Commit não é uma borracha automática."')
            print('"Ele registra uma fotografia da mudança para o histórico continuar compreensível."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Richard separa os territórios.')
            print('"Boa tentativa, mas senha e acesso pertencem ao tema de segurança."')
            print('"Commit fala sobre registrar mudanças no projeto."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_branch_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('🌿 TÓPICO 3: BRANCH')
        print("=" * 60)
        print('Às vezes o time precisa trabalhar sem mexer direto na versão principal.')
        print()
        print('Branch é uma linha separada de trabalho.')
        print()
        print('Ela permite testar, criar e ajustar sem colocar tudo em risco de imediato.')
        print()
        print('Richard desenha uma linha principal e uma linha lateral.')
        print()
        print('"A branch cria espaço para trabalhar com segurança."')
        print('"Depois, se fizer sentido, o trabalho volta para a linha principal."')
        print()
        print('Ideia de sobrevivência:')
        print('branch permite trabalhar sem bagunçar a versão principal.')
        print()
        print("PERGUNTA:")
        print('Por que uma branch ajuda quando alguém quer trabalhar sem mexer direto na versão principal?')
        print()
        print('1 - Porque branch é uma tela visual que substitui o frontend.')
        print('2 - Porque branch apaga a linha principal para começar tudo de novo.')
        print('3 - Porque branch cria uma linha separada de trabalho para testar e desenvolver com mais segurança.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Richard confirma.')
            print('"Isso. Branch cria um espaço de trabalho separado."')
            print('"Assim o time pode testar ideias sem bagunçar a linha principal."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Branch não é uma tela."')
            print('"Ela é uma linha de trabalho dentro da história do projeto."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Richard aponta para a linha principal.')
            print('"Boa tentativa, mas branch não serve para apagar a linha principal."')
            print('"Ela ajuda a trabalhar separado sem colocar a versão principal em risco."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_merge_conflito_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('🔀 TÓPICO 4: MERGE E CONFLITO')
        print("=" * 60)
        print('Depois de trabalhar em uma branch, chega a hora de juntar mudanças.')
        print()
        print('Merge é o ato de juntar uma linha de trabalho com outra.')
        print()
        print('Mas se duas pessoas mexeram no mesmo ponto, o Git pode parar e avisar.')
        print()
        print('Esse aviso é um conflito.')
        print()
        print('Richard levanta a mão com calma.')
        print()
        print('"Conflito não significa que alguém errou."')
        print('"Significa que o Git precisa de uma decisão humana."')
        print()
        print('Ideia de sobrevivência:')
        print('merge junta mudanças; conflito pede escolha cuidadosa.')
        print()
        print("PERGUNTA:")
        print('Quando duas mudanças precisam ser juntadas, mas mexeram no mesmo ponto,')
        print('o que o conflito indica?')
        print()
        print('1 - Que o projeto deve ser apagado e recomeçado do zero.')
        print('2 - Que o Git precisa de uma decisão humana para resolver aquela parte.')
        print('3 - Que o banco de dados escolheu sozinho qual versão fica.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Richard confirma.')
            print('"Isso. Conflito não significa que alguém errou."')
            print('"Significa que o Git parou para o time decidir com segurança."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Conflito não é fim do projeto."')
            print('"É um aviso de que aquela parte precisa ser analisada com cuidado."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Richard aponta para o time.')
            print('"Boa tentativa, mas banco de dados não resolve conflito de código."')
            print('"Quem decide como juntar mudanças é o time."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_github_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('☁️ TÓPICO 5: GITHUB')
        print("=" * 60)
        print('Git guarda a história do projeto.')
        print('Mas o time também precisa compartilhar essa história.')
        print()
        print('GitHub é um lugar na internet onde o repositório pode ficar guardado.')
        print()
        print('Ele ajuda o time a colaborar, revisar e acessar o projeto de outros lugares.')
        print()
        print('Richard aponta para um repositório online.')
        print()
        print('"Git é o caderno."')
        print('"GitHub é o lugar onde esse caderno pode ficar disponível para o time."')
        print()
        print('Ideia de sobrevivência:')
        print('GitHub ajuda o time a compartilhar e colaborar no projeto.')
        print()
        print("PERGUNTA:")
        print('Se Git é o caderno da história do projeto, qual é o papel do GitHub?')
        print()
        print('1 - Ajudar o time a guardar, compartilhar e colaborar nesse caderno pela internet.')
        print('2 - Escolher sozinho quais pessoas podem entrar no sistema da empresa.')
        print('3 - Criar automaticamente o layout visual das telas.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Richard confirma.')
            print('"Isso. GitHub é onde o caderno do projeto pode ficar disponível para o time."')
            print('"Ele ajuda na colaboração, revisão e acesso ao histórico."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Permissão de acesso ao sistema pertence ao tema de segurança."')
            print('"GitHub ajuda o time a colaborar no projeto."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Richard separa ferramenta de colaboração e tela.')
            print('"Boa tentativa, mas layout visual pertence ao frontend."')
            print('"GitHub não desenha tela. Ele ajuda a compartilhar o repositório."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_clone_push_pull_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('🔁 TÓPICO 6: CLONE, PUSH E PULL')
        print("=" * 60)
        print('Quando o projeto está em um repositório online, o time precisa trocar mudanças.')
        print()
        print('Clone é pegar uma cópia do projeto pela primeira vez.')
        print('Push é empurrar suas mudanças para o repositório online.')
        print('Pull é puxar as mudanças que outras pessoas enviaram.')
        print()
        print('Richard mostra o caminho de ida e volta.')
        print()
        print('"Clone acontece quando você traz o projeto para sua máquina."')
        print('"Push envia sua parte."')
        print('"Pull atualiza sua cópia com o que o time fez."')
        print()
        print('Ideia de sobrevivência:')
        print('clone traz, push envia, pull atualiza.')
        print()
        print("PERGUNTA:")
        print('Qual leitura combina melhor com clone, push e pull no trabalho em equipe?')
        print()
        print('1 - Clone apaga o projeto, push troca as cores e pull muda a senha.')
        print('2 - Clone cria uma tela nova, push abre o banco e pull fecha o servidor.')
        print('3 - Clone traz uma cópia, push envia suas mudanças e pull atualiza sua cópia com o que o time enviou.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Richard confirma.')
            print('"Isso. Clone traz, push envia e pull atualiza."')
            print('"São movimentos de ida e volta do caderno do time."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Esses termos não falam de cor, senha ou apagar projeto."')
            print('"Eles falam de trazer, enviar e atualizar trabalho."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Richard aponta para o movimento do projeto.')
            print('"Boa tentativa, mas isso mistura várias áreas."')
            print('"Clone, push e pull são movimentos do projeto entre sua máquina e o repositório."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_historico_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('🕰️ TÓPICO 7: HISTÓRICO DO PROJETO')
        print("=" * 60)
        print('Um projeto real cresce com muitas mudanças.')
        print()
        print('O histórico mostra como ele evoluiu.')
        print()
        print('Ele ajuda a descobrir quando algo nasceu, quando algo quebrou')
        print('e quem participou de cada mudança.')
        print()
        print('Richard abre uma linha do tempo.')
        print()
        print('"O histórico é uma memória organizada do trabalho do time."')
        print('"Sem ele, todo problema vira adivinhação."')
        print()
        print('Ideia de sobrevivência:')
        print('histórico ajuda a investigar e entender a evolução do projeto.')
        print()
        print("PERGUNTA:")
        print('Quando aparece um bug que talvez tenha começado semanas atrás,')
        print('por que o histórico do projeto ajuda?')
        print()
        print('1 - Porque ele muda automaticamente o design da tela.')
        print('2 - Porque ele mostra a sequência de mudanças e ajuda a investigar quando algo nasceu ou quebrou.')
        print('3 - Porque ele impede qualquer pessoa de trabalhar no projeto.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Richard confirma.')
            print('"Isso. Histórico evita adivinhação."')
            print('"Ele mostra o caminho que o projeto percorreu até chegar ao estado atual."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Design da tela é tema de frontend."')
            print('"Histórico ajuda a investigar a evolução do projeto."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Richard aponta para o rastro do trabalho.')
            print('"Boa tentativa, mas histórico não existe para impedir trabalho."')
            print('"Ele existe para deixar rastros claros do que aconteceu."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_git_github_time_etapa_7():
    while True:
        print()
        print("=" * 60)
        print('🤝 TÓPICO 8: GIT E GITHUB NO TIME')
        print("=" * 60)
        print('Git e GitHub não existem só para guardar código.')
        print()
        print('Eles ajudam pessoas a trabalharem juntas sem se perderem.')
        print()
        print('Cada pessoa pode trabalhar, registrar, enviar, atualizar e revisar.')
        print()
        print('Richard olha diretamente para você.')
        print()
        print('"No trabalho real, não basta fazer alteração."')
        print('"É preciso deixar rastro, conversar com o time e manter o projeto organizado."')
        print()
        print('Ideia de sobrevivência:')
        print('Git e GitHub são ferramentas de colaboração e memória do projeto.')
        print()
        print("PERGUNTA:")
        print('No trabalho real, por que Git e GitHub são importantes para o time?')
        print()
        print('1 - Porque ajudam a registrar, compartilhar, revisar e organizar mudanças do projeto.')
        print('2 - Porque substituem todas as conversas entre pessoas da equipe.')
        print('3 - Porque fazem o sistema entrar automaticamente em produção sem revisão.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Richard confirma.')
            print('"Isso. Git e GitHub ajudam o time a trabalhar com memória e organização."')
            print('"Cada mudança ganha rastro e o projeto fica mais fácil de cuidar."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Richard reancora com calma.')
            print('"Quase. Git e GitHub ajudam a colaboração, mas não substituem conversa."')
            print('"O time ainda precisa tomar decisões e se comunicar."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Richard separa colaboração de publicação.')
            print('"Boa tentativa, mas publicar sistema é outro assunto."')
            print('"Git e GitHub ajudam no histórico e colaboração; deploy vem em outra etapa."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")



def reconhecimento_etapa_7():
    while True:
        print()
        print("=" * 60)
        print("💡 RECONHECIMENTO: O CADERNO DO TIME")
        print("=" * 60)
        print("Richard organiza os primeiros conceitos de Git e GitHub.")
        print()
        print("1 - Git")
        print("2 - Commit")
        print("3 - Branch")
        print("4 - Merge e conflito")
        print("5 - GitHub")
        print("6 - Clone, Push e Pull")
        print("7 - Histórico do projeto")
        print("8 - Git e GitHub no time")
        print("0 - Voltar à etapa 07")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_git_etapa_7()
        elif escolha == "2":
            topico_commit_etapa_7()
        elif escolha == "3":
            topico_branch_etapa_7()
        elif escolha == "4":
            topico_merge_conflito_etapa_7()
        elif escolha == "5":
            topico_github_etapa_7()
        elif escolha == "6":
            topico_clone_push_pull_etapa_7()
        elif escolha == "7":
            topico_historico_etapa_7()
        elif escolha == "8":
            topico_git_github_time_etapa_7()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")

def cena_abertura_etapa_7():
    print()
    print("=" * 60)
    print("🎬 INICIAR MISSÃO: O CADERNO DO TIME")
    print("=" * 60)
    print("Você chega a uma sala com um quadro cheio de linhas e marcas de tempo.")
    print()
    print("Depois de entender a rede, o backend, o banco, a ponte, a interface e a portaria,")
    print("agora falta entender como um time registra a evolução de um projeto.")
    print()
    print("Richard aparece na tela e olha diretamente para você.")
    print()
    print("Olá. Eu sou Richard.")
    print()
    print("Minha área é Git e GitHub.")
    print("Eu ajudo o time a guardar a história do projeto sem se perder.")
    print()
    print("Antes do Git, muita gente salvava arquivos no improviso:")
    print("projeto_final, projeto_final_corrigido, projeto_final_agora_vai.")
    print()
    print("Isso não conta a história de verdade.")
    print()
    print("Git existe para registrar mudanças com ordem, contexto e memória.")
    print()
    print("Nesta etapa, você vai entender:")
    print()
    print("- por que um projeto precisa de histórico;")
    print("- o que é Git;")
    print("- o que é commit;")
    print("- por que branches ajudam a trabalhar com segurança;")
    print("- como mudanças são juntadas;")
    print("- por que conflitos não são necessariamente erro;")
    print("- para que serve o GitHub;")
    print("- e como clone, push e pull fazem o time trabalhar junto.")
    print()
    print("Richard aponta para a linha do tempo.")
    print()
    print("Sem decorar comandos.")
    print("Sem sintaxe disfarçada.")
    print("Primeiro você entende o caderno.")
    print("Depois, no mundo prático, aprende a operar a ferramenta.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def campo_treinamento_etapa_7():
    print()
    print("=" * 60)
    print("🛠️ CAMPO DE TREINAMENTO: LENDO O CADERNO")
    print("=" * 60)
    print("Richard aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos acompanhar como um projeto cresce com histórico.")
    print()
    print("Imagine o app da CampOne nascendo aos poucos.")
    print()
    print("-" * 60)
    print("1. O PROJETO COMEÇA")
    print("-" * 60)
    print("No começo, existe apenas a estrutura básica.")
    print()
    print("O time registra essa primeira fotografia do projeto.")
    print()
    print("Essa fotografia é um commit.")
    print()
    print("-" * 60)
    print("2. UMA FUNCIONALIDADE NASCE")
    print("-" * 60)
    print("Depois, alguém cria uma tela de reservas.")
    print()
    print("Essa mudança também precisa entrar no histórico.")
    print()
    print("O commit ajuda o time a saber o que mudou e por quê.")
    print()
    print("-" * 60)
    print("3. UM PROBLEMA É CORRIGIDO")
    print("-" * 60)
    print("Mais tarde, aparece um erro no cálculo de uma reserva.")
    print()
    print("O time corrige o problema e registra a correção.")
    print()
    print("Sem histórico, seria difícil descobrir quando o problema apareceu.")
    print()
    print("-" * 60)
    print("4. ALGUÉM TRABALHA EM UMA LINHA SEPARADA")
    print("-" * 60)
    print("Para não mexer direto na versão principal, uma pessoa trabalha em uma branch.")
    print()
    print("A branch permite testar uma ideia sem colocar a linha principal em risco.")
    print()
    print("-" * 60)
    print("5. O TIME JUNTA AS MUDANÇAS")
    print("-" * 60)
    print("Quando o trabalho faz sentido, ele pode ser juntado de volta.")
    print()
    print("Essa junção é o merge.")
    print()
    print("Se duas pessoas mexeram no mesmo lugar, pode aparecer conflito.")
    print("Conflito não é drama: é o Git pedindo uma decisão humana.")
    print()
    print("-" * 60)
    print("RESUMO DO TREINAMENTO")
    print("-" * 60)
    print("Git guarda a história.")
    print("Commit registra uma mudança.")
    print("Branch cria uma linha segura de trabalho.")
    print("Merge junta mudanças.")
    print("Conflito pede decisão.")
    print("GitHub ajuda o time a compartilhar o caderno.")
    print()
    print("Ideia de sobrevivência:")
    print("um projeto profissional precisa de memória, não de adivinhação.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def laboratorio_falhas_etapa_7():
    print()
    print("=" * 60)
    print("🧪 LABORATÓRIO DE FALHAS: PROBLEMAS NO CADERNO")
    print("=" * 60)
    print("Richard aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos olhar falhas comuns no trabalho com Git e GitHub.")
    print()
    print("A ideia não é decorar comando.")
    print("A ideia é entender o sintoma e suspeitar da peça certa.")
    print()
    print("-" * 60)
    print("FALHA 1 — MUDANÇA SEM REGISTRO")
    print("-" * 60)
    print("A pessoa alterou o projeto, mas não registrou a mudança.")
    print()
    print("Suspeita:")
    print("faltou commit.")
    print()
    print("Por quê?")
    print("Sem commit, a mudança não vira uma fotografia clara no histórico.")
    print()
    print("-" * 60)
    print("FALHA 2 — TRABALHO FICOU SÓ NO COMPUTADOR")
    print("-" * 60)
    print("A pessoa registrou a mudança, mas o time não consegue ver.")
    print()
    print("Suspeita:")
    print("faltou push.")
    print()
    print("Por quê?")
    print("O commit ficou local, mas ainda não foi enviado para o repositório online.")
    print()
    print("-" * 60)
    print("FALHA 3 — PROJETO LOCAL DESATUALIZADO")
    print("-" * 60)
    print("O time mudou o projeto, mas a pessoa continua trabalhando em uma cópia antiga.")
    print()
    print("Suspeita:")
    print("faltou pull.")
    print()
    print("Por quê?")
    print("A cópia local precisa puxar as mudanças que já foram enviadas pelo time.")
    print()
    print("-" * 60)
    print("FALHA 4 — DUAS PESSOAS MEXERAM NO MESMO PONTO")
    print("-" * 60)
    print("Na hora de juntar mudanças, o Git para e avisa que existe conflito.")
    print()
    print("Suspeita:")
    print("as mudanças precisam de decisão humana.")
    print()
    print("Por quê?")
    print("O Git não deve escolher sozinho quando duas versões mexem no mesmo lugar.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("Git não existe para impedir o trabalho.")
    print()
    print("Ele existe para deixar rastros claros,")
    print("evitar adivinhação")
    print("e ajudar o time a trabalhar sem apagar o caminho.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def missao_producao_etapa_7():
    print()
    print("=" * 60)
    print("🏢 MISSÃO EM PRODUÇÃO: O TIME TRABALHANDO JUNTO")
    print("=" * 60)
    print("Richard aparece na tela e olha diretamente para você.")
    print()
    print("Agora o caderno do time sai do treinamento e entra em produção.")
    print()
    print("Imagine que a equipe da CampOne está trabalhando no mesmo app.")
    print()
    print("-" * 60)
    print("CENA 1 — UMA PESSOA COMEÇA NO PROJETO")
    print("-" * 60)
    print("Ela precisa trazer uma cópia do projeto para a própria máquina.")
    print()
    print("Essa primeira cópia é a ideia do clone.")
    print()
    print("-" * 60)
    print("CENA 2 — UMA FUNCIONALIDADE É CRIADA")
    print("-" * 60)
    print("A pessoa trabalha em uma nova tela.")
    print()
    print("Quando termina uma parte importante, registra a mudança com commit.")
    print()
    print("O commit deixa claro o que mudou.")
    print()
    print("-" * 60)
    print("CENA 3 — A MUDANÇA PRECISA CHEGAR AO TIME")
    print("-" * 60)
    print("Depois de registrar, a pessoa envia sua parte para o repositório online.")
    print()
    print("Essa é a ideia do push.")
    print()
    print("-" * 60)
    print("CENA 4 — O TIME TAMBÉM MUDOU COISAS")
    print("-" * 60)
    print("Antes de continuar trabalhando, a pessoa precisa atualizar sua cópia.")
    print()
    print("Essa é a ideia do pull.")
    print()
    print("-" * 60)
    print("CENA 5 — MUDANÇAS SE ENCONTRAM")
    print("-" * 60)
    print("Quando linhas de trabalho se juntam, pode acontecer merge.")
    print()
    print("Se duas mudanças baterem no mesmo ponto, pode aparecer conflito.")
    print()
    print("O conflito pede conversa e decisão do time.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("No trabalho real, Git e GitHub ajudam o time a não depender de memória solta.")
    print()
    print("Cada mudança ganha registro.")
    print("Cada pessoa consegue enviar e receber trabalho.")
    print("Cada problema pode ser investigado no histórico.")
    print()
    print("Um bom dev não só altera o projeto.")
    print("Ele deixa o caminho compreensível para o time.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def prova_dominio_etapa_7():
    while True:
        print()
        print("=" * 60)
        print("✅ PROVA DE DOMÍNIO: O CADERNO DO TIME")
        print("=" * 60)
        print("Richard aparece na tela e olha diretamente para você.")
        print()
        print('"Agora vamos juntar o caderno inteiro em uma cena só."')
        print()
        print("Um dev cria uma mudança em uma branch,")
        print("registra com commit,")
        print("envia para o GitHub,")
        print("atualiza a própria cópia com o que o time fez")
        print("e encontra um conflito ao juntar mudanças.")
        print()
        print("PERGUNTA:")
        print("Qual leitura mostra melhor o que aconteceu?")
        print()
        print("1 - O banco de dados decidiu sozinho que a mudança era inválida.")
        print("2 - O frontend apagou a tela porque o botão foi clicado errado.")
        print("3 - O dev trabalhou em uma linha separada, registrou a mudança, compartilhou no repositório, atualizou a cópia local e encontrou uma parte que precisa de decisão humana.")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "3":
            print()
            print("Richard confirma.")
            print('"Isso. Você juntou o caderno do time:"')
            print('"branch, commit, GitHub, push, pull e conflito."')
            print()
            print("A base teórica de Git e GitHub está dominada.")
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print()
            print("Richard reancora com calma.")
            print('"Quase. Banco de dados não decide conflito de histórico do projeto."')
            print('"Aqui estamos falando de Git, GitHub e colaboração."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == "2":
            print()
            print("Richard aponta para o caderno do time.")
            print('"Boa tentativa, mas isso não é problema de tela."')
            print('"O conflito apareceu porque mudanças do projeto precisam ser combinadas."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def registro_etapa_7():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA — O CADERNO DO TIME")
    print("=" * 60)
    print("Richard aparece na tela e olha diretamente para você.")
    print()
    print("Vamos registrar o que você entendeu sobre Git e GitHub.")
    print()
    print("Você reconheceu que:")
    print()
    print("- Git guarda a história das mudanças do projeto;")
    print("- commit registra uma mudança com sentido;")
    print("- branch cria uma linha segura de trabalho;")
    print("- merge junta mudanças;")
    print("- conflito pede decisão humana;")
    print("- GitHub ajuda o time a compartilhar o repositório;")
    print("- clone traz uma cópia do projeto;")
    print("- push envia mudanças;")
    print("- pull atualiza sua cópia local;")
    print("- histórico ajuda a investigar a evolução do projeto.")
    print()
    print("Richard confirma:")
    print()
    print("Isso ainda não é programação prática.")
    print("É visão de trabalho em equipe.")
    print()
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_7():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL — O CADERNO DO TIME")
    print("=" * 60)
    print("Richard aparece na tela e olha diretamente para você.")
    print()
    print("Relatório da missão: Dominando as Linhas do Tempo")
    print()
    print("Você agora sabe que:")
    print()
    print("- Git é o caderno de mudanças do projeto;")
    print("- commits registram momentos importantes;")
    print("- branches permitem trabalhar sem mexer direto na linha principal;")
    print("- merge junta linhas de trabalho;")
    print("- conflitos não são desastre, são pedidos de decisão;")
    print("- GitHub ajuda o time a colaborar pela internet;")
    print("- clone, push e pull movem o projeto entre sua máquina e o repositório;")
    print("- o histórico evita adivinhação quando algo quebra.")
    print()
    print("Conclusão:")
    print()
    print("Você começou a enxergar que um projeto profissional precisa de memória.")
    print()
    print("Não basta alterar.")
    print("É preciso deixar rastro, contexto e caminho para o time.")
    print()
    print("A etapa ainda não marca conclusão permanente nesta versão.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def entrar_etapa_7():
    while True:
        print()
        print("=" * 60)
        print("07. DOMINANDO AS LINHAS DO TEMPO")
        print("=" * 60)
        print("Tema real: Git e GitHub")
        print("Tipo: Treinamento de Sobrevivência")
        print("Status: Estrutura inicial")
        print("Mentor previsto: Richard")
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
            cena_abertura_etapa_7()
        elif escolha == "2":
            reconhecimento_etapa_7()
        elif escolha == "3":
            campo_treinamento_etapa_7()
        elif escolha == "4":
            laboratorio_falhas_etapa_7()
        elif escolha == "5":
            missao_producao_etapa_7()
        elif escolha == "6":
            prova_dominio_etapa_7()
        elif escolha == "7":
            registro_etapa_7()
        elif escolha == "8":
            relatorio_final_etapa_7()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")



def topico_sistema_local_etapa_8():
    while True:
        print()
        print("=" * 60)
        print('🏠 TÓPICO 1: SISTEMA LOCAL')
        print("=" * 60)
        print('Um sistema pode funcionar perfeitamente no computador do desenvolvedor.')
        print()
        print('Mas, se só funciona ali, o cliente ainda não consegue usar.')
        print()
        print('Gabriel aparece na tela e olha diretamente para você.')
        print()
        print('Um sistema preso no computador do dev ainda não virou produto.')
        print()
        print('Ideia de sobrevivência:')
        print('local é o ambiente onde o dev cria e testa antes de publicar.')
        print()
        print("PERGUNTA:")
        print('Por que um sistema funcionando apenas no computador do desenvolvedor')
        print('ainda não é um produto disponível?')
        print()
        print('1 - Porque o computador do dev sempre apaga o banco de dados.')
        print('2 - Porque outras pessoas ainda não conseguem acessar e usar esse sistema.')
        print('3 - Porque sistema local já está automaticamente publicado para clientes.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Gabriel confirma.')
            print('"Isso. Se só funciona no computador do dev, ainda não está disponível para usuários reais."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Gabriel reancora com calma.')
            print('"Quase. O problema não é o banco apagar."')
            print('"O ponto é que o sistema ainda está preso no ambiente do dev."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Gabriel aponta para a diferença entre local e publicado.')
            print('"Boa tentativa, mas local não significa publicado."')
            print('"Local é onde o dev cria e testa."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_deploy_etapa_8():
    while True:
        print()
        print("=" * 60)
        print('🚀 TÓPICO 2: DEPLOY')
        print("=" * 60)
        print('Deploy é o momento em que o sistema sai do ambiente privado')
        print('e vai para um lugar onde outras pessoas conseguem acessar.')
        print()
        print('É como mudar de uma garagem fechada para uma loja com endereço aberto.')
        print()
        print('Gabriel aponta para uma tela de publicação.')
        print()
        print('Deploy não é só apertar um botão.')
        print('É colocar o sistema no ar com cuidado.')
        print()
        print('Ideia de sobrevivência:')
        print('deploy coloca o sistema em funcionamento para usuários reais.')
        print()
        print("PERGUNTA:")
        print('O que melhor descreve o deploy?')
        print()
        print('1 - A mudança que leva o sistema para um ambiente onde usuários conseguem acessar.')
        print('2 - A troca das cores e botões da interface.')
        print('3 - O ato de apagar todo o histórico do Git.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Gabriel confirma.')
            print('"Isso. Deploy é colocar o sistema em funcionamento para usuários reais."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Gabriel reancora com calma.')
            print('"Quase. Cores e botões são assunto de interface."')
            print('"Deploy é sobre disponibilizar o sistema."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Gabriel separa deploy de histórico.')
            print('"Boa tentativa, mas deploy não apaga histórico."')
            print('"Ele leva uma versão para um ambiente acessível."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_servidor_deploy_etapa_8():
    while True:
        print()
        print("=" * 60)
        print('🖥️ TÓPICO 3: SERVIDOR')
        print("=" * 60)
        print('Depois do deploy, o sistema precisa morar em algum lugar.')
        print()
        print('Esse lugar é um servidor.')
        print()
        print('Servidor é a máquina ou ambiente que fica disponível para receber acessos.')
        print()
        print('Gabriel olha diretamente para você.')
        print()
        print('O servidor é a casa onde o sistema fica funcionando fora do computador do dev.')
        print()
        print('Ideia de sobrevivência:')
        print('servidor mantém o sistema disponível para quem precisa usar.')
        print()
        print("PERGUNTA:")
        print('Depois do deploy, por que o sistema precisa de um servidor?')
        print()
        print('1 - Para o usuário escolher a cor do aplicativo.')
        print('2 - Para substituir todos os arquivos do projeto por imagens.')
        print('3 - Para ter um ambiente disponível onde o sistema possa receber acessos.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Gabriel confirma.')
            print('"Isso. Servidor é a casa onde o sistema fica disponível fora do computador do dev."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Gabriel reancora com calma.')
            print('"Quase. Cor do aplicativo é assunto de frontend."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Gabriel aponta para a função da casa.')
            print('"Boa tentativa, mas servidor não transforma projeto em imagens."')
            print('"Ele hospeda o sistema funcionando."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_dominio_dns_etapa_8():
    while True:
        print()
        print("=" * 60)
        print('🌐 TÓPICO 4: DOMÍNIO E DNS')
        print("=" * 60)
        print('Depois que o sistema tem uma casa, as pessoas precisam encontrar essa casa.')
        print()
        print('Domínio é o nome fácil que a pessoa digita.')
        print('DNS é a agenda que liga esse nome ao endereço real do servidor.')
        print()
        print('Gabriel desenha uma placa de endereço.')
        print()
        print('Sem domínio e DNS configurados, o usuário pode não encontrar o sistema.')
        print()
        print('Ideia de sobrevivência:')
        print('domínio é o nome; DNS aponta esse nome para o servidor certo.')
        print()
        print("PERGUNTA:")
        print('Qual é a relação entre domínio e DNS?')
        print()
        print('1 - Domínio guarda a senha do usuário e DNS desenha a tela.')
        print('2 - Domínio é o nome fácil, e DNS aponta esse nome para o servidor correto.')
        print('3 - Domínio e DNS servem para apagar versões antigas do projeto.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Gabriel confirma.')
            print('"Isso. Domínio é o nome fácil; DNS liga esse nome ao endereço real."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Gabriel reancora com calma.')
            print('"Quase. Senha é segurança; desenho da tela é frontend."')
            print('"Domínio e DNS ajudam a encontrar o sistema."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Gabriel aponta para o endereço.')
            print('"Boa tentativa, mas apagar versões é outro assunto."')
            print('"Aqui falamos de endereço."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_hospedagem_vps_nuvem_etapa_8():
    while True:
        print()
        print("=" * 60)
        print('🏢 TÓPICO 5: HOSPEDAGEM, VPS E NUVEM')
        print("=" * 60)
        print('Existem formas diferentes de dar moradia para um sistema.')
        print()
        print('Hospedagem é a empresa ou serviço que oferece o lugar.')
        print('VPS é como um apartamento separado dentro de uma estrutura maior.')
        print('Nuvem é uma estrutura flexível que pode crescer conforme a necessidade.')
        print()
        print('Gabriel aponta para três tipos de moradia.')
        print()
        print('O melhor caminho depende do tamanho, custo, controle e crescimento do projeto.')
        print()
        print('Ideia de sobrevivência:')
        print('hospedagem é a moradia; VPS e nuvem são modelos possíveis dessa moradia.')
        print()
        print("PERGUNTA:")
        print('O que melhor descreve hospedagem, VPS e nuvem?')
        print()
        print('1 - Formas de dar moradia para o sistema funcionar fora do computador do dev.')
        print('2 - Tipos de botão que aparecem na interface.')
        print('3 - Métodos para criar commits automaticamente.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Gabriel confirma.')
            print('"Isso. São formas de hospedar o sistema e mantê-lo acessível."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Gabriel reancora com calma.')
            print('"Quase. Botões pertencem à interface."')
            print('"Aqui falamos de onde o sistema mora."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Gabriel separa deploy de Git.')
            print('"Boa tentativa. Commits são Git."')
            print('"Hospedagem, VPS e nuvem são moradia e estrutura."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_pipeline_etapa_8():
    while True:
        print()
        print("=" * 60)
        print('🏭 TÓPICO 6: PIPELINE')
        print("=" * 60)
        print('Deploy moderno pode ter uma esteira de segurança.')
        print()
        print('Pipeline é uma sequência organizada que pode conferir, testar e publicar mudanças.')
        print()
        print('Se algo está errado, a esteira pode parar antes de afetar o usuário.')
        print()
        print('Gabriel mostra uma linha de etapas.')
        print()
        print('A pipeline ajuda o time a publicar com mais cuidado e menos improviso.')
        print()
        print('Ideia de sobrevivência:')
        print('pipeline é a esteira que ajuda a levar mudanças para produção com segurança.')
        print()
        print("PERGUNTA:")
        print('Por que uma pipeline ajuda no deploy?')
        print()
        print('1 - Porque ela troca o nome do domínio sozinha todos os dias.')
        print('2 - Porque ela substitui todos os testes por sorte.')
        print('3 - Porque ela organiza etapas para conferir, testar e publicar mudanças com mais segurança.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Gabriel confirma.')
            print('"Isso. Pipeline é a esteira que ajuda a publicar com cuidado."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Gabriel reancora com calma.')
            print('"Quase. Domínio é endereço."')
            print('"Pipeline é esteira de publicação."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Gabriel aponta para o cuidado.')
            print('"Boa tentativa, mas pipeline não é sorte."')
            print('"Ela existe para reduzir improviso."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_producao_etapa_8():
    while True:
        print()
        print("=" * 60)
        print('🌍 TÓPICO 7: PRODUÇÃO')
        print("=" * 60)
        print('Produção é o ambiente onde usuários reais usam o sistema.')
        print()
        print('Ali, qualquer mudança precisa de cuidado.')
        print()
        print('Uma falha em produção pode afetar clientes, dados e a reputação da empresa.')
        print()
        print('Gabriel fala com seriedade.')
        print()
        print('O melhor deploy é aquele que o usuário nem percebe.')
        print()
        print('Ideia de sobrevivência:')
        print('produção é o mundo real do sistema em funcionamento.')
        print()
        print("PERGUNTA:")
        print('Por que mudanças em produção exigem cuidado?')
        print()
        print('1 - Porque produção é só um desenho sem usuários reais.')
        print('2 - Porque usuários reais podem ser afetados se algo quebrar.')
        print('3 - Porque produção apaga automaticamente todo o código local.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Gabriel confirma.')
            print('"Isso. Produção é o mundo real do sistema, então exige cuidado."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Gabriel reancora com calma.')
            print('"Quase. Produção não é desenho; é o sistema real em uso."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Gabriel aponta para o risco real.')
            print('"Boa tentativa, mas produção não apaga código local."')
            print('"O risco é afetar usuários reais."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")



def reconhecimento_etapa_8():
    while True:
        print()
        print("=" * 60)
        print("💡 RECONHECIMENTO: O SISTEMA NO AR")
        print("=" * 60)
        print("Gabriel organiza os primeiros conceitos de Deploy.")
        print()
        print("1 - Sistema local")
        print("2 - Deploy")
        print("3 - Servidor")
        print("4 - Domínio e DNS")
        print("5 - Hospedagem, VPS e Nuvem")
        print("6 - Pipeline")
        print("7 - Produção")
        print("0 - Voltar à etapa 08")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_sistema_local_etapa_8()
        elif escolha == "2":
            topico_deploy_etapa_8()
        elif escolha == "3":
            topico_servidor_deploy_etapa_8()
        elif escolha == "4":
            topico_dominio_dns_etapa_8()
        elif escolha == "5":
            topico_hospedagem_vps_nuvem_etapa_8()
        elif escolha == "6":
            topico_pipeline_etapa_8()
        elif escolha == "7":
            topico_producao_etapa_8()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")

def cena_abertura_etapa_8():
    print()
    print("=" * 60)
    print("🎬 INICIAR MISSÃO: O SISTEMA GANHA ENDEREÇO")
    print("=" * 60)
    print("Você chega a uma sala cheia de painéis verdes.")
    print()
    print("Até aqui, você já entendeu como o sistema nasce,")
    print("como ele guarda dados,")
    print("como a tela conversa com o backend,")
    print("como a interface aparece para o usuário,")
    print("como a segurança protege a entrada")
    print("e como o time registra mudanças com Git e GitHub.")
    print()
    print("Mas ainda existe uma pergunta importante:")
    print()
    print("como o sistema sai do computador do desenvolvedor")
    print("e fica disponível para pessoas usarem de verdade?")
    print()
    print("Gabriel aparece na tela e olha diretamente para você.")
    print()
    print("Olá. Eu sou Gabriel.")
    print()
    print("Minha área é Deploy.")
    print("Eu cuido do momento em que o sistema deixa de ser só código")
    print("e passa a estar disponível em um ambiente real.")
    print()
    print("Um sistema funcionando apenas no computador do dev")
    print("ainda não é um produto acessível.")
    print()
    print("Deploy é a passagem para o mundo real.")
    print()
    print("Nesta etapa, você vai entender:")
    print()
    print("- o que é um sistema local;")
    print("- o que significa fazer deploy;")
    print("- por que o sistema precisa de servidor;")
    print("- como domínio e DNS ajudam as pessoas a encontrar o sistema;")
    print("- o que são hospedagem, VPS e nuvem;")
    print("- como uma pipeline ajuda a publicar com segurança;")
    print("- e por que produção exige cuidado.")
    print()
    print("Gabriel aponta para o painel.")
    print()
    print("Sem decorar comando.")
    print("Sem sintaxe disfarçada.")
    print("Primeiro você entende a mudança de casa.")
    print("Depois, no mundo prático, aprende a operar a ferramenta.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def campo_treinamento_etapa_8():
    print()
    print("=" * 60)
    print("🛠️ CAMPO DE TREINAMENTO: A MUDANÇA DE CASA")
    print("=" * 60)
    print("Gabriel aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos acompanhar o caminho de um sistema saindo do computador do dev")
    print("e indo para um lugar onde outras pessoas conseguem acessar.")
    print()
    print("-" * 60)
    print("1. O SISTEMA FUNCIONA LOCALMENTE")
    print("-" * 60)
    print("No começo, o sistema funciona no computador de quem desenvolve.")
    print()
    print("Isso é útil para criar, testar e ajustar.")
    print()
    print("Mas o cliente não usa o computador do dev.")
    print()
    print("-" * 60)
    print("2. O SISTEMA PRECISA DE UMA CASA")
    print("-" * 60)
    print("Para outras pessoas acessarem, o sistema precisa morar em um servidor.")
    print()
    print("O servidor é o ambiente que fica disponível para receber acessos.")
    print()
    print("-" * 60)
    print("3. A MUDANÇA ACONTECE")
    print("-" * 60)
    print("Deploy é a mudança do sistema para esse ambiente acessível.")
    print()
    print("Antes, ele funcionava só localmente.")
    print("Depois, pode ser usado por usuários reais.")
    print()
    print("-" * 60)
    print("4. AS PESSOAS PRECISAM ENCONTRAR O SISTEMA")
    print("-" * 60)
    print("Um sistema no ar precisa de endereço.")
    print()
    print("O domínio é o nome fácil.")
    print("O DNS aponta esse nome para o servidor certo.")
    print()
    print("-" * 60)
    print("5. A PUBLICAÇÃO PRECISA DE CUIDADO")
    print("-" * 60)
    print("Em produção, pessoas reais podem estar usando o sistema.")
    print()
    print("Por isso, publicar mudança exige atenção.")
    print()
    print("Uma pipeline pode ajudar a conferir, testar e publicar com mais segurança.")
    print()
    print("-" * 60)
    print("RESUMO DO TREINAMENTO")
    print("-" * 60)
    print("Local é onde o dev cria e testa.")
    print("Servidor é onde o sistema pode morar.")
    print("Deploy é a mudança para um ambiente acessível.")
    print("Domínio é o nome fácil.")
    print("DNS aponta o nome para o servidor.")
    print("Pipeline ajuda a publicar com cuidado.")
    print("Produção é o mundo real do sistema.")
    print()
    print("Ideia de sobrevivência:")
    print("deploy transforma um sistema pronto em um sistema disponível.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def laboratorio_falhas_etapa_8():
    print()
    print("=" * 60)
    print("🧪 LABORATÓRIO DE FALHAS: QUANDO O SISTEMA NÃO SOBE")
    print("=" * 60)
    print("Gabriel aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos olhar falhas comuns no deploy.")
    print()
    print("A ideia não é decorar comando.")
    print("A ideia é entender onde a mudança pode quebrar.")
    print()
    print("-" * 60)
    print("FALHA 1 — FUNCIONA NA MINHA MÁQUINA")
    print("-" * 60)
    print("O sistema funciona no computador do dev,")
    print("mas não funciona no servidor.")
    print()
    print("Suspeita:")
    print("ambiente diferente ou configuração faltando.")
    print()
    print("Por quê?")
    print("O computador local e o servidor podem não estar preparados do mesmo jeito.")
    print()
    print("-" * 60)
    print("FALHA 2 — SISTEMA SEM ENDEREÇO")
    print("-" * 60)
    print("O sistema foi enviado para o servidor,")
    print("mas o usuário não consegue encontrar pelo nome do site.")
    print()
    print("Suspeita:")
    print("domínio ou DNS mal configurado.")
    print()
    print("Por quê?")
    print("O nome fácil precisa apontar para o servidor certo.")
    print()
    print("-" * 60)
    print("FALHA 3 — MUDANÇA QUEBRA EM PRODUÇÃO")
    print("-" * 60)
    print("Uma nova versão foi publicada e usuários reais começaram a ter problema.")
    print()
    print("Suspeita:")
    print("mudança publicada sem validação suficiente.")
    print()
    print("Por quê?")
    print("Produção exige cuidado porque afeta pessoas reais.")
    print()
    print("-" * 60)
    print("FALHA 4 — ESTEIRA PAROU")
    print("-" * 60)
    print("A pipeline tentou publicar, mas parou antes do fim.")
    print()
    print("Suspeita:")
    print("a esteira encontrou algo errado antes de chegar ao usuário.")
    print()
    print("Por quê?")
    print("Isso pode ser proteção, não defeito.")
    print("Melhor parar antes do cliente ser afetado.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("Deploy ruim pode derrubar uma experiência real.")
    print()
    print("Por isso, colocar no ar exige ambiente certo, endereço certo,")
    print("configuração correta e cuidado com produção.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def missao_producao_etapa_8():
    print()
    print("=" * 60)
    print("🏢 MISSÃO EM PRODUÇÃO: O SISTEMA NO AR")
    print("=" * 60)
    print("Gabriel aparece na tela e olha diretamente para você.")
    print()
    print("Agora o deploy sai do treinamento e entra em produção.")
    print()
    print("Imagine que a CampOne tem uma nova versão do app pronta.")
    print()
    print("-" * 60)
    print("CENA 1 — O CÓDIGO ESTÁ PRONTO")
    print("-" * 60)
    print("O time terminou uma melhoria.")
    print()
    print("A mudança foi registrada no Git.")
    print("O repositório está atualizado.")
    print()
    print("Mas isso ainda não significa que o cliente consegue usar.")
    print()
    print("-" * 60)
    print("CENA 2 — A ESTEIRA CONFERE")
    print("-" * 60)
    print("Antes de publicar, a pipeline pode conferir se está tudo em ordem.")
    print()
    print("Ela pode rodar verificações, preparar o ambiente e evitar improviso.")
    print()
    print("-" * 60)
    print("CENA 3 — O SISTEMA VAI PARA O SERVIDOR")
    print("-" * 60)
    print("A nova versão vai para o ambiente onde o sistema mora.")
    print()
    print("Esse ambiente precisa estar preparado para receber acessos.")
    print()
    print("-" * 60)
    print("CENA 4 — O ENDEREÇO APONTA PARA O LUGAR CERTO")
    print("-" * 60)
    print("O domínio precisa levar o usuário até o servidor correto.")
    print()
    print("O DNS ajuda nessa ligação entre nome fácil e endereço real.")
    print()
    print("-" * 60)
    print("CENA 5 — O USUÁRIO ACESSA")
    print("-" * 60)
    print("Agora o usuário abre o navegador e consegue usar a nova versão.")
    print()
    print("Se tudo deu certo, ele nem percebeu a mudança acontecendo.")
    print()
    print("-" * 60)
    print("IDEIA DE SOBREVIVÊNCIA")
    print("-" * 60)
    print("Deploy é o caminho entre código pronto e sistema usado por pessoas reais.")
    print()
    print("O objetivo não é só colocar na internet.")
    print("É colocar de um jeito seguro, estável e encontrável.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def prova_dominio_etapa_8():
    while True:
        print()
        print("=" * 60)
        print("✅ PROVA DE DOMÍNIO: O SISTEMA NO AR")
        print("=" * 60)
        print("Gabriel aparece na tela e olha diretamente para você.")
        print()
        print("A CampOne tem um sistema pronto no computador do dev,")
        print("envia para um servidor,")
        print("configura domínio e DNS,")
        print("usa uma pipeline")
        print("e publica para usuários reais.")
        print()
        print("PERGUNTA:")
        print("Qual leitura resume melhor esse caminho?")
        print()
        print("1 - O sistema só mudou de cor e continuou preso no computador do dev.")
        print("2 - O banco de dados decidiu sozinho publicar a aplicação.")
        print("3 - O sistema saiu do ambiente local, foi para um servidor, ganhou endereço e chegou à produção com cuidado.")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "3":
            print()
            print("Gabriel confirma.")
            print('"Isso. Você juntou o caminho do deploy:"')
            print('"local, servidor, endereço, pipeline e produção."')
            print()
            print("A base teórica de Deploy está dominada.")
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print()
            print("Gabriel reancora com calma.")
            print('"Quase. Deploy não é mudança de cor."')
            print('"É disponibilizar o sistema."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == "2":
            print()
            print("Gabriel aponta para o caminho do deploy.")
            print('"Boa tentativa, mas banco não publica sozinho."')
            print('"Deploy envolve ambiente, servidor, endereço e produção."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def registro_etapa_8():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA — O SISTEMA NO AR")
    print("=" * 60)
    print("Gabriel aparece na tela e olha diretamente para você.")
    print()
    print("Vamos registrar o que você entendeu sobre deploy.")
    print()
    print("Você reconheceu que:")
    print()
    print("- sistema local é onde o dev cria e testa;")
    print("- deploy leva o sistema para um ambiente acessível;")
    print("- servidor é a casa onde o sistema fica disponível;")
    print("- domínio é o nome fácil que a pessoa digita;")
    print("- DNS aponta esse nome para o servidor correto;")
    print("- hospedagem, VPS e nuvem são formas de moradia do sistema;")
    print("- pipeline ajuda a publicar mudanças com mais segurança;")
    print("- produção é o ambiente usado por pessoas reais;")
    print("- deploy exige cuidado porque afeta usuários de verdade.")
    print()
    print("Gabriel confirma:")
    print()
    print("Isso ainda não é programação prática.")
    print("É visão de publicação.")
    print()
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_8():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL — O SISTEMA NO AR")
    print("=" * 60)
    print("Gabriel aparece na tela e olha diretamente para você.")
    print()
    print("Relatório da missão: O Rito da Grande Implantação")
    print()
    print("Você agora sabe que:")
    print()
    print("- um sistema preso no computador do dev ainda não é produto disponível;")
    print("- deploy é colocar o sistema em funcionamento para usuários reais;")
    print("- servidor é onde o sistema fica disponível fora do ambiente local;")
    print("- domínio e DNS ajudam as pessoas a encontrar o sistema;")
    print("- hospedagem, VPS e nuvem são formas de dar moradia ao sistema;")
    print("- pipeline ajuda a levar mudanças para produção com cuidado;")
    print("- produção é o mundo real do sistema em uso;")
    print("- o melhor deploy é aquele que o usuário nem percebe.")
    print()
    print("Conclusão:")
    print()
    print("Deploy não é só colocar algo na internet.")
    print("É publicar com endereço, ambiente, cuidado e responsabilidade.")
    print()
    print("A etapa ainda não marca conclusão permanente nesta versão.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def entrar_etapa_8():
    while True:
        print()
        print("=" * 60)
        print("08. O RITO DA GRANDE IMPLANTAÇÃO")
        print("=" * 60)
        print("Tema real: Deploy")
        print("Tipo: Treinamento de Sobrevivência")
        print("Status: Estrutura inicial")
        print("Mentor previsto: Gabriel")
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
            cena_abertura_etapa_8()
        elif escolha == "2":
            reconhecimento_etapa_8()
        elif escolha == "3":
            campo_treinamento_etapa_8()
        elif escolha == "4":
            laboratorio_falhas_etapa_8()
        elif escolha == "5":
            missao_producao_etapa_8()
        elif escolha == "6":
            prova_dominio_etapa_8()
        elif escolha == "7":
            registro_etapa_8()
        elif escolha == "8":
            relatorio_final_etapa_8()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")



def cena_abertura_etapa_9():
    print()
    print("=" * 60)
    print("🎬 INICIAR MISSÃO: A PLANTA-MESTRA")
    print("=" * 60)
    print("Você chega a uma sala ampla da CampOne.")
    print()
    print("Na parede, existe uma folha grande em branco.")
    print("Ao redor dela, estão as peças que você já conheceu:")
    print()
    print("- a rede;")
    print("- o backend;")
    print("- o banco de dados;")
    print("- a ponte entre frontend e backend;")
    print("- a interface visual;")
    print("- a portaria digital;")
    print("- o caderno do time;")
    print("- e o sistema no ar.")
    print()
    print("Agora falta entender como tudo isso se organiza.")
    print()
    print("Adria aparece na tela e olha diretamente para você.")
    print()
    print("Olá. Eu sou Adria.")
    print()
    print("Minha área é Arquitetura.")
    print("Eu ajudo o time a enxergar a planta do sistema antes de construir ou mudar qualquer coisa.")
    print()
    print("Arquitetura não é enfeite.")
    print("É entender onde cada parte mora, pelo que ela é responsável e como conversa com as outras.")
    print()
    print("Nesta etapa, você vai entender:")
    print()
    print("- o que é arquitetura de software;")
    print("- por que cliente e servidor ficam separados;")
    print("- como as camadas do sistema se organizam;")
    print("- como frontend, backend, banco, API, segurança e deploy trabalham juntos;")
    print("- como um pedido atravessa a planta inteira;")
    print("- e por que uma boa planta ajuda o time a diagnosticar problemas.")
    print()
    print("Adria aponta para a folha em branco.")
    print()
    print("Sem decorar nomes.")
    print("Sem sintaxe disfarçada.")
    print("Primeiro você entende a planta.")
    print("Depois, no mundo prático, aprende a construir com organização.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def topico_arquitetura_etapa_9():
    while True:
        print()
        print("=" * 60)
        print('🏛️ TÓPICO 1: O QUE É ARQUITETURA')
        print("=" * 60)
        print('Arquitetura é a planta do sistema.')
        print()
        print('Ela mostra onde cada parte fica, qual responsabilidade cada uma tem')
        print('e como essas partes conversam entre si.')
        print()
        print('Adria olha diretamente para você.')
        print()
        print('Antes de construir rápido, o time precisa saber que casa está construindo.')
        print()
        print('Ideia de sobrevivência:')
        print('arquitetura é a organização das partes do sistema.')
        print()
        print("PERGUNTA:")
        print('O que melhor descreve arquitetura de software?')
        print()
        print('1 - Um conjunto de cores e botões bonitos na tela.')
        print('2 - A organização das partes do sistema, mostrando onde cada peça fica, sua responsabilidade e como conversa com as outras.')
        print('3 - Um lugar onde o banco de dados guarda senhas para sempre.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Adria confirma.')
            print('"Isso. Arquitetura é a planta do sistema."')
            print('"Ela ajuda o time a entender onde cada parte mora e como tudo conversa."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Adria reancora com calma.')
            print('"Quase. Cores e botões fazem parte da interface visual."')
            print('"Arquitetura olha para a organização do sistema inteiro."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Adria aponta para a planta completa.')
            print('"Boa tentativa. Banco de dados guarda informações, mas arquitetura não é só armazenamento."')
            print('"Ela mostra a planta completa das partes do sistema."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_cliente_servidor_etapa_9():
    while True:
        print()
        print("=" * 60)
        print('🧱 TÓPICO 2: CLIENTE E SERVIDOR')
        print("=" * 60)
        print('Todo sistema web tem dois lados importantes.')
        print()
        print('O cliente é o lado que a pessoa usa:')
        print('navegador, aplicativo, tela, botão, formulário.')
        print()
        print('O servidor é o lado que responde:')
        print('regras, processamento, dados, segurança e respostas.')
        print()
        print('Adria desenha uma linha separando os dois lados.')
        print()
        print('O cliente pede. O servidor responde.')
        print()
        print('Ideia de sobrevivência:')
        print('cliente e servidor são lados separados que conversam.')
        print()
        print("PERGUNTA:")
        print('Em uma arquitetura web, qual é a ideia principal entre cliente e servidor?')
        print()
        print('1 - O cliente pede, e o servidor recebe, trabalha e responde.')
        print('2 - O cliente guarda todos os dados sozinho, sem servidor.')
        print('3 - O servidor escolhe as cores da tela do usuário sem nenhuma comunicação.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Adria confirma.')
            print('"Isso. Cliente e servidor são lados separados que conversam."')
            print('"O cliente pede; o servidor responde."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Adria reancora com calma.')
            print('"Quase. O cliente usa a tela, mas não carrega o sistema inteiro sozinho."')
            print('"Quando precisa de dados ou regras, ele conversa com o servidor."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Adria separa visual de arquitetura.')
            print('"Boa tentativa, mas cor da tela é assunto de frontend."')
            print('"Servidor entra para responder pedidos e aplicar regras."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_camadas_etapa_9():
    while True:
        print()
        print("=" * 60)
        print('🏗️ TÓPICO 3: CAMADAS DO SISTEMA')
        print("=" * 60)
        print('Um sistema organizado não mistura tudo no mesmo lugar.')
        print()
        print('Cada camada tem uma responsabilidade.')
        print()
        print('A interface mostra e recebe ações.')
        print('O backend aplica regras.')
        print('O banco guarda informações.')
        print('A segurança controla acesso.')
        print('O deploy coloca o sistema no ar.')
        print()
        print('Adria aponta para a planta.')
        print()
        print('Quando cada camada sabe seu papel, o sistema fica mais fácil de entender e manter.')
        print()
        print('Ideia de sobrevivência:')
        print('camadas separam responsabilidades.')
        print()
        print("PERGUNTA:")
        print('Por que separar o sistema em camadas ajuda a manter a organização?')
        print()
        print('1 - Porque todas as partes passam a fazer exatamente a mesma coisa.')
        print('2 - Porque a separação apaga o histórico do projeto.')
        print('3 - Porque cada parte tem uma responsabilidade clara, como interface, regras, dados, segurança e publicação.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Adria confirma.')
            print('"Isso. Camadas separam responsabilidades."')
            print('"Quando cada parte sabe seu papel, o sistema fica mais fácil de entender e manter."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Adria reancora com calma.')
            print('"Quase. Camadas não existem para todo mundo fazer a mesma coisa."')
            print('"Elas existem para separar responsabilidades."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Adria aponta para outro tema.')
            print('"Boa tentativa, mas histórico do projeto é tema de Git."')
            print('"Camadas ajudam a organizar as funções internas do sistema."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_api_planta_etapa_9():
    while True:
        print()
        print("=" * 60)
        print('🌉 TÓPICO 4: API — A JANELA ENTRE AS PARTES')
        print("=" * 60)
        print('As partes do sistema precisam conversar sem virar bagunça.')
        print()
        print('A API organiza a conversa entre a tela e o backend.')
        print()
        print('Ela funciona como uma janela de pedidos e respostas.')
        print()
        print('Adria desenha uma passagem entre a interface e o backend.')
        print()
        print('A tela não entra na cozinha do sistema.')
        print('Ela pede pela janela certa.')
        print()
        print('Ideia de sobrevivência:')
        print('API organiza a comunicação entre partes do sistema.')
        print()
        print("PERGUNTA:")
        print('Na planta do sistema, qual é o papel da API?')
        print()
        print('1 - Guardar todos os dados no lugar do banco.')
        print('2 - Organizar a comunicação entre partes, como a tela e o backend.')
        print('3 - Trocar automaticamente o layout da página no celular.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Adria confirma.')
            print('"Isso. API organiza a comunicação."')
            print('"Ela permite que a tela peça e o backend responda por caminhos combinados."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Adria reancora com calma.')
            print('"Quase. Guardar dados é papel do banco de dados."')
            print('"A API organiza a conversa entre partes do sistema."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Adria aponta para a janela correta.')
            print('"Boa tentativa, mas adaptação visual é tema de responsividade."')
            print('"A API é a janela de pedidos e respostas entre partes."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_fluxo_pedido_etapa_9():
    while True:
        print()
        print("=" * 60)
        print('🔁 TÓPICO 5: O CAMINHO COMPLETO DO PEDIDO')
        print("=" * 60)
        print('Agora a planta ganha movimento.')
        print()
        print('Um usuário toca na tela.')
        print('A interface cria um pedido.')
        print('O pedido passa pela internet.')
        print('A segurança pode conferir quem está pedindo.')
        print('O backend aplica regras.')
        print('O banco pode ser consultado.')
        print('A resposta volta.')
        print('A tela mostra o resultado.')
        print()
        print('Adria acompanha o caminho com o dedo na planta.')
        print()
        print('Ideia de sobrevivência:')
        print('arquitetura ajuda a seguir o pedido de ponta a ponta.')
        print()
        print("PERGUNTA:")
        print('Qual caminho representa melhor um pedido atravessando a planta do sistema?')
        print()
        print('1 - Usuário toca na tela, frontend monta pedido, segurança pode conferir, backend aplica regras, banco pode participar, resposta volta para a tela.')
        print('2 - O banco aparece direto para o usuário e decide sozinho o que mostrar.')
        print('3 - O frontend cria todos os dados sozinho sem pedir nada para outras partes.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print()
            print('Adria confirma.')
            print('"Isso. Você seguiu o pedido pela planta."')
            print('"A arquitetura ajuda a enxergar o caminho de ponta a ponta."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '2':
            print()
            print('Adria reancora com calma.')
            print('"Quase. O banco guarda dados, mas normalmente não aparece direto para o usuário."')
            print('"O pedido passa por outras partes antes da resposta voltar."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Adria aponta para o caminho completo.')
            print('"Boa tentativa, mas o frontend não faz tudo sozinho."')
            print('"Ele pede, recebe resposta e mostra o resultado."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_diagnostico_etapa_9():
    while True:
        print()
        print("=" * 60)
        print('🧭 TÓPICO 6: DIAGNÓSTICO PELA PLANTA')
        print("=" * 60)
        print('Quando algo quebra, a planta ajuda o time a não chutar no escuro.')
        print()
        print('Se a tela não reage, olhe para a interface.')
        print('Se o pedido falha, olhe a comunicação.')
        print('Se a regra dá errado, olhe o backend.')
        print('Se a informação some, olhe o banco.')
        print('Se o acesso é recusado, olhe a segurança.')
        print('Se o sistema não abre para ninguém, olhe deploy, servidor ou domínio.')
        print()
        print('Adria confirma.')
        print()
        print('A planta não resolve tudo sozinha, mas mostra onde procurar.')
        print()
        print('Ideia de sobrevivência:')
        print('arquitetura transforma problema confuso em suspeitas organizadas.')
        print()
        print("PERGUNTA:")
        print('Quando algo quebra, por que a planta do sistema ajuda no diagnóstico?')
        print()
        print('1 - Porque ela resolve todos os erros automaticamente sem análise.')
        print('2 - Porque ela troca a senha do usuário sempre que aparece um bug.')
        print('3 - Porque ela mostra onde procurar: tela, comunicação, backend, banco, segurança, deploy ou outro ponto da arquitetura.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            print()
            print('Adria confirma.')
            print('"Isso. Arquitetura transforma confusão em suspeitas organizadas."')
            print('"Ela mostra por onde começar a investigação."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Adria reancora com calma.')
            print('"Quase. A planta não resolve tudo sozinha."')
            print('"Ela ajuda o time a saber onde investigar."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '2':
            print()
            print('Adria aponta para outra área.')
            print('"Boa tentativa, mas senha é assunto de segurança."')
            print('"Diagnóstico pela planta é descobrir onde o problema pode estar."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def topico_planta_mestra_etapa_9():
    while True:
        print()
        print("=" * 60)
        print('🗺️ TÓPICO 7: A PLANTA-MESTRA')
        print("=" * 60)
        print('A planta-mestra junta tudo que você viu na Academy.')
        print()
        print('Rede para o caminho.')
        print('Backend para regras.')
        print('Banco para memória.')
        print('API para comunicação.')
        print('Frontend para experiência visual.')
        print('Segurança para entrada e permissão.')
        print('Git e GitHub para histórico do time.')
        print('Deploy para colocar no ar.')
        print()
        print('Adria olha diretamente para você.')
        print()
        print('Você não aprendeu peças soltas.')
        print('Você percorreu a planta inteira do sistema.')
        print()
        print('Ideia de sobrevivência:')
        print('arquitetura é enxergar o sistema inteiro sem se perder nas partes.')
        print()
        print("PERGUNTA:")
        print('O que a planta-mestra representa depois de todas as etapas da Academy?')
        print()
        print('1 - Apenas uma lista de comandos para decorar antes da prática.')
        print('2 - A visão do sistema inteiro, juntando rede, backend, banco, API, frontend, segurança, Git, deploy e responsabilidades.')
        print('3 - Um desenho sem utilidade que não ajuda o time a trabalhar.')
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print()
            print('Adria confirma.')
            print('"Isso. A planta-mestra junta tudo."')
            print('"Você não aprendeu peças soltas; você enxergou o sistema inteiro."')
            input("Pressione Enter para voltar...")
            break
        elif escolha == '1':
            print()
            print('Adria reancora com calma.')
            print('"Quase. A Academy não está criando lista de comandos."')
            print('"Ela está formando visão de sistema antes da prática."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == '3':
            print()
            print('Adria aponta para a utilidade da planta.')
            print('"Boa tentativa, mas a planta tem utilidade real."')
            print('"Ela ajuda o time a conversar, construir, manter e diagnosticar."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")



def reconhecimento_etapa_9():
    while True:
        print()
        print("=" * 60)
        print("💡 RECONHECIMENTO: A PLANTA DO SISTEMA")
        print("=" * 60)
        print("Adria organiza os primeiros conceitos de Arquitetura.")
        print()
        print("1 - O que é Arquitetura")
        print("2 - Cliente e Servidor")
        print("3 - Camadas do Sistema")
        print("4 - API — a janela entre as partes")
        print("5 - O caminho completo do pedido")
        print("6 - Diagnóstico pela planta")
        print("7 - A Planta-Mestra")
        print("0 - Voltar à etapa 09")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_arquitetura_etapa_9()
        elif escolha == "2":
            topico_cliente_servidor_etapa_9()
        elif escolha == "3":
            topico_camadas_etapa_9()
        elif escolha == "4":
            topico_api_planta_etapa_9()
        elif escolha == "5":
            topico_fluxo_pedido_etapa_9()
        elif escolha == "6":
            topico_diagnostico_etapa_9()
        elif escolha == "7":
            topico_planta_mestra_etapa_9()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")

def campo_treinamento_etapa_9():
    print()
    print("=" * 60)
    print("🛠️ CAMPO DE TREINAMENTO: SEGUINDO UM PEDIDO PELA PLANTA")
    print("=" * 60)
    print("Adria aparece na tela e olha diretamente para você.")
    print()
    print("Vamos seguir um pedido atravessando o sistema inteiro.")
    print()
    print("Cena:")
    print("Uma pessoa tenta reservar um horário pelo app da CampOne.")
    print()
    print("1. A pessoa toca na tela.")
    print("2. O frontend monta o pedido.")
    print("3. A internet leva o pedido até o servidor.")
    print("4. A segurança confere se a pessoa pode fazer aquilo.")
    print("5. O backend aplica as regras da reserva.")
    print("6. O banco verifica e guarda as informações.")
    print("7. O backend monta a resposta.")
    print("8. A tela mostra o resultado.")
    print()
    print("Ideia de sobrevivência:")
    print("arquitetura é saber por onde o pedido passa e quem faz cada parte.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def laboratorio_falhas_etapa_9():
    print()
    print("=" * 60)
    print("🧪 LABORATÓRIO DE FALHAS: ONDE O PEDIDO PAROU?")
    print("=" * 60)
    print("Adria aparece na tela e olha diretamente para você.")
    print()
    print("Agora vamos diagnosticar problemas usando a planta.")
    print()
    print("1. A tela está quebrada ou não reage.")
    print("Suspeita: frontend.")
    print()
    print("2. A tela pede, mas a resposta volta errada.")
    print("Suspeita: API, rota ou backend.")
    print()
    print("3. O sistema esquece dados ou mostra informação incorreta.")
    print("Suspeita: banco de dados ou regra de negócio.")
    print()
    print("4. A pessoa não consegue acessar uma área.")
    print("Suspeita: segurança, autenticação ou autorização.")
    print()
    print("5. O site nem abre pelo endereço.")
    print("Suspeita: deploy, servidor, domínio ou DNS.")
    print()
    print("Ideia de sobrevivência:")
    print("a planta ajuda a transformar erro confuso em investigação organizada.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def missao_producao_etapa_9():
    print()
    print("=" * 60)
    print("🏢 MISSÃO EM PRODUÇÃO: LENDO A PLANTA DA CAMPONE")
    print("=" * 60)
    print("Adria aparece na tela e olha diretamente para você.")
    print()
    print("A CampOne precisa evoluir o sistema sem se perder.")
    print()
    print("Antes de mexer em qualquer coisa, o time consulta a planta:")
    print()
    print("- o que aparece para o usuário?")
    print("- onde ficam as regras?")
    print("- onde os dados são guardados?")
    print("- por onde a tela conversa com o backend?")
    print("- quem pode acessar?")
    print("- como o sistema chega aos usuários?")
    print("- como o time registra mudanças?")
    print()
    print("A planta não é burocracia.")
    print("Ela evita que o time construa rápido a coisa errada.")
    print()
    print("Ideia de sobrevivência:")
    print("arquitetura ajuda a construir, conversar, manter e diagnosticar.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def prova_dominio_etapa_9():
    while True:
        print()
        print("=" * 60)
        print("✅ PROVA DE DOMÍNIO: A PLANTA-MESTRA")
        print("=" * 60)
        print("Adria aparece na tela e olha diretamente para você.")
        print()
        print("Um usuário tenta reservar um horário no app.")
        print("A tela monta um pedido,")
        print("a segurança confere o acesso,")
        print("o backend aplica regras,")
        print("o banco guarda a reserva,")
        print("a resposta volta")
        print("e a tela mostra a confirmação.")
        print()
        print("PERGUNTA:")
        print("Qual leitura mostra melhor essa arquitetura?")
        print()
        print("1 - A tela fez tudo sozinha e o resto do sistema não participou.")
        print("2 - O banco apareceu direto para o usuário e escolheu sozinho o resultado.")
        print("3 - Várias partes trabalharam juntas, cada uma com sua responsabilidade, formando o caminho completo do pedido.")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "3":
            print()
            print("Adria confirma.")
            print('"Isso. Essa é a visão de arquitetura."')
            print('"Cada parte tem responsabilidade, e juntas entregam a experiência ao usuário."')
            print()
            print("A planta-mestra da Academy está dominada na teoria.")
            input("Pressione Enter para voltar...")
            break
        elif escolha == "1":
            print()
            print("Adria reancora com calma.")
            print('"Quase. A tela é importante, mas não faz tudo sozinha."')
            print('"Ela participa do caminho junto com outras partes."')
            input("Pressione Enter para tentar novamente...")
        elif escolha == "2":
            print()
            print("Adria aponta para as camadas.")
            print('"Boa tentativa, mas o banco não aparece direto para o usuário."')
            print('"Ele participa por trás, junto com backend e outras camadas."')
            input("Pressione Enter para tentar novamente...")
        else:
            print()
            print("Escolha uma das opções: 1, 2 ou 3.")


def registro_etapa_9():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA — A PLANTA-MESTRA")
    print("=" * 60)
    print("Adria aparece na tela e olha diretamente para você.")
    print()
    print("Vamos registrar o que você entendeu sobre Arquitetura.")
    print()
    print("Você reconheceu que:")
    print()
    print("- arquitetura é a planta do sistema;")
    print("- cliente e servidor são lados separados que conversam;")
    print("- camadas separam responsabilidades;")
    print("- API organiza a comunicação entre partes;")
    print("- um pedido atravessa várias camadas;")
    print("- diagnóstico melhora quando o time sabe onde procurar;")
    print("- a planta-mestra junta tudo que a Academy ensinou.")
    print()
    print("Adria confirma:")
    print()
    print("Isso ainda não é programação prática.")
    print("É visão de sistema.")
    print()
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_9():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL — A PLANTA-MESTRA")
    print("=" * 60)
    print("Adria aparece na tela e olha diretamente para você.")
    print()
    print("Relatório da missão: Desenhando a Planta-Mestra")
    print()
    print("Você agora sabe que:")
    print()
    print("- a internet é o caminho;")
    print("- o backend aplica regras;")
    print("- o banco guarda memória;")
    print("- a API organiza a conversa;")
    print("- o frontend entrega a experiência visual;")
    print("- a segurança protege entrada e permissões;")
    print("- Git e GitHub guardam o histórico do time;")
    print("- deploy coloca o sistema no ar;")
    print("- arquitetura junta tudo em uma planta compreensível.")
    print()
    print("Conclusão:")
    print()
    print("Você concluiu a Academy teórica.")
    print()
    print("Agora você não enxerga mais peças soltas.")
    print("Você enxerga o sistema como uma casa inteira.")
    print()
    print("A Academy está pronta para ser fechada antes da futura consolidação da Engine.")
    print("=" * 60)

    input("Pressione Enter para voltar...")

def entrar_etapa_9():
    while True:
        print()
        print("=" * 60)
        print("09. DESENHANDO A PLANTA-MESTRA")
        print("=" * 60)
        print("Tema real: Arquitetura")
        print("Tipo: Treinamento de Sobrevivência")
        print("Status: Estrutura inicial")
        print("Mentora prevista: Adria")
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
            cena_abertura_etapa_9()
        elif escolha == "2":
            reconhecimento_etapa_9()
        elif escolha == "3":
            campo_treinamento_etapa_9()
        elif escolha == "4":
            laboratorio_falhas_etapa_9()
        elif escolha == "5":
            missao_producao_etapa_9()
        elif escolha == "6":
            prova_dominio_etapa_9()
        elif escolha == "7":
            registro_etapa_9()
        elif escolha == "8":
            relatorio_final_etapa_9()
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
        print("4 - Entrar na etapa 03: Arquivando a História do Mundo")
        print("5 - Entrar na etapa 04: Construindo a Ponte dos Mundos")
        print("6 - Entrar na etapa 05: Forjando a Interface Visual")
        print("7 - Entrar na etapa 06: Erguendo os Escudos de Defesa")
        print("8 - Entrar na etapa 07: Dominando as Linhas do Tempo")
        print("9 - Entrar na etapa 08: O Rito da Grande Implantação")
        print("10 - Entrar na etapa 09: Desenhando a Planta-Mestra")
        print("0 - Voltar ao menu do jogador")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_etapas_nivel_1()
        elif escolha == "2":
            entrar_etapa_1()
        elif escolha == "3":
            entrar_etapa_2()
        elif escolha == "4":
            entrar_etapa_3()
        elif escolha == "5":
            entrar_etapa_4()
        elif escolha == "6":
            entrar_etapa_5()
        elif escolha == "7":
            entrar_etapa_6()
        elif escolha == "8":
            entrar_etapa_7()
        elif escolha == "9":
            entrar_etapa_8()
        elif escolha == "10":
            entrar_etapa_9()
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
