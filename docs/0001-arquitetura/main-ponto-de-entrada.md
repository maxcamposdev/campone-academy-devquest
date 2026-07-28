# main.py — Ponto de Entrada da CampOne

**Status:** Concluído
**Marco:** Pós-Academy / Particionamento inicial

## Objetivo

O main.py agora possui uma única responsabilidade:

iniciar o jogo

Ele não deve conter:

- funções de etapa;
- conteúdo narrativo;
- validações;
- menus internos complexos;
- regras de negócio;
- sistemas permanentes.

## Estado atual

O main.py importa os módulos principais:

- engine.telas;
- engine.mapa;
- engine.navegacao;
- jogador.perfil.

E executa o fluxo inicial do jogo.

## Funções restantes no main.py

0

## Regra para o futuro

Nenhuma função nova deve ser criada diretamente no main.py.

Se uma funcionalidade nova surgir, ela deve ser classificada antes:

- Engine;
- Academy;
- Mundo Prático;
- Workspace;
- Sistemas;
- Jogador;
- Conteúdo.

Depois deve ser implementada no módulo correto.

## Próximo passo técnico

Continuar a organização da Engine e revisar dependências internas dos módulos.
