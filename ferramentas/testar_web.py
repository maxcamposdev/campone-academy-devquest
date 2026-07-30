from pathlib import Path
import json
import sys

ERROS = []

def ok(msg):
    print(f"✅ {msg}")

def erro(msg):
    print(f"❌ {msg}")
    ERROS.append(msg)

def existe(caminho):
    p = Path(caminho)
    if p.exists():
        ok(f"Existe: {caminho}")
        return p
    erro(f"Não encontrado: {caminho}")
    return p

def contem(caminho, texto):
    p = Path(caminho)
    if not p.exists():
        erro(f"Arquivo não existe para busca: {caminho}")
        return

    conteudo = p.read_text(encoding="utf-8")
    if texto in conteudo:
        ok(f"{caminho} contém: {texto}")
    else:
        erro(f"{caminho} NÃO contém: {texto}")

def validar_json(caminho):
    p = existe(caminho)
    if not p.exists():
        return None

    try:
        dados = json.loads(p.read_text(encoding="utf-8"))
        ok(f"JSON válido: {caminho}")
        return dados
    except Exception as exc:
        erro(f"JSON inválido em {caminho}: {exc}")
        return None

print("=== TESTE WEB CAMPONE ===")

# Arquivos principais
existe("web/frontend/index.html")
existe("web/frontend/pages/mapa.html")
existe("web/frontend/pages/aula-1.html")
existe("web/frontend/styles/login.css")
existe("web/frontend/styles/mapa.css")
existe("web/frontend/styles/aula-1.css")
existe("web/frontend/js/login.js")
existe("web/frontend/js/mapa.js")
existe("web/frontend/js/aula-1.js")
existe("web/frontend/assets/background.png")
existe("web/frontend/assets/logo-c1.png")

# JSONs
academy = validar_json("web/frontend/data/academy-nivel01.json")
aula1 = validar_json("web/frontend/data/aula-1.json")

if isinstance(academy, list) and len(academy) == 9:
    ok("Academy Nível 1 possui 9 etapas")
else:
    erro("Academy Nível 1 não possui exatamente 9 etapas")

if isinstance(aula1, dict) and len(aula1.get("etapas", [])) >= 1:
    ok("Aula 1 possui etapas configuradas")
else:
    erro("Aula 1 não possui etapas configuradas")

# Links importantes
contem("web/frontend/index.html", "styles/login.css")
contem("web/frontend/index.html", "js/login.js")
contem("web/frontend/js/login.js", 'window.location.href = "pages/mapa.html";')
contem("web/frontend/pages/mapa.html", "../styles/mapa.css")
contem("web/frontend/pages/mapa.html", "../js/mapa.js")
contem("web/frontend/js/mapa.js", "../data/academy-nivel01.json")
contem("web/frontend/pages/aula-1.html", "../styles/aula-1.css")
contem("web/frontend/pages/aula-1.html", "../js/aula-1.js")
contem("web/frontend/js/aula-1.js", "../data/aula-1.json")
contem("web/frontend/pages/aula-1.html", 'class="botao-voltar-padrao"')
contem("web/frontend/pages/mapa.html", 'class="botao-voltar-padrao"')

print()
if ERROS:
    print("=== RESULTADO: FALHOU ===")
    for item in ERROS:
        print("-", item)
    sys.exit(1)

print("=== RESULTADO: OK ===")
