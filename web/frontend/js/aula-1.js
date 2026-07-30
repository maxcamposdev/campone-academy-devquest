let aulaAtual = null;
let indiceEtapaAtual = 0;

async function carregarAula1() {
    const resposta = await fetch("../data/aula-1.json");
    const aula = await resposta.json();
    aulaAtual = aula;

    document.getElementById("aulaTitulo").textContent = aula.titulo;
    document.getElementById("aulaResumo").textContent = aula.resumo;
    document.getElementById("aulaBadge").textContent = `${aula.fase} • ${aula.nivel}`;

    document.getElementById("aulaMeta").innerHTML = `
        <span>Mentora: ${aula.mentora}</span>
        <span>Status: Protótipo Web</span>
        <span>Cargo do jogador: ${aula.cargo_jogador}</span>
        <span>Objetivo: compreender a Grande Rede</span>
    `;

    document.getElementById("aulaContexto").innerHTML = `
        <h2>${aula.contexto.titulo}</h2>
        ${aula.contexto.paragrafos.map((paragrafo) => `<p>${paragrafo}</p>`).join("")}
    `;

    document.getElementById("falaMentora").innerHTML = `
        <div class="personagem-card">
            <div class="personagem-avatar">
                <span>${aula.fala_mentora.personagem.charAt(0)}</span>
                <small>${aula.fala_mentora.avatar_status}</small>
            </div>

            <div class="personagem-conteudo">
                <h2>${aula.fala_mentora.titulo}</h2>
                <strong>${aula.fala_mentora.cargo}</strong>
                <p class="fala">"${aula.fala_mentora.fala}"</p>

                <button class="audio-futuro" type="button" onclick="alert('Narração será adicionada em uma fase futura.')">
                    ▶ Ouvir narração futura
                </button>
            </div>
        </div>
    `;

    document.getElementById("aulaEtapas").innerHTML = aula.etapas.map((etapa) => `
        <div class="step">
            <h3>${etapa.titulo}</h3>
            <p>${etapa.descricao}</p>
        </div>
    `).join("");

    document.getElementById("checkpointTitulo").textContent = aula.checkpoint.titulo;
    document.getElementById("checkpointTexto").textContent = aula.checkpoint.texto;
}

function iniciarAula() {
    if (!aulaAtual || !aulaAtual.etapas || aulaAtual.etapas.length === 0) {
        alert("Conteúdo da aula ainda não carregado.");
        return;
    }

    indiceEtapaAtual = 0;

    document.getElementById("painelInicioAula").classList.add("hidden");
    document.getElementById("checkpointAula").classList.add("hidden");

    renderizarEtapaAtual();
}

function renderizarEtapaAtual() {
    const etapa = aulaAtual.etapas[indiceEtapaAtual];

    document.getElementById("etapaAtivaTitulo").textContent = etapa.titulo;
    document.getElementById("etapaAtivaDescricao").textContent = etapa.descricao;
    document.getElementById("etapaAtiva").classList.remove("hidden");

    document.getElementById("etapaIndicador").textContent =
        `Parte ${indiceEtapaAtual + 1} de ${aulaAtual.etapas.length}`;

    document.getElementById("botaoAnteriorEtapa").disabled = indiceEtapaAtual === 0;

    document.getElementById("botaoProximoEtapa").textContent =
        indiceEtapaAtual === aulaAtual.etapas.length - 1
            ? "Concluir partes"
            : "Próximo";

    document.getElementById("etapaAtiva").scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}

function proximaEtapa() {
    if (!aulaAtual) {
        return;
    }

    if (indiceEtapaAtual < aulaAtual.etapas.length - 1) {
        indiceEtapaAtual += 1;
        renderizarEtapaAtual();
        return;
    }

    mostrarCheckpoint();
}

function etapaAnterior() {
    if (!aulaAtual || indiceEtapaAtual === 0) {
        return;
    }

    indiceEtapaAtual -= 1;
    renderizarEtapaAtual();
}

function mostrarCheckpoint() {
    const checkpoint = aulaAtual.checkpoint;

    document.getElementById("checkpointTitulo").textContent = checkpoint.titulo;
    document.getElementById("checkpointTexto").textContent = checkpoint.texto;
    document.getElementById("checkpointPergunta").textContent = checkpoint.pergunta;

    document.getElementById("checkpointOpcoes").innerHTML = checkpoint.opcoes.map((opcao, indice) => `
        <button class="checkpoint-option" type="button" onclick="responderCheckpoint(${indice})">
            ${opcao.texto}
        </button>
    `).join("");

    document.getElementById("checkpointFeedback").textContent = "";
    document.getElementById("checkpointFeedback").className = "checkpoint-feedback";
    document.getElementById("conclusaoAula").classList.add("hidden");
    document.getElementById("checkpointAula").classList.remove("hidden");

    document.getElementById("checkpointAula").scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}

function responderCheckpoint(indice) {
    const opcao = aulaAtual.checkpoint.opcoes[indice];
    const feedback = document.getElementById("checkpointFeedback");

    feedback.textContent = opcao.feedback;
    feedback.className = opcao.correta
        ? "checkpoint-feedback correto"
        : "checkpoint-feedback incorreto";

    if (opcao.correta) {
        localStorage.setItem("campone_aula_1_checkpoint", "concluido");
        localStorage.setItem("campone_aula_1_status", "concluida");
        document.getElementById("conclusaoAula").classList.remove("hidden");
    }
}

function abrirMenuAula() {
    document.getElementById("menuAulaOverlay").classList.remove("hidden");
}

function fecharMenuAula() {
    document.getElementById("menuAulaOverlay").classList.add("hidden");
}

function salvarProgressoManual() {
    const user = JSON.parse(localStorage.getItem("campone_user") || "{}");
    const etapaAtual = aulaAtual && aulaAtual.etapas
        ? aulaAtual.etapas[indiceEtapaAtual]
        : null;

    const progresso = {
        jogador: {
            nome: user.nome || "Jogador",
            nivel: user.nivel || "Recruta"
        },
        aula: {
            id: 1,
            titulo: aulaAtual ? aulaAtual.titulo : "Aula 1",
            status: localStorage.getItem("campone_aula_1_status") || "em_andamento",
            checkpoint: localStorage.getItem("campone_aula_1_checkpoint") || "pendente",
            parteAtual: indiceEtapaAtual + 1,
            parteAtualTitulo: etapaAtual ? etapaAtual.titulo : "Não iniciada",
            totalPartes: aulaAtual && aulaAtual.etapas ? aulaAtual.etapas.length : 0
        },
        atualizadoEm: new Date().toISOString()
    };

    localStorage.setItem("campone_aula_1_save", JSON.stringify(progresso));

    alert(
        "Progresso salvo!\n\n" +
        "Jogador: " + progresso.jogador.nome + "\n" +
        "Aula: " + progresso.aula.titulo + "\n" +
        "Parte atual: " + progresso.aula.parteAtualTitulo
    );
}

carregarAula1();
