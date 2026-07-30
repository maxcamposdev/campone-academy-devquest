let aulaAtual = null;
let cenaAtualIndex = 0;
let falaAtualIndex = 0;

async function carregarAula() {
    const resposta = await fetch("../data/aula-1.json");
    aulaAtual = await resposta.json();
    renderizarCena();
}

function renderizarCena() {
    const cena = aulaAtual.cenas[cenaAtualIndex];
    document.getElementById("localBadge").textContent = cena.local;
    document.getElementById("personagemEmoji").textContent = cena.emoji;
    document.getElementById("personagemNome").textContent = cena.personagem;
    document.getElementById("acaoTexto").textContent = cena.acao;
    
    if (cena.tipo === "pergunta") {
        renderizarPergunta(cena);
    } else {
        renderizarFalas(cena);
    }
}

function renderizarFalas(cena) {
    const falaContainer = document.getElementById("falaTexto");
    const opcoesContainer = document.getElementById("opcoesContainer");
    const btnProximo = document.getElementById("btnProximo");
    
    opcoesContainer.classList.add("hidden");
    btnProximo.classList.remove("hidden");
    
    let html = "";
    for (let i = 0; i <= falaAtualIndex; i++) {
        if (cena.falas[i]) {
            html += `<p class="fala-item fade-in">${cena.falas[i]}</p>`;
        }
    }
    
    falaContainer.innerHTML = html;
    
    if (falaAtualIndex >= cena.falas.length - 1) {
        btnProximo.textContent = "Próximo ▶";
    } else {
        btnProximo.textContent = "Continuar...";
    }
}

function renderizarPergunta(cena) {
    const falaContainer = document.getElementById("falaTexto");
    const opcoesContainer = document.getElementById("opcoesContainer");
    const btnProximo = document.getElementById("btnProximo");
    
    btnProximo.classList.add("hidden");
    falaContainer.innerHTML = `<p>${cena.falas[0]}</p>`;
    
    let html = "";
    cena.opcoes.forEach(opcao => {
        html += `<button class="opcao-btn" onclick="responder(${cena.id}, ${opcao.id})">${opcao.texto}</button>`;
    });
    
    opcoesContainer.innerHTML = html;
    opcoesContainer.classList.remove("hidden");
}

function responder(cenaId, opcaoId) {
    const cena = aulaAtual.cenas.find(c => c.id === cenaId);
    const feedback = cena.feedbacks[opcaoId];
    const acertou = opcaoId === cena.resposta_correta;
    
    // Desabilitar botões
    const botoes = document.querySelectorAll(".opcao-btn");
    botoes.forEach(btn => btn.disabled = true);
    
    // Mostrar feedback do personagem
    const opcoesContainer = document.getElementById("opcoesContainer");
    const falaContainer = document.getElementById("falaTexto");
    
    let feedbackHtml = `<div class="feedback-area fade-in">`;
    feedbackHtml += `<p class="feedback-acao"><em>${feedback.acao}</em></p>`;
    feedback.falas.forEach(fala => {
        feedbackHtml += `<p class="feedback-fala">"${fala}"</p>`;
    });
    feedbackHtml += `</div>`;
    
    opcoesContainer.innerHTML = feedbackHtml;
    
    if (acertou) {
        // Acertou: avança para próxima cena
        setTimeout(() => {
            document.getElementById("btnProximo").classList.remove("hidden");
            document.getElementById("btnProximo").textContent = "Continuar ▶";
            document.getElementById("btnProximo").onclick = function() {
                cenaAtualIndex++;
                falaAtualIndex = 0;
                renderizarCena();
            };
        }, 1500);
    } else {
        // Errou: mostra aprendizado e permite tentar novamente
        setTimeout(() => {
            opcoesContainer.innerHTML += `<button class="btn-tentar" onclick="tentarNovamente(${cenaId})">Tentar novamente</button>`;
        }, 1500);
    }
}

function tentarNovamente(cenaId) {
    const cena = aulaAtual.cenas.find(c => c.id === cenaId);
    renderizarPergunta(cena);
}

function proximaCena() {
    const cena = aulaAtual.cenas[cenaAtualIndex];
    
    if (cena.tipo !== "pergunta" && falaAtualIndex < cena.falas.length - 1) {
        falaAtualIndex++;
        renderizarFalas(cena);
        return;
    }
    
    if (cenaAtualIndex < aulaAtual.cenas.length - 1) {
        cenaAtualIndex++;
        falaAtualIndex = 0;
        renderizarCena();
    }
}

carregarAula();
