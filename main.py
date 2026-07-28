from engine.telas import tela_boas_vindas
from jogador.perfil import criar_jogador, mostrar_status
from engine.mapa import mostrar_mapa, mostrar_etapas_nivel_1
from academy.nivel01.etapa01.etapa import entrar_etapa_1
from academy.nivel01.etapa02.etapa import entrar_etapa_2
from academy.nivel01.etapa03.etapa import entrar_etapa_3
from academy.nivel01.etapa04.etapa import entrar_etapa_4
from academy.nivel01.etapa05.etapa import entrar_etapa_5
from academy.nivel01.etapa06.etapa import entrar_etapa_6































































































































































































































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
