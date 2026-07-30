let aulaAtual = null;
let secaoAtual = null;
let topicoAtual = null;

async function carregarAula1() {
    const resposta = await fetch("../data/aula-1.json");
    const aula = await resposta.json();
    aulaAtual = aula;
    renderizarMenuPrincipal();
}

function renderizarMenuPrincipal() {
    const menu = aulaAtual.menu_principal;
    document.getElementById("aulaTitulo").textContent = menu.titulo;
    document.getElementById("aulaResumo").textContent = `${menu.tema_real} • ${menu.tipo}`;
    document.getElementById("aulaBadge").textContent = `${aulaAtual.fase} • ${aulaAtual.nivel}`;
    
    let html = '<div class="menu-opcoes">';
    menu.opcoes.forEach(opcao => {
        html += `<button class="menu-opcao" onclick="navegarPara('${opcao.secao}')">${opcao.id} - ${opcao.titulo}</button>`;
    });
    html += '</div>';
    document.getElementById("menuPrincipal").innerHTML = html;
    document.getElementById("menuPrincipal").classList.remove("hidden");
    document.getElementById("conteudoAula").classList.add("hidden");
}

function navegarPara(secao) {
    secaoAtual = secao;
    document.getElementById("menuPrincipal").classList.add("hidden");
    document.getElementById("conteudoAula").classList.remove("hidden");
    
    switch(secao) {
        case 'abertura': renderizarAbertura(); break;
        case 'reconhecimento': renderizarReconhecimento(); break;
        case 'campo_treinamento': renderizarCampoTreinamento(); break;
        case 'laboratorio_falhas': renderizarLaboratorioFalhas(); break;
        case 'missao_producao': renderizarMissaoProducao(); break;
        case 'prova_dominio': renderizarProvaDominio(); break;
        case 'registro': renderizarRegistro(); break;
        case 'relatorio_final': renderizarRelatorioFinal(); break;
    }
}

function voltarMenu() {
    document.getElementById("menuPrincipal").classList.remove("hidden");
    document.getElementById("conteudoAula").classList.add("hidden");
}

function renderizarAbertura() {
    const abertura = aulaAtual.abertura;
    let html = `<h2>${abertura.titulo}</h2>`;
    html += '<div class="cena">';
    abertura.cenas.forEach(cena => html += `<p>${cena}</p>`);
    html += '</div>';
    html += '<div class="falas">';
    abertura.falas.forEach(fala => html += `<p class="fala">"${fala}"</p>`);
    html += '</div>';
    html += '<div class="narracao">';
    abertura.narracao.forEach(n => html += `<p>${n}</p>`);
    html += '</div>';
    html += '<div class="falas">';
    abertura.falas_finais.forEach(fala => html += `<p class="fala">"${fala}"</p>`);
    html += '</div>';
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function renderizarReconhecimento() {
    const reconhecimento = aulaAtual.reconhecimento;
    let html = `<h2>${reconhecimento.titulo}</h2>`;
    html += `<p>${reconhecimento.intro}</p>`;
    html += '<div class="topicos">';
    reconhecimento.topicos.forEach(topico => {
        html += `<button class="topico-btn" onclick="abrirTopico(${topico.id})">${topico.icone} ${topico.titulo}</button>`;
    });
    html += `<button class="topico-btn resumo-btn" onclick="abrirResumo()">🧩 Resumo da Etapa</button>`;
    html += '</div>';
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function abrirTopico(id) {
    const topico = aulaAtual.reconhecimento.topicos.find(t => t.id === id);
    topicoAtual = topico;
    let html = `<h2>${topico.icone} ${topico.titulo}</h2>`;
    html += `<p class="personagem">${topico.personagem}: ${topico.fala_intro}</p>`;
    html += '<div class="conteudo">';
    topico.conteudo.forEach(c => html += `<p>${c}</p>`);
    html += '</div>';
    html += `<div class="pergunta">
        <p><strong>${topico.pergunta.texto}</strong></p>
        <div class="opcoes">`;
    topico.pergunta.opcoes.forEach(opcao => {
        html += `<button onclick="responderTopico(${topico.id}, ${opcao.id})">${opcao.texto}</button>`;
    });
    html += `</div><div id="feedbackTopico"></div></div>`;
    html += `<button onclick="renderizarReconhecimento()">Voltar aos Tópicos</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function responderTopico(topicoId, opcaoId) {
    const topico = aulaAtual.reconhecimento.topicos.find(t => t.id === topicoId);
    const opcao = topico.pergunta.opcoes.find(o => o.id === opcaoId);
    let html = `<p class="${opcao.correta ? 'correto' : 'incorreto'}"><strong>${opcao.feedback_personagem}</strong></p>`;
    html += `<p>${opcao.feedback}</p>`;
    if(opcao.feedback2) html += `<p>${opcao.feedback2}</p>`;
    if(opcao.feedback3) html += `<p>${opcao.feedback3}</p>`;
    if(opcao.dica) html += `<p class="dica">${opcao.dica}</p>`;
    if(opcao.correta) {
        html += `<button onclick="renderizarReconhecimento()">Continuar</button>`;
    } else {
        html += `<button onclick="abrirTopico(${topicoId})">Tentar Novamente</button>`;
    }
    document.getElementById("feedbackTopico").innerHTML = html;
}

function abrirResumo() {
    const resumo = aulaAtual.reconhecimento.resumo;
    let html = `<h2>${resumo.titulo}</h2>`;
    html += `<p class="personagem">${resumo.personagem}: "${resumo.fala_intro}"</p>`;
    html += `<p>${resumo.narracao}</p>`;
    html += '<ul>';
    resumo.itens.forEach(item => html += `<li>${item}</li>`);
    html += '</ul>';
    html += `<p class="fluxo"><strong>${resumo.fluxo}</strong></p>`;
    html += `<p>${resumo.conclusao}</p>`;
    html += `<p class="nota">${resumo.nota}</p>`;
    html += `<button onclick="renderizarReconhecimento()">Voltar</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function renderizarCampoTreinamento() {
    const campo = aulaAtual.campo_treinamento;
    let html = `<h2>${campo.titulo}</h2>`;
    html += `<p class="personagem">${campo.personagem}: "${campo.fala_intro}"</p>`;
    html += `<p>${campo.contexto}</p>`;
    html += `<p><strong>${campo.intro}</strong></p>`;
    html += '<ol>';
    campo.passos.forEach(p => html += `<li>${p}</li>`);
    html += '</ol>';
    html += `<p><strong>${campo.conclusao}</strong></p>`;
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function renderizarLaboratorioFalhas() {
    const lab = aulaAtual.laboratorio_falhas;
    let html = `<h2>${lab.titulo}</h2>`;
    html += `<p class="personagem">${lab.personagem}: "${lab.falas_intro[0]}"</p>`;
    html += `<p>"${lab.falas_intro[1]}"</p>`;
    html += `<p><strong>${lab.intro}</strong></p>`;
    lab.falhas.forEach(falha => {
        html += `<h3>${falha.titulo}</h3><p>${falha.descricao}</p>`;
    });
    html += '<h3>Resumo:</h3><ul>';
    lab.resumo.forEach(r => html += `<li>${r}</li>`);
    html += '</ul>';
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function renderizarMissaoProducao() {
    const missao = aulaAtual.missao_producao;
    let html = `<h2>${missao.titulo}</h2>`;
    html += `<p class="personagem">${missao.personagem}: "${missao.fala_intro}"</p>`;
    missao.narracao.forEach(n => html += `<p>${n}</p>`);
    html += `<p><strong>${missao.intro}</strong></p>`;
    missao.exemplos.forEach(ex => {
        html += `<h3>${ex.nome}</h3><ul>`;
        ex.passos.forEach(p => html += `<li>${p}</li>`);
        html += '</ul>';
    });
    html += '<h3>Resumo:</h3><ul>';
    missao.resumo.forEach(r => html += `<li>${r}</li>`);
    html += '</ul>';
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function renderizarProvaDominio() {
    const prova = aulaAtual.prova_dominio;
    let html = `<h2>${prova.titulo}</h2>`;
    html += `<p class="personagem">${prova.personagem}: "${prova.fala_intro}"</p>`;
    html += `<p>${prova.contexto}</p>`;
    html += `<div class="pergunta"><p><strong>${prova.pergunta.texto}</strong></p><div class="opcoes">`;
    prova.pergunta.opcoes.forEach(opcao => {
        html += `<button onclick="responderProva(${opcao.id})">${opcao.texto}</button>`;
    });
    html += `</div><div id="feedbackProva"></div></div>`;
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function responderProva(opcaoId) {
    const opcao = aulaAtual.prova_dominio.pergunta.opcoes.find(o => o.id === opcaoId);
    let html = `<p class="${opcao.correta ? 'correto' : 'incorreto'}"><strong>${opcao.feedback_personagem}</strong></p>`;
    html += `<p>${opcao.feedback}</p>`;
    if(opcao.feedback2) html += `<p>${opcao.feedback2}</p>`;
    if(opcao.dica) html += `<p class="dica">${opcao.dica}</p>`;
    if(opcao.correta) {
        html += `<p><strong>${aulaAtual.prova_dominio.conclusao.mensagem}</strong></p>`;
        html += `<p>${aulaAtual.prova_dominio.conclusao.nota}</p>`;
        html += `<button onclick="voltarMenu()">Continuar</button>`;
    } else {
        html += `<button onclick="renderizarProvaDominio()">Tentar Novamente</button>`;
    }
    document.getElementById("feedbackProva").innerHTML = html;
}

function renderizarRegistro() {
    const reg = aulaAtual.registro;
    let html = `<h2>${reg.titulo}</h2>`;
    html += `<p class="personagem">${reg.personagem}: "${reg.fala_intro}"</p>`;
    html += `<p>${reg.intro}</p>`;
    html += '<ul>';
    reg.itens.forEach(item => html += `<li>${item}</li>`);
    html += '</ul>';
    html += `<p><strong>${reg.nota.titulo}:</strong> ${reg.nota.mensagem}</p>`;
    html += `<p>${reg.nota.futura}</p>`;
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

function renderizarRelatorioFinal() {
    const rel = aulaAtual.relatorio_final;
    let html = `<h2>${rel.titulo}</h2>`;
    html += `<p class="personagem">${rel.personagem}: "${rel.fala_intro}"</p>`;
    html += `<p><strong>${rel.subtitulo}</strong></p>`;
    html += `<p>${rel.intro}</p>`;
    html += '<ul>';
    rel.itens.forEach(item => html += `<li>${item}</li>`);
    html += '</ul>';
    html += `<p><strong>${rel.conclusao.titulo}:</strong> ${rel.conclusao.mensagem}</p>`;
    html += `<p>${rel.nota}</p>`;
    html += `<button onclick="voltarMenu()">Voltar ao Menu</button>`;
    document.getElementById("conteudoAula").innerHTML = html;
}

carregarAula1();
