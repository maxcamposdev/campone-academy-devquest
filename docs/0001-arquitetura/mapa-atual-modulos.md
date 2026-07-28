# Mapa Atual de Módulos Python — CampOne Academy

**Status:** Pós-Academy / Particionamento inicial

## Resumo

```text
main.py = ponto de entrada
engine/ = telas, mapa e navegação
jogador/ = perfil do jogador
academy/nivel01/etapa01–etapa09 = etapas teóricas da Academy
```

---

## main.py

Funções: 0

```text
nenhuma função
```

Imports:

```python
from engine.telas import tela_boas_vindas
from engine.mapa import mostrar_mapa
from engine.navegacao import menu_jogador
from jogador.perfil import criar_jogador, mostrar_status
```

---

## engine/__init__.py

Funções: 0

```text
nenhuma função
```

Imports:

```text
nenhum import
```

---

## engine/mapa.py

Funções: 2

- mostrar_mapa
- mostrar_etapas_nivel_1

Imports:

```text
nenhum import
```

---

## engine/navegacao.py

Funções: 2

- entrar_nivel_1
- menu_jogador

Imports:

```python
from engine.mapa import mostrar_mapa, mostrar_etapas_nivel_1
from jogador.perfil import mostrar_status
from academy.nivel01.etapa01.etapa import entrar_etapa_1
from academy.nivel01.etapa02.etapa import entrar_etapa_2
from academy.nivel01.etapa03.etapa import entrar_etapa_3
from academy.nivel01.etapa04.etapa import entrar_etapa_4
from academy.nivel01.etapa05.etapa import entrar_etapa_5
from academy.nivel01.etapa06.etapa import entrar_etapa_6
from academy.nivel01.etapa07.etapa import entrar_etapa_7
from academy.nivel01.etapa08.etapa import entrar_etapa_8
from academy.nivel01.etapa09.etapa import entrar_etapa_9
```

---

## engine/telas.py

Funções: 1

- tela_boas_vindas

Imports:

```text
nenhum import
```

---

## jogador/__init__.py

Funções: 0

```text
nenhuma função
```

Imports:

```text
nenhum import
```

---

## jogador/perfil.py

Funções: 2

- criar_jogador
- mostrar_status

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa01/etapa.py

Funções: 16

- topico_internet
- topico_cliente_servidor
- topico_http_https
- topico_dns
- topico_endereco_ip
- topico_requisicao_http
- resumo_etapa_1
- cena_abertura_etapa_1
- conceito_etapa_1
- pratica_caminho_clique
- experimentacao_etapa_1
- aplicacao_vida_real_etapa_1
- prova_dominio_etapa_1
- registro_etapa_1
- relatorio_final_etapa_1
- entrar_etapa_1

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa02/etapa.py

Funções: 17

- cena_abertura_etapa_2
- topico_backend
- topico_servidor_web
- topico_logica_negocio
- topico_api
- topico_api_rest
- topico_endpoints
- topico_rotas
- topico_json
- reconhecimento_etapa_2
- campo_treinamento_etapa_2
- laboratorio_falhas_etapa_2
- missao_producao_etapa_2
- registro_etapa_2
- relatorio_final_etapa_2
- prova_dominio_etapa_2
- entrar_etapa_2

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa03/etapa.py

Funções: 15

- topico_banco_dados
- topico_sql
- topico_tabelas
- topico_registros_colunas
- topico_chave_primaria
- topico_chave_estrangeira
- topico_relacionamento
- reconhecimento_etapa_3
- campo_treinamento_etapa_3
- laboratorio_falhas_etapa_3
- missao_producao_etapa_3
- prova_dominio_etapa_3
- registro_etapa_3
- relatorio_final_etapa_3
- entrar_etapa_3

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa04/etapa.py

Funções: 17

- topico_comunicacao_frontend_backend_etapa_4
- topico_api_rest_pratica_etapa_4
- topico_get_etapa_4
- topico_post_etapa_4
- topico_put_etapa_4
- topico_delete_etapa_4
- topico_status_code_etapa_4
- topico_fluxo_completo_etapa_4
- cena_abertura_etapa_4
- reconhecimento_etapa_4
- campo_treinamento_etapa_4
- laboratorio_falhas_etapa_4
- missao_producao_etapa_4
- prova_dominio_etapa_4
- registro_etapa_4
- relatorio_final_etapa_4
- entrar_etapa_4

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa05/etapa.py

Funções: 16

- topico_frontend_etapa_5
- topico_html_etapa_5
- topico_css_etapa_5
- topico_javascript_etapa_5
- topico_dom_etapa_5
- topico_responsividade_etapa_5
- topico_frontend_completo_etapa_5
- cena_abertura_etapa_5
- reconhecimento_etapa_5
- campo_treinamento_etapa_5
- laboratorio_falhas_etapa_5
- missao_producao_etapa_5
- prova_dominio_etapa_5
- registro_etapa_5
- relatorio_final_etapa_5
- entrar_etapa_5

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa06/etapa.py

Funções: 16

- topico_login_etapa_6
- topico_autenticacao_etapa_6
- topico_autorizacao_etapa_6
- topico_cookies_etapa_6
- topico_sessao_etapa_6
- topico_token_etapa_6
- topico_seguranca_completa_etapa_6
- cena_abertura_etapa_6
- reconhecimento_etapa_6
- campo_treinamento_etapa_6
- laboratorio_falhas_etapa_6
- missao_producao_etapa_6
- prova_dominio_etapa_6
- registro_etapa_6
- relatorio_final_etapa_6
- entrar_etapa_6

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa07/etapa.py

Funções: 17

- topico_git_etapa_7
- topico_commit_etapa_7
- topico_branch_etapa_7
- topico_merge_conflito_etapa_7
- topico_github_etapa_7
- topico_clone_push_pull_etapa_7
- topico_historico_etapa_7
- topico_git_github_time_etapa_7
- reconhecimento_etapa_7
- cena_abertura_etapa_7
- campo_treinamento_etapa_7
- laboratorio_falhas_etapa_7
- missao_producao_etapa_7
- prova_dominio_etapa_7
- registro_etapa_7
- relatorio_final_etapa_7
- entrar_etapa_7

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa08/etapa.py

Funções: 16

- topico_sistema_local_etapa_8
- topico_deploy_etapa_8
- topico_servidor_deploy_etapa_8
- topico_dominio_dns_etapa_8
- topico_hospedagem_vps_nuvem_etapa_8
- topico_pipeline_etapa_8
- topico_producao_etapa_8
- reconhecimento_etapa_8
- cena_abertura_etapa_8
- campo_treinamento_etapa_8
- laboratorio_falhas_etapa_8
- missao_producao_etapa_8
- prova_dominio_etapa_8
- registro_etapa_8
- relatorio_final_etapa_8
- entrar_etapa_8

Imports:

```text
nenhum import
```

---

## academy/nivel01/etapa09/etapa.py

Funções: 16

- cena_abertura_etapa_9
- topico_arquitetura_etapa_9
- topico_cliente_servidor_etapa_9
- topico_camadas_etapa_9
- topico_api_planta_etapa_9
- topico_fluxo_pedido_etapa_9
- topico_diagnostico_etapa_9
- topico_planta_mestra_etapa_9
- reconhecimento_etapa_9
- campo_treinamento_etapa_9
- laboratorio_falhas_etapa_9
- missao_producao_etapa_9
- prova_dominio_etapa_9
- registro_etapa_9
- relatorio_final_etapa_9
- entrar_etapa_9

Imports:

```text
nenhum import
```

---

## Total

```text
Arquivos analisados: 16
Funções mapeadas: 153
```

## Próximo passo recomendado

```text
Decidir com Max se o próximo corte será:
1 - dividir internamente as etapas da Academy;
2 - fortalecer a Engine antes do Mundo Prático.
```
