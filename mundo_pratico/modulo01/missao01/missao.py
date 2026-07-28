# mundo_pratico/modulo01/missao01/missao.py
# Missão 01 — "O Primeiro Dia" (Versão Completa - Roteiro Aprovado)

caderno = []

def adicionar_ao_caderno(entrada):
    caderno.append(entrada)
    print("\n" + "─" * 55)
    print("📖 CADERNO DE CÓDIGO — Nova Entrada")
    print(entrada)
    print(f"📊 Total no Caderno: {len(caderno)} entradas")
    print("─" * 55)

def mostrar_caderno():
    print("\n" + "=" * 55)
    print("📖 SEU CADERNO DE CÓDIGO")
    print("=" * 55)
    for i, entrada in enumerate(caderno, 1):
        print(f"{i}. {entrada}")
    print("=" * 55)

def iniciar():
    print("\n" + "=" * 60)
    print("MISSÃO 01 — O Primeiro Dia")
    print("=" * 60)
    
    cena_0()
    cena_1()
    cena_2()
    cena_3()
    cena_4()
    cena_5()
    cena_6()
    cena_7()
    cena_8()
    cena_9()
    validacao_final()
    
    print("\n" + "=" * 60)
    print("📖 CADERNO DE CÓDIGO FINAL DA MISSÃO")
    print("=" * 60)
    mostrar_caderno()

# ==================== CENAS ====================

def cena_0():
    print("\n[CENA 0 — VIDEOCHAMADA COM A CAMPONE (ENCAMINHAMENTO)]")
    print("Segunda-feira. 8h.")
    print("Você está em casa. Seu celular toca.")
    print("\n👩‍💼 ELOISA — Analista de Recrutamento e Seleção (CampOne)")
    print("\nEloisa: Bom dia. Aqui é a Eloisa, da CampOne.")
    print("Você concluiu o Treinamento de Sobrevivência.")
    print("Agora começa a fase prática com nossas empresas parceiras.")
    print("\nSua primeira empresa parceira é a **Loja do Dev** (e-commerce de eletrônicos).")
    print("Eles estão com um bug no catálogo de produtos.")
    print("Quem vai te receber é o **Marcos**, o líder técnico.")
    print("\nLá dentro você não é mais recruta. É parte do time.")
    print("Se errar, tudo bem — mas precisa entender por que errou.")
    input("\nPressione Enter para continuar...")

def cena_1():
    print("\n[CENA 1 — CHEGADA NA EMPRESA PARCEIRA]")
    print("Você desliga a chamada e vai direto para a sede da Loja do Dev.")
    print("\n🏢 LOJA DO DEV — SEU PRIMEIRO DIA")
    print("Segunda-feira. 9h da manhã.")
    print("Você passa o crachá na catraca.")
    print("É o dev mais novo do time.")
    input("\nPressione Enter para continuar...")

def cena_2():
    print("\n[CENA 2 — PRIMEIRO CONTATO COM MARCOS]")
    print("Um homem de uns 35 anos levanta da cadeira.")
    print("\n👨‍💼 MARCOS — Líder Técnico")
    print("\nMarcos: E aí. Você é o trainee novo que a CampOne mandou?")
    print("\nMe chamo Marcos. Sou o Líder Técnico aqui. Cuido do sistema inteiro — backend, frontend, banco, deploy.")
    print("Você vai responder direto pra mim.")
    print("\nVamos direto ao ponto. A gente tá com um problema no catálogo.")
    input("\nPressione Enter para continuar...")

def cena_3():
    print("\n[CENA 3 — O BUG]")
    print("👨‍💼 MARCOS")
    print("\nMarcos: Bom, vou ser direto. A gente tá com um problema.")
    print("Nosso catálogo de produtos tá bugado.")
    print("O cliente abre a página do Teclado Mecânico RGB e o preço aparece errado às vezes.")
    print("\nNome e estoque aparecem corretos. Só o preço oscila.")
    print("\nVocê é trainee, então não vai resolver sozinho.")
    print("Mas vai acompanhar e entender o que tá acontecendo.")
    input("\nPressione Enter para continuar...")

def cena_4():
    print("\n[CENA 4 — FLUXO DO SISTEMA]")
    print("👨‍💼 MARCOS")
    print("\nMarcos: O frontend é só um espelho. Ele mostra o que recebe.")
    print("O backend pega os dados do banco, processa e manda pro frontend.")
    print("O banco só guarda. Não processa nada sozinho.")
    input("\nPressione Enter para continuar...")

def cena_5():
    print("\n[CENA 5 — INVESTIGANDO O BANCO]")
    print("👨‍💼 MARCOS")
    print("\nMarcos: Antes de olhar o código, vamos checar a fonte — o banco de dados.")
    print("\nTabela: produtos")
    print("Teclado Mecânico RGB → preco = 249.90 (correto)")
    print("\nMarcos: O banco está certo. O problema está depois que o dado sai do banco.")
    input("\nPressione Enter para continuar...")

def cena_6():
    print("\n[CENA 6 — PRIMEIRO CONTATO COM CÓDIGO + ENSINO DE SINTAXE]")
    print("👨‍💼 MARCOS")
    print("\nMarcos: Vamos abrir o código do backend. É aqui que o backend pega o preço do banco e prepara pra mandar pro frontend.")
    print("\n**Antes de mostrar, uma coisa importante:**")
    print("Esse código tá escrito em **Python** — é a linguagem de programação que a gente usa aqui.")
    print("Linguagem de programação é como uma receita: você escreve passo a passo o que o computador precisa fazer.")
    input("\nPressione Enter para continuar...")

    print("\nMarcos abre o arquivo e começa a explicar com calma:")

    # Comentários
    print("\n📌 Primeiro: Comentários")
    print('''Marcos: Tá vendo essas linhas que começam com # ? Isso se chama **comentário**.
O computador **ignora** comentários — eles são só pra gente ler e entender o código.''')
    print('''
# Buscar produto no banco
produto = banco.buscar("Teclado Mecanico RGB")
''')
    adicionar_ao_caderno("🐍 # (hashtag)\n   Comentário — o computador ignora.\n   Serve pra explicar o código pra quem lê.\n   📂 Sintaxe Básica | 📅 Dia 1")

    input("\nPressione Enter para continuar...")

    # Variáveis e =
    print("\n📌 Segundo: Variáveis e o sinal =")
    print('''Marcos: Cada uma dessas linhas cria uma **variável**.
Variável é como uma **gaveta com nome** onde a gente guarda informação.

O símbolo = **não significa "é igual a"** como na matemática.
Em programação, = significa "**guarde isso aqui**". É uma ordem.''')
    print('''
nome = produto.nome          # Cria gaveta chamada 'nome'
preco = produto.preco        # Cria gaveta chamada 'preco'
estoque = produto.estoque    # Cria gaveta chamada 'estoque'
''')
    adicionar_ao_caderno("🐍 variável\n   Gaveta com nome que guarda informação na memória do computador.\n   📂 Conceito | 📅 Dia 1")
    adicionar_ao_caderno("🐍 =\n   Atribuição — 'guarde isso aqui'.\n   NÃO é 'igual a' da matemática.\n   📂 Operador | 📅 Dia 1")

    input("\nPressione Enter para continuar...")

    # Tipos de dado
    print("\n📌 Terceiro: Tipos de Dado")
    print('''Marcos: Agora olha o que a gente guardou em cada gaveta:''')
    print('''
nome = "Teclado Mecanico RGB"   # Texto (string) — entre aspas
preco = 249.90                  # Número decimal (float) — com ponto
estoque = 15                    # Número inteiro (int)
disponivel = True               # Booleano (bool) — Verdadeiro ou Falso
''')
    print("Marcos: O Python trata cada tipo de forma diferente. E tem coisas que você **não pode fazer** com certos tipos.")
    adicionar_ao_caderno("🐍 Tipos de dado:\n   - str (string): texto entre aspas\n   - int: número inteiro (sem ponto)\n   - float: número com ponto\n   - bool: True ou False\n   📂 Conceito | 📅 Dia 1")

    input("\nPressione Enter para continuar...")

    print("\nMarcos: Beleza. Agora que você entendeu o básico, olha o código de novo com calma.")

def cena_7():
    print("\n[CENA 7 — O CÓDIGO COM O ERRO]")
    print("Marcos mostra o código completo:")
    print('''
desconto = "10"
preco_final = preco - desconto
''')
    print("\nMarcos: Consegue encontrar onde o preço está sendo estragado?")
    input("\nPressione Enter para continuar...")

def cena_8():
    print("\n[CENA 8 — RESOLUÇÃO + TYPEERROR]")
    print("👨‍💼 MARCOS")
    print("\nMarcos: O problema está aqui:")
    print('  desconto = "10"     ← Isso é TEXTO (string)')
    print('  preco_final = preco - desconto')
    print("\nMarcos: Você não consegue subtrair texto de número. Isso gera um erro chamado TypeError.")
    print("\nCorreção:")
    print('  desconto = 10       ← Agora é NÚMERO')
    print('  preco_final = preco - 10   # 239.90')
    adicionar_ao_caderno("🐍 TypeError\n   Erro de tipo — tentar fazer operação com tipos incompatíveis.\n   Ex: subtrair texto de número.\n   📂 Erro | 📅 Dia 1")
    input("\nPressione Enter para continuar...")

def cena_9():
    print("\n[CENA 9 — REVISÃO DO DIA]")
    print("👨‍💼 MARCOS")
    print("\nMarcos: Antes de ir embora, vamos recapitular o que rolou hoje.")
    print("\nVocê aprendeu:")
    print("• Variáveis são gavetas com nome que guardam informação")
    print("• O sinal = significa 'guarde isso aqui'")
    print("• Aspas = texto (string). Sem aspas = número")
    print("• Comentários começam com #")
    print("• Não dá para fazer conta com texto")
    print("• O frontend só mostra o que o backend entrega")
    input("\nPressione Enter para continuar...")

def validacao_final():
    print("\n" + "=" * 60)
    print("VALIDAÇÃO DE FIM DE DIA")
    print("=" * 60)

    pergunta_1()
    pergunta_2()

    print("\n" + "=" * 60)
    print("✅ MISSÃO 01 CONCLUÍDA")
    print("=" * 60)
    print("\nO que você aprendeu:")
    print("• Variáveis e atribuição (=)")
    print("• Tipos de dado (string vs número)")
    print("• Fluxo: Frontend ← Backend ← Banco")
    print("• Como um erro pequeno pode quebrar o sistema")
    print("\nReputação na Loja do Dev: +10")
    print("Próxima missão: Missão 02 — O Estoque Fantasma")
    input("\nPressione Enter para voltar ao menu...")

def pergunta_1():
    tentativas = 0
    while tentativas < 3:
        print("\nPergunta 1 de 2:")
        print("No Python, qual a diferença entre 10 e \"10\"?")
        print("[1] Não tem diferença, são a mesma coisa.")
        print("[2] 10 sem aspas é número. '10' com aspas é texto.")
        print("[3] 10 é pra fazer conta e '10' é pra mostrar na tela.")

        resposta = input("\nSua resposta: ").strip()

        if resposta == "2":
            print("\nCorreto! Você entendeu a diferença entre número e texto. +XP")
            return
        elif resposta == "1":
            print("\nMarcos: Não exatamente. Em Python, aspas mudam o tipo do dado.")
            print("10 sem aspas = número (pode fazer contas).")
            print("'10' com aspas = texto (string). O Python trata como letras.")
        elif resposta == "3":
            print("\nMarcos: Quase. A diferença não é o uso, é o **tipo**.")
            print("10 sem aspas é número. '10' com aspas é texto.")
            print("Você não consegue fazer conta com texto.")
        else:
            print("\nMarcos: Resposta inválida.")

        tentativas += 1
        if tentativas < 3:
            print("Tente novamente.\n")
        else:
            print("\nMarcos: A resposta correta é a [2].")
            print("10 sem aspas = número. '10' com aspas = texto (string).")

def pergunta_2():
    tentativas = 0
    while tentativas < 3:
        print("\nPergunta 2 de 2:")
        print("O que o sinal = faz em programação?")
        print("[1] Compara se dois valores são iguais.")
        print("[2] Guarda um valor dentro de uma variável.")
        print("[3] Mostra o resultado na tela.")

        resposta = input("\nSua resposta: ").strip()

        if resposta == "2":
            print("\nPerfeito! O = é atribuição: 'guarde isso aqui'. +XP")
            return
        elif resposta == "1":
            print("\nMarcos: Cuidado. Comparar é com **dois** sinais: ==.")
            print("Um só sinal (=) é para guardar valor em uma variável.")
        elif resposta == "3":
            print("\nMarcos: Não. Para mostrar na tela usamos print().")
            print("O = serve para criar ou atualizar uma variável.")
        else:
            print("\nMarcos: Resposta inválida.")

        tentativas += 1
        if tentativas < 3:
            print("Tente novamente.\n")
        else:
            print("\nMarcos: A resposta correta é a [2].")
            print("O sinal = guarda um valor dentro de uma variável.")

