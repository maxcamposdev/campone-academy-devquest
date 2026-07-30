const user = JSON.parse(localStorage.getItem("campone_user") || "{}");
const nome = user.nome || "Jogador";

document.getElementById("playerStatus").textContent = "";

const grid = document.getElementById("academyGrid");

function obterNomeExibicao() {
    if (!nome || nome === "Recruta") {
        return "Jogador";
    }

    return nome;
}

function chaveStatusAula(etapa) {
    return "campone_aula_" + etapa.id + "_status";
}

function contarAulasConcluidas(etapas) {
    return etapas.filter((etapa) =>
        localStorage.getItem(chaveStatusAula(etapa)) === "concluida"
    ).length;
}

function calcularCargoColaborador(etapas) {
    const concluidas = contarAulasConcluidas(etapas);

    if (concluidas >= 9) {
        return "Trainee";
    }

    return "Recruta";
}

function atualizarColaborador(etapas) {
    const colaboradorAtual = document.getElementById("colaboradorAtual");

    if (!colaboradorAtual) {
        return;
    }

    const cargo = calcularCargoColaborador(etapas);
    colaboradorAtual.textContent = cargo + " — " + obterNomeExibicao();
}

function criarCardEtapa(etapa) {
    const concluida = localStorage.getItem(chaveStatusAula(etapa)) === "concluida";
    const bloqueada = etapa.status === "bloqueada" && !concluida;

    const statusIcone = concluida ? "✅" : (bloqueada ? "🔒" : "🟢");
    const statusTexto = concluida ? "Concluída" : (bloqueada ? "Bloqueada" : "Disponível");

    const artigo = document.createElement("article");
    artigo.className = bloqueada ? "card locked" : "card";

    const acao = bloqueada
        ? `<a class="button secondary" href="#" onclick="alert('Esta etapa ainda está bloqueada neste protótipo.')">Bloqueada</a>`
        : `<a class="button" href="${etapa.rota}">${concluida ? "Revisar Aula" : "Entrar na Aula " + etapa.id}</a>`;

    artigo.innerHTML = `
        <h2>${statusIcone} Aula ${etapa.id} — ${etapa.titulo}</h2>
        <p><strong>Tema:</strong> ${etapa.tema}</p>
        <p><strong>Mentor(a):</strong> ${etapa.mentor}</p>
        <p>${etapa.descricao}</p>
        <p><strong>Status:</strong> ${statusTexto}</p>
        ${acao}
    `;

    return artigo;
}

function atualizarPainelProgresso(etapas) {
    const concluidas = contarAulasConcluidas(etapas);
    const itemPrototipo = document.getElementById("progressoAcademyValor");

    if (itemPrototipo) {
        itemPrototipo.textContent = `${concluidas}/9 etapas concluídas`;
    }
}

async function carregarAcademy() {
    try {
        const resposta = await fetch("../data/academy-nivel01.json");
        const etapas = await resposta.json();

        grid.innerHTML = "";

        atualizarColaborador(etapas);
        atualizarPainelProgresso(etapas);

        etapas.forEach((etapa) => {
            grid.appendChild(criarCardEtapa(etapa));
        });

        const mundoPratico = document.createElement("article");
        mundoPratico.className = "card";
        mundoPratico.innerHTML = `
            <h2>🟡 Mundo Prático</h2>
            <p><strong>Status:</strong> em desenvolvimento paralelo.</p>
            <p>Missão 01 — O Primeiro Dia já começou na branch principal do jogo Python.</p>
            <a class="button secondary" href="#" onclick="alert('Mundo Prático será integrado depois.')">Ver status</a>
        `;
        grid.appendChild(mundoPratico);

    } catch (erro) {
        grid.innerHTML = `
            <article class="card">
                <h2>Erro ao carregar Academy</h2>
                <p>Não foi possível carregar os dados das etapas.</p>
            </article>
        `;
        console.error(erro);
    }
}

carregarAcademy();
