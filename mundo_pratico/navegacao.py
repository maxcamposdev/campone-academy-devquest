# mundo_pratico/navegacao.py
# Fase A - Navegação do Mundo Prático (particionada)

from .modulo01 import menu as modulo01_menu

def entrar_mundo_pratico():
    print("\n" + "="*50)
    print("🌍 MUNDO PRÁTICO")
    print("="*50)
    print("1 - Módulo 1 — Fundamentos")
    print("2 - Módulo 2 — Persistência e APIs (em breve)")
    print("0 - Voltar ao menu principal")
    
    escolha = input("\nEscolha: ").strip()
    
    if escolha == "1":
        modulo01_menu.menu_modulo_01()
        entrar_mundo_pratico()
    elif escolha == "2":
        print("\n[Módulo 2 ainda em construção - Fase A]")
        input("Pressione Enter para voltar...")
        entrar_mundo_pratico()
    elif escolha == "0":
        return
    else:
        print("Opção inválida.")
        entrar_mundo_pratico()
