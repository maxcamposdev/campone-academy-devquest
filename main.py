from engine.telas import tela_boas_vindas
from jogador.perfil import criar_jogador, mostrar_status
from engine.mapa import mostrar_mapa, mostrar_etapas_nivel_1
from academy.nivel01.etapa01.etapa import entrar_etapa_1
from academy.nivel01.etapa02.etapa import entrar_etapa_2
from academy.nivel01.etapa03.etapa import entrar_etapa_3
from academy.nivel01.etapa04.etapa import entrar_etapa_4
from academy.nivel01.etapa05.etapa import entrar_etapa_5
from academy.nivel01.etapa06.etapa import entrar_etapa_6
from academy.nivel01.etapa07.etapa import entrar_etapa_7
from academy.nivel01.etapa08.etapa import entrar_etapa_8
from academy.nivel01.etapa09.etapa import entrar_etapa_9





















































































































































































































































































































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
