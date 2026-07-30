async function carregarAula1() {
    const resposta = await fetch("../data/aula-1.json");
    const aula = await resposta.json();

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
        <h2>${aula.fala_mentora.titulo}</h2>
        <p class="fala">"${aula.fala_mentora.fala}"</p>
    `;

    const etapas = document.getElementById("aulaEtapas");
    etapas.innerHTML = aula.etapas.map((etapa) => `
        <div class="step">
            <small>${etapa.ordem}</small>
            <h3>${etapa.titulo}</h3>
            <p>${etapa.descricao}</p>
        </div>
    `).join("");

    document.getElementById("checkpointTitulo").textContent = aula.checkpoint.titulo;
    document.getElementById("checkpointTexto").textContent = aula.checkpoint.texto;
}

carregarAula1();
