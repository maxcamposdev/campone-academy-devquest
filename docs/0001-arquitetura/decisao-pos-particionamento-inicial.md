# Decisão Pós-Particionamento Inicial

**Status:** Decisão técnica registrada
**Marco:** Academy extraída do main.py

## Estado alcançado

O main.py virou ponto de entrada.

As responsabilidades principais foram separadas:

- engine/telas.py
- engine/mapa.py
- engine/navegacao.py
- jogador/perfil.py
- academy/nivel01/etapa01 até etapa09

## Decisão

Não dividir internamente cada etapa agora.

## Motivo

Cada etapa já está isolada em seu próprio módulo.

Dividir cada etapa em arquivos como:

- introducao.py
- reconhecimento.py
- campo_treinamento.py
- laboratorio.py
- missao.py
- prova.py
- registro.py
- relatorio.py

criaria muitos arquivos neste momento e traria pouco ganho imediato.

## Próximo foco recomendado

Preparar a Engine e o Mundo Prático.

Antes do Mundo Prático, a Engine deve receber recursos reutilizáveis como:

- sistema de telas;
- sistema de diálogo;
- sistema de perguntas;
- sistema de validação;
- sistema de navegação;
- sistema de registros;
- utilidades gerais.

## Regra

Se uma etapa crescer demais no futuro, ela poderá ser dividida internamente.

Mas isso deve acontecer por necessidade real, não por ansiedade arquitetural.
