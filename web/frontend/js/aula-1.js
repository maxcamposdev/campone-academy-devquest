let aulaAtual = null;

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

    const contexto = document.getElementById("aulaContexto");
    contexto.innerHTML = `
        <h2>${aula.contexto.titulo}</h2>
        ${aula.contexto.paragrafos.map((paragrafo) => `<p>${paragrafo}</p>`).join("")}
    `;

    const fala = document.getElementById("falaMentora");
    fala.innerHTML = `
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

    const etapas = document.getElementById("aulaEtapas");
    etapas.innerHTML = aula.etapas.map((etapa) => `
        <div class="step">
            <h3>${etapa.titulo}</h3>
            <p>${etapa.descricao}</p>
        </div>
    `).join("");

    document.getElementById("checkpointTitulo").textContent = aula.checkpoint.titulo;
    document.getElementById("checkpointTexto").textContent = aula.checkpoint.texto;
}

carregarAula1();


function iniciarAula() {
    if (!aulaAtual || !aulaAtual.etapas || aulaAtual.etapas.length === 0) {
        alert("Conteúdo da aula ainda não carregado.");
        return;
    }

    const primeiraEtapa = aulaAtual.etapas[0];

    document.getElementById("etapaAtivaTitulo").textContent = primeiraEtapa.titulo;
    document.getElementById("etapaAtivaDescricao").textContent = primeiraEtapa.descricao;
    document.getElementById("etapaAtiva").classList.remove("hidden");

    document.getElementById("etapaAtiva").scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}
