# Arquitetura Oficial — CampOne Academy DevQuest

Esta pasta documenta a arquitetura técnica do projeto.

## Estado atual

A Academy teórica foi fechada no fluxo atual do terminal.

O main.py ainda concentra o jogo inteiro.

A estrutura de pastas foi criada antes da migração para preparar o projeto para crescer com segurança.

## Regra principal

Não mover todo o código de uma vez.

A migração deve acontecer em blocos pequenos:

1. uma responsabilidade por vez;
2. teste manual no terminal;
3. commit pequeno;
4. próxima responsabilidade.

## Estrutura principal

engine/
academy/
mundo_pratico/
workspace/
sistemas/
jogador/
conteudo/
assets/
docs/
saves/
testes/
ferramentas/

## Próximo passo técnico

Antes de mover funções, gerar e revisar o mapa de migração do main.py.

Primeiro bloco recomendado para migração:

jogador/perfil.py

Funções iniciais:

- criar_jogador
- mostrar_status
