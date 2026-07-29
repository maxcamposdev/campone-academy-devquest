"""Camada visual simples da Engine.

Este módulo centraliza funções visuais reutilizáveis do terminal.
A ideia é melhorar a aparência do jogo sem alterar a lógica.
"""

LARGURA_PADRAO = 60


def linha(caractere="=", largura=LARGURA_PADRAO):
    """Mostra uma linha horizontal simples."""
    print(caractere * largura)


def titulo(texto, subtitulo=None, largura=LARGURA_PADRAO):
    """Mostra um título centralizado."""
    print()
    linha("=", largura)
    print(texto.center(largura))
    if subtitulo:
        print(subtitulo.center(largura))
    linha("=", largura)


def caixa(linhas, largura=LARGURA_PADRAO):
    """Mostra uma caixa simples com várias linhas de texto."""
    print("╔" + "═" * (largura - 2) + "╗")
    for linha_texto in linhas:
        texto = str(linha_texto)
        print("║ " + texto[: largura - 4].ljust(largura - 4) + " ║")
    print("╚" + "═" * (largura - 2) + "╝")


def separador(largura=LARGURA_PADRAO):
    """Mostra um separador visual."""
    linha("-", largura)


def menu(opcoes, largura=LARGURA_PADRAO):
    """Mostra uma lista de opções de menu."""
    separador(largura)
    for numero, texto in opcoes:
        print(f"{numero} - {texto}")
    separador(largura)


def pausar(mensagem="Pressione Enter para continuar..."):
    """Pausa a execução até o jogador pressionar Enter."""
    input(f"\n{mensagem}")


def mensagem_sistema(texto):
    """Mostra uma mensagem do sistema ou coordenação da jornada."""
    print()
    print("🎙️ COORDENADORA DA JORNADA")
    separador()
    print(texto)


def mensagem_personagem(nome, texto):
    """Mostra uma fala de personagem."""
    print()
    print(nome)
    separador()
    print(f'"{texto}"')


def mostrar_codigo(caminho, codigo):
    """Mostra um bloco de código com cabeçalho."""
    print()
    caixa([f"📄 {caminho}"])
    print(codigo)
