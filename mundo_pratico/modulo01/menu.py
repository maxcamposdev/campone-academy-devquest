# mundo_pratico/modulo01/menu.py
# Fase A - Menu do Módulo 1

from .missao01 import missao as missao01

def menu_modulo_01():
    print("\n" + "="*50)
    print("📘 MÓDULO 1 — FUNDAMENTOS")
    print("="*50)
    print("1  - Missão 01 — O Primeiro Dia")
    print("2  - Missão 02 — O Estoque Fantasma (em breve)")
    print("3  - Missão 03 — O Preço que Some (em breve)")
    print("0  - Voltar ao Mundo Prático")
    
    escolha = input("\nEscolha: ").strip()
    
    if escolha == "1":
        missao01.iniciar()
        menu_modulo_01()
    elif escolha in [str(i) for i in range(2, 16)]:
        print(f"\n[Missão {escolha} ainda em construção - Fase A]")
        input("Pressione Enter para voltar...")
        menu_modulo_01()
    elif escolha == "0":
        return
    else:
        print("Opção inválida.")
        menu_modulo_01()
