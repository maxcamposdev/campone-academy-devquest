# mundo_pratico/modulo01/missao01/missao.py
# Fase A - Missão 01 (apenas navegação)

def iniciar():
    print("\n" + "="*50)
    print("MISSÃO 01 — O Primeiro Dia")
    print("="*50)
    print("\n[Versão provisória - Fase A]")
    print("Aqui entrará o conteúdo completo da missão na Fase B.")
    print("\n0 - Voltar ao Módulo 1")
    
    escolha = input("\nEscolha: ").strip()
    
    if escolha != "0":
        print("Opção inválida.")
        iniciar()
