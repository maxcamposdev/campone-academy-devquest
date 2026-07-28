"""Etapa 03 — Arquivando a História do Mundo."""

def topico_banco_dados():
    while True:
        print()
        print("=" * 60)
        print("🗄️ TÓPICO 1: BANCO DE DADOS")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print('"Todo sistema precisa ter memória."')
        print()
        print("Pensa em um aplicativo de banco, loja ou agenda.")
        print("Se ele esquecesse tudo quando fechasse, não serviria para quase nada.")
        print()
        print("O banco de dados existe para isso:")
        print("guardar informações importantes de forma organizada.")
        print()
        print("É ali que podem ficar clientes, produtos, pedidos, reservas")
        print("e o histórico do que aconteceu no sistema.")
        print()
        print("Pergunta de domínio:")
        print("Por que um sistema precisa de um banco de dados?")
        print()
        print("1 - Para guardar informações importantes de forma organizada e não esquecer tudo quando o programa fecha.")
        print("2 - Para escolher as cores e os botões que aparecem na tela.")
        print("3 - Para substituir o backend e processar todas as regras sozinho.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Letícia confirma.")
            print('"Isso. O banco de dados é a memória organizada do sistema."')
            print('"Ele guarda informações importantes para que o sistema não esqueça clientes, produtos, pedidos e históricos."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Letícia aponta para a tela.")
            print('"Essa opção fala da aparência visual."')
            print('"Cores e botões pertencem ao frontend."')
            print('"O banco não cuida da aparência; ele cuida da memória do sistema."')
            print()
            print('"Tenta de novo pensando no que o sistema precisa lembrar."')
        elif escolha == "3":
            print("Letícia aponta para a cozinha do sistema.")
            print('"Essa opção mistura banco com backend."')
            print('"O backend processa regras. O banco guarda informações para que essas regras tenham dados para consultar."')
            print()
            print('"Tenta de novo pensando em memória, não em processamento."')
        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_sql():
    while True:
        print()
        print("=" * 60)
        print("🧾 TÓPICO 2: SQL")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print('"Guardar informação não basta. O sistema também precisa pedir essa informação de volta."')
        print()
        print("Imagine uma despensa enorme cheia de gavetas.")
        print("Se ninguém souber pedir o que precisa, a informação fica perdida lá dentro.")
        print()
        print("SQL é a forma usada para conversar com muitos bancos de dados.")
        print("Com ele, o sistema pode pedir, guardar, alterar ou remover informações.")
        print()
        print("Você não precisa decorar comandos agora.")
        print("Por enquanto, entenda só o papel:")
        print("SQL é a língua usada para falar com a despensa dos dados.")
        print()
        print("Pergunta de domínio:")
        print("Qual é o papel do SQL em um sistema que usa banco de dados?")
        print()
        print("1 - Ser a forma usada para conversar com o banco e pedir informações.")
        print("2 - Ser a tela onde o usuário vê botões, cores e textos.")
        print("3 - Ser o lugar físico onde os dados ficam guardados para sempre.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Letícia confirma.")
            print('"Isso. SQL é a forma de conversar com muitos bancos de dados."')
            print('"Com ele, o sistema pode pedir, guardar, alterar ou remover informações."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Letícia aponta para a tela.")
            print('"Essa opção fala do frontend."')
            print('"A tela mostra informações para o usuário."')
            print('"SQL não é tela; SQL é a forma de conversar com o banco."')
            print()
            print('"Tenta de novo pensando na língua da despensa."')
        elif escolha == "3":
            print("Letícia aponta para a despensa.")
            print('"Essa opção fala do banco de dados em si."')
            print('"O banco é onde a informação fica guardada."')
            print('"SQL é a forma de pedir algo para essa despensa."')
            print()
            print('"Tenta de novo pensando na conversa com o banco."')
        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_tabelas():
    while True:
        print()
        print("=" * 60)
        print("📊 TÓPICO 3: TABELAS")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print('"Uma memória bagunçada também vira problema."')
        print()
        print("Imagine jogar clientes, produtos e pedidos todos na mesma gaveta.")
        print("Na hora de procurar qualquer coisa, seria um caos.")
        print()
        print("Por isso o banco separa as informações em tabelas.")
        print("Uma tabela pode guardar clientes.")
        print("Outra pode guardar produtos.")
        print("Outra pode guardar pedidos.")
        print()
        print("Pergunta de domínio:")
        print("Para que servem as tabelas dentro de um banco de dados?")
        print()
        print("1 - Para separar e organizar tipos diferentes de informação, como clientes, produtos e pedidos.")
        print("2 - Para decidir as regras de desconto e permissão do sistema.")
        print("3 - Para desenhar a tela que o usuário vê no aplicativo.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Letícia confirma.")
            print('"Isso. Tabelas são como gavetas organizadas dentro do banco."')
            print('"Cada tabela guarda um tipo de informação, para o sistema não misturar tudo."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Letícia aponta para o motor do sistema.")
            print('"Essa opção fala de lógica de negócio."')
            print('"Regras de desconto e permissão são decisões do sistema."')
            print('"Tabelas servem para organizar dados guardados."')
            print()
            print('"Tenta de novo pensando em gavetas de informações."')
        elif escolha == "3":
            print("Letícia aponta para a tela.")
            print('"Essa opção fala do frontend."')
            print('"A tela mostra informações para o usuário."')
            print('"Tabelas ficam no banco, organizando os dados que o sistema precisa lembrar."')
            print()
            print('"Tenta de novo pensando na despensa dos dados."')
        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_registros_colunas():
    while True:
        print()
        print("=" * 60)
        print("📋 TÓPICO 4: REGISTROS E COLUNAS")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print('"Depois de abrir uma gaveta, você precisa entender como as fichas são organizadas."')
        print()
        print("Dentro de uma tabela, cada item guardado é como uma ficha.")
        print("Essa ficha é o registro.")
        print()
        print("As informações dentro da ficha são as colunas.")
        print()
        print("Exemplo:")
        print("- um produto é um registro;")
        print("- nome, preço e estoque são colunas desse produto.")
        print()
        print("Pergunta de domínio:")
        print("Dentro de uma tabela, o que são registros e colunas?")
        print()
        print("1 - Registro é uma ficha/linha da tabela, e coluna é uma informação dessa ficha.")
        print("2 - Registro é a cor da tela, e coluna é o botão que o usuário clica.")
        print("3 - Registro é o servidor inteiro, e coluna é a internet por onde o pedido viaja.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Letícia confirma.")
            print('"Isso. Registro é uma ficha dentro da tabela."')
            print('"Colunas são as informações dessa ficha, como nome, preço ou estoque."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Letícia aponta para a tela.")
            print('"Essa opção mistura banco com frontend."')
            print('"Cores e botões pertencem à interface visual."')
            print('"Registro e coluna são organização interna dos dados."')
            print()
            print('"Tenta de novo pensando nas fichas dentro da tabela."')
        elif escolha == "3":
            print("Letícia aponta para o caminho da Grande Rede.")
            print('"Essa opção mistura banco com servidor e internet."')
            print('"Servidor e internet fazem parte do caminho do pedido."')
            print('"Registro e coluna ficam dentro da tabela, organizando os dados."')
            print()
            print('"Tenta de novo pensando na gaveta do banco."')
        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_chave_primaria():
    while True:
        print()
        print("=" * 60)
        print("🔑 TÓPICO 5: CHAVE PRIMÁRIA")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print('"Quando existem muitas fichas, o sistema precisa saber exatamente qual é qual."')
        print()
        print("Imagine dois clientes com o mesmo nome.")
        print("Só o nome não basta para saber quem é quem.")
        print()
        print("Por isso cada registro precisa de uma identificação única.")
        print("Essa identificação é a chave primária.")
        print()
        print("Na prática, ela costuma aparecer como um ID.")
        print("Esse ID ajuda o sistema a buscar, alterar ou apagar a ficha certa.")
        print()
        print("Pergunta de domínio:")
        print("Para que serve uma chave primária em uma tabela?")
        print()
        print("1 - Para identificar de forma única cada registro da tabela.")
        print("2 - Para escolher a cor da tela onde os dados aparecem.")
        print("3 - Para conectar a internet ao servidor da aplicação.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Letícia confirma.")
            print('"Isso. A chave primária é a identificação única de uma ficha."')
            print('"Ela ajuda o banco a saber exatamente qual registro buscar, alterar ou apagar."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Letícia aponta para a tela.")
            print('"Essa opção fala de aparência visual."')
            print('"A cor da tela não identifica uma ficha no banco."')
            print('"Chave primária serve para diferenciar registros."')
            print()
            print('"Tenta de novo pensando em identificação única."')
        elif escolha == "3":
            print("Letícia aponta para a estrada da rede.")
            print('"Essa opção mistura banco com internet."')
            print('"Conectar internet ao servidor faz parte do caminho da rede."')
            print('"Chave primária vive dentro da tabela, ajudando o banco a encontrar um registro específico."')
            print()
            print('"Tenta de novo pensando em como o banco sabe quem é quem."')
        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_chave_estrangeira():
    while True:
        print()
        print("=" * 60)
        print("🔗 TÓPICO 6: CHAVE ESTRANGEIRA")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print('"Algumas fichas precisam lembrar de outras fichas."')
        print()
        print("Um pedido, por exemplo, precisa saber de qual cliente ele é.")
        print("Em vez de copiar todos os dados do cliente dentro do pedido,")
        print("o sistema guarda uma referência para o cliente certo.")
        print()
        print("Essa ligação é chamada de chave estrangeira.")
        print()
        print("Ela aponta de uma tabela para outra.")
        print("Assim, pedido e cliente continuam conectados sem repetir tudo.")
        print()
        print("Pergunta de domínio:")
        print("Para que serve uma chave estrangeira em um banco de dados?")
        print()
        print("1 - Para ligar uma informação de uma tabela a um registro de outra tabela.")
        print("2 - Para dar uma cor diferente para cada linha da tela.")
        print("3 - Para apagar todos os dados repetidos automaticamente.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Letícia confirma.")
            print('"Isso. A chave estrangeira cria uma ligação entre tabelas."')
            print('"Ela permite que um pedido lembre de qual cliente ele pertence, sem copiar todos os dados do cliente."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Letícia aponta para a tela.")
            print('"Essa opção fala de aparência visual."')
            print('"Cor de linha é coisa de interface."')
            print('"Chave estrangeira não pinta nada; ela conecta informações."')
            print()
            print('"Tenta de novo pensando em uma ficha lembrando de outra."')
        elif escolha == "3":
            print("Letícia balança a cabeça com calma.")
            print('"Essa opção parece útil, mas não é o papel da chave estrangeira."')
            print('"Ela ajuda a evitar repetição porque conecta dados, mas não sai apagando tudo automaticamente."')
            print()
            print('"Tenta de novo pensando em ligação entre tabelas."')
        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def topico_relacionamento():
    while True:
        print()
        print("=" * 60)
        print("🔄 TÓPICO 7: RELACIONAMENTO")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print('"Agora que você viu as fichas, precisa entender como elas se conectam."')
        print()
        print("Em um sistema real, as informações não vivem isoladas.")
        print("Um cliente pode ter vários pedidos.")
        print("Um pedido pode ter vários produtos.")
        print()
        print("Relacionamento é essa ligação entre tabelas.")
        print()
        print("Ele ajuda o sistema a responder perguntas como:")
        print("- quais pedidos pertencem a este cliente?")
        print("- quais produtos fazem parte deste pedido?")
        print("- qual cliente fez esta compra?")
        print()
        print("Pergunta de domínio:")
        print("O que é um relacionamento entre tabelas?")
        print()
        print("1 - Uma ligação que mostra como informações de tabelas diferentes se conectam.")
        print("2 - Uma imagem que aparece na tela para o usuário clicar.")
        print("3 - Um comando que apaga todos os registros antigos do banco.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")

        print()

        if escolha == "1":
            print("Letícia confirma.")
            print('"Isso. Relacionamento é a ligação entre tabelas."')
            print('"Ele permite que o sistema entenda, por exemplo, quais pedidos pertencem a um cliente."')
            print()
            print("Tópico validado nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break
        elif escolha == "2":
            print("Letícia aponta para a tela.")
            print('"Essa opção fala da interface visual."')
            print('"Relacionamento não é algo que o usuário clica na tela."')
            print('"Ele fica no banco, conectando informações."')
            print()
            print('"Tenta de novo pensando em tabelas que precisam conversar."')
        elif escolha == "3":
            print("Letícia levanta a mão com calma.")
            print('"Essa opção fala de apagar dados."')
            print('"Relacionamento não apaga registros."')
            print('"Ele ajuda o banco a entender como um dado se liga a outro."')
            print()
            print('"Tenta de novo pensando em conexão, não em exclusão."')
        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')


def reconhecimento_etapa_3():
    while True:
        print()
        print("=" * 60)
        print("💡 RECONHECIMENTO: A DESPENSA DOS DADOS")
        print("=" * 60)
        print("Letícia organiza os primeiros conceitos de Banco de Dados.")
        print()
        print("1 - Banco de Dados")
        print("2 - SQL")
        print("3 - Tabelas")
        print("4 - Registros e Colunas")
        print("5 - Chave Primária")
        print("6 - Chave Estrangeira")
        print("7 - Relacionamento")
        print("0 - Voltar à etapa 03")
        print("=" * 60)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            topico_banco_dados()
        elif escolha == "2":
            topico_sql()
        elif escolha == "3":
            topico_tabelas()
        elif escolha == "4":
            topico_registros_colunas()
        elif escolha == "5":
            topico_chave_primaria()
        elif escolha == "6":
            topico_chave_estrangeira()
        elif escolha == "7":
            topico_relacionamento()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")


def campo_treinamento_etapa_3():
    print()
    print("=" * 60)
    print("🛠 CAMPO DE TREINAMENTO: SEGUINDO UMA INFORMAÇÃO")
    print("=" * 60)
    print("Letícia aparece na tela e olha diretamente para você.")
    print()
    print('"Agora vamos seguir uma informação dentro da despensa."')
    print()
    print("Imagine que um cliente faz uma compra na CampOne.")
    print()
    print("O sistema precisa guardar essa história:")
    print()
    print("1. O cliente existe na tabela de clientes.")
    print("2. O produto existe na tabela de produtos.")
    print("3. O pedido vira um novo registro na tabela de pedidos.")
    print("4. O pedido recebe uma chave primária própria.")
    print("5. O pedido guarda uma chave estrangeira apontando para o cliente.")
    print("6. O pedido também se relaciona com os produtos comprados.")
    print()
    print("Assim o sistema consegue responder depois:")
    print("- quem comprou?")
    print("- o que comprou?")
    print("- quando comprou?")
    print("- qual pedido pertence a qual cliente?")
    print()
    print("Resumo de sobrevivência:")
    print("- Banco guarda a história.")
    print("- Tabelas organizam a história.")
    print("- Chaves ligam as partes da história.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def laboratorio_falhas_etapa_3():
    print()
    print("=" * 60)
    print("🧪 LABORATÓRIO DE FALHAS: QUANDO A DESPENSA BAGUNÇA")
    print("=" * 60)
    print("Letícia aparece na tela e olha diretamente para você.")
    print()
    print('"Dados também quebram sistemas quando estão mal organizados."')
    print()
    print("Algumas falhas comuns no banco:")
    print()
    print("1. Registro duplicado")
    print("- duas fichas representam a mesma coisa sem necessidade.")
    print()
    print("2. Dado sem identificação")
    print("- o sistema não sabe exatamente qual ficha deve buscar.")
    print()
    print("3. Ligação quebrada")
    print("- um pedido aponta para um cliente que não existe.")
    print()
    print("4. Informação no lugar errado")
    print("- dado de produto misturado com dado de cliente.")
    print()
    print("Resumo de sobrevivência:")
    print("- Banco bagunçado gera resposta bagunçada.")
    print("- Chaves ajudam o sistema a não se perder.")
    print("- Dados bem organizados evitam muitos bugs.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def missao_producao_etapa_3():
    print()
    print("=" * 60)
    print("🏢 MISSÃO EM PRODUÇÃO: DADOS NO DIA A DIA")
    print("=" * 60)
    print("Letícia aparece na tela e olha diretamente para você.")
    print()
    print('"Agora vamos ver a despensa funcionando em uma situação real."')
    print()
    print("Imagine um e-commerce recebendo uma compra.")
    print()
    print("O sistema precisa guardar:")
    print("- quem comprou;")
    print("- qual produto foi comprado;")
    print("- qual foi o valor;")
    print("- quando o pedido aconteceu;")
    print("- qual é o status da entrega.")
    print()
    print("Essas informações não podem ficar soltas.")
    print("Elas precisam entrar nas tabelas certas e se conectar corretamente.")
    print()
    print("Assim, depois o sistema consegue responder:")
    print("- quais pedidos um cliente fez?")
    print("- quais produtos saíram do estoque?")
    print("- qual compra ainda está pendente?")
    print()
    print("Resumo de sobrevivência:")
    print("- Banco bem organizado sustenta decisões reais.")
    print("- Dados conectados ajudam o sistema a contar a história.")
    print("- Sem organização, o negócio perde confiança.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def prova_dominio_etapa_3():
    tentativas = 0

    while True:
        print()
        print("=" * 60)
        print("🧠 PROVA DE DOMÍNIO — DESPENSA DOS DADOS")
        print("=" * 60)
        print("Letícia aparece na tela e olha diretamente para você.")
        print()
        print("Um cliente faz uma compra em uma loja online.")
        print("O sistema precisa guardar quem comprou, o que comprou e qual pedido foi gerado.")
        print("Qual caminho representa melhor a organização correta desses dados?")
        print()
        print("1 - Guardar tudo em uma única gaveta misturada, sem separar cliente, produto e pedido.")
        print("2 - Separar os dados em tabelas, dar identificação única aos registros e ligar pedido, cliente e produto por relacionamentos.")
        print("3 - Deixar a tela guardar tudo sozinha, porque é nela que o cliente faz a compra.")
        print("=" * 60)

        escolha = input("Escolha uma resposta: ")
        tentativas += 1

        print()

        if escolha == "2":
            print("Letícia confirma.")
            print('"Isso. Você enxergou a despensa funcionando."')
            print('"Clientes, produtos e pedidos ficam organizados em tabelas."')
            print('"Cada registro precisa de identificação, e as relações mostram como uma informação se conecta à outra."')
            print()
            print("Prova de Domínio concluída nesta versão.")
            print("Ainda não há XP, recompensa ou progresso salvo.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break

        elif escolha == "1":
            print("Letícia aponta para uma gaveta bagunçada.")
            print('"Essa opção cria confusão."')
            print('"Se tudo fica misturado, o sistema não sabe encontrar com segurança quem comprou, o que comprou e qual pedido foi gerado."')
            print()
            print('"Tenta de novo pensando em gavetas separadas e organizadas."')

        elif escolha == "3":
            print("Letícia aponta para a tela.")
            print('"Essa opção coloca responsabilidade demais no frontend."')
            print('"A tela inicia a compra e mostra informações, mas quem guarda a história é o banco de dados."')
            print()
            print('"Tenta de novo pensando em onde o sistema guarda memória."')

        else:
            print("Letícia inclina a cabeça.")
            print('"Escolha uma das opções: 1, 2 ou 3."')
            tentativas -= 1

        if tentativas >= 3:
            print()
            print("Letícia se aproxima com calma.")
            print('"Vamos fechar juntos."')
            print('"A resposta certa é a opção 2."')
            print()
            print('"O sistema organiza clientes, produtos e pedidos em tabelas."')
            print('"Cada registro tem uma identificação, e as ligações entre tabelas mostram como uma compra pertence a um cliente e envolve produtos."')
            print()
            print('"Essa é a história do mundo ficando arquivada."')
            print()
            print("A prova segue sem punição nesta versão.")
            print("=" * 60)
            input("Pressione Enter para voltar...")
            break


def registro_etapa_3():
    print()
    print("=" * 60)
    print("📝 REGISTRAR EXPERIÊNCIA — DESPENSA DOS DADOS")
    print("=" * 60)
    print("Letícia aparece na tela e olha diretamente para você.")
    print()
    print('"Toda informação bem guardada ajuda o sistema a lembrar sua própria história."')
    print()
    print("Nesta etapa, você começou a reconhecer o banco de dados:")
    print()
    print("- entendeu que o sistema precisa ter memória;")
    print("- viu que SQL é uma forma de conversar com o banco;")
    print("- conheceu tabelas, registros e colunas;")
    print("- entendeu chave primária e chave estrangeira;")
    print("- viu que relacionamentos conectam informações;")
    print("- acompanhou como uma compra pode virar história guardada.")
    print()
    print("Registro atual:")
    print("Experiência registrada apenas na narrativa.")
    print("Salvamento real será criado em uma fase futura.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def relatorio_final_etapa_3():
    print()
    print("=" * 60)
    print("📋 RELATÓRIO FINAL — DESPENSA DOS DADOS")
    print("=" * 60)
    print("Letícia aparece na tela e olha diretamente para você.")
    print()
    print('"Antes de seguir, revise o que você encontrou na despensa dos dados."')
    print()
    print("Relatório da missão: Arquivando a História do Mundo")
    print()
    print("Você agora sabe que:")
    print()
    print("- banco de dados é a memória organizada do sistema;")
    print("- SQL é uma forma de conversar com o banco;")
    print("- tabelas separam tipos de informação;")
    print("- registros são fichas dentro das tabelas;")
    print("- colunas são informações dessas fichas;")
    print("- chave primária identifica um registro;")
    print("- chave estrangeira conecta tabelas;")
    print("- relacionamentos mostram como as informações dependem umas das outras.")
    print()
    print("Conclusão:")
    print("Você começou a entender como o sistema guarda sua própria história.")
    print()
    print("A etapa ainda não marca conclusão permanente nesta versão.")
    print("=" * 60)

    input("Pressione Enter para voltar...")


def entrar_etapa_3():
    while True:
        print()
        print("=" * 60)
        print("03. ARQUIVANDO A HISTÓRIA DO MUNDO")
        print("=" * 60)
        print("Tema real: Banco de Dados")
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
            print()
            print("Cena da etapa 03 já foi apresentada na primeira versão.")
            print("A ponte David → Letícia será refinada em seguida.")
        elif escolha == "2":
            reconhecimento_etapa_3()
        elif escolha == "3":
            campo_treinamento_etapa_3()
        elif escolha == "4":
            laboratorio_falhas_etapa_3()
        elif escolha == "5":
            missao_producao_etapa_3()
        elif escolha == "6":
            prova_dominio_etapa_3()
        elif escolha == "7":
            registro_etapa_3()
        elif escolha == "8":
            relatorio_final_etapa_3()
        elif escolha == "0":
            break
        else:
            print()
            print("Opção inválida.")
