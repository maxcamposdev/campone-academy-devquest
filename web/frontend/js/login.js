function togglePassword(el) {
            const input = el.parentElement.querySelector('input');
            input.type = input.type === 'password' ? 'text' : 'password';
        }

        function handleLogin(e) {
            e.preventDefault();
            const email = document.getElementById('email').value;
            
            localStorage.setItem('campone_user', JSON.stringify({
                nome: email.split('@')[0] || "Recruta",
                email: email,
                nivel: "Recruta",
                xp: 0
            }));
            
            window.location.href = "pages/mapa.html";
        }

        function socialLogin(provider) {
            alert(`Login com ${provider} simulado!`);
            localStorage.setItem('campone_user', JSON.stringify({
                nome: "Max Campos",
                email: "max.campos@campone.dev",
                nivel: "Recruta"
            }));
            window.location.href = "pages/mapa.html";
        }

        function startNewGame() {
            document.getElementById('email').value = "recruta.novo@campone.dev";
            document.getElementById('password').value = "campone123";
            setTimeout(() => {
                document.getElementById('loginForm').dispatchEvent(new Event('submit', { bubbles: true }));
            }, 200);
        }

        function loadGame() {
            document.getElementById('email').value = "max.campos@campone.dev";
            document.getElementById('password').value = "campone123";
            setTimeout(() => {
                document.getElementById('loginForm').dispatchEvent(new Event('submit', { bubbles: true }));
            }, 200);
        }
/* =====================================================
      CAMPONE - CÓDIGOS ANIMADOS DE FUNDO
===================================================== */

const canvas = document.getElementById("codeCanvas");
const ctx = canvas.getContext("2d");

let W, H;
let streams = [];

const COLORS = [
    "#00ff88",
    "#7CFC00",
    "#9CFF2E",
    "#FFD54F",
    "#FFC107",
    "#FF9800",
    "#FF7043"
];

const CODES = [
    "import academy",
    "from campone.academy import Missao",
    "class DevJunior:",
    "def __init__(self):",
    "self.nivel = 1",
    "self.xp = 0",
    "self.missoes = []",
    "def ganhar_xp(self):",
    "def subir_nivel(self):",
    "print('Pensar')",
    "print('Praticar')",
    "print('Evoluir')",
    "while aprendendo:",
    "estudar()",
    "praticar()",
    "evoluir()",
    "SELECT * FROM devs",
    "JOIN missoes",
    "UPDATE jogadores",
    "INSERT INTO ranking",
    "const xp = 100;",
    "let nivel = 5;",
    "function iniciar(){",
    "return true;",
    "player.addXP(50)",
    "git commit",
    "npm install",
    "python main.py",
    "<html>",
    "<body>",
    "<\/body>",
    "<\/html>"
];

function resizeCanvas(){

    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;

    streams = [];

    const colSpacing = 130;     // colunas mais espaçadas = menos denso
    const rowSpacing = 90;      // menos palavras empilhadas por coluna
    const columns = Math.floor(W / colSpacing);
    const rowsPerColumn = Math.ceil(H / rowSpacing); // cobre a tela sem exagerar

    for(let i=0;i<columns;i++){
        for(let r=0;r<rowsPerColumn;r++){

            streams.push({

                x: i * colSpacing + Math.random()*20,

                y: (r * rowSpacing) - Math.random()*H,

                speed: 0.3 + Math.random()*0.6,

                color: COLORS[Math.floor(Math.random()*COLORS.length)],

                text: CODES[Math.floor(Math.random()*CODES.length)],

                font: 12 + Math.random()*4

            });

        }
    }

}

resizeCanvas();

window.addEventListener("resize", resizeCanvas);

function animateCode(){

    ctx.clearRect(0,0,W,H);

    streams.forEach(stream=>{

        ctx.font = stream.font + "px Consolas";

        ctx.fillStyle = stream.color;

        ctx.shadowBlur = 4;

        ctx.shadowColor = stream.color;

        ctx.fillText(

            stream.text,

            stream.x,

            stream.y

        );

        stream.y += stream.speed;

        if(stream.y > H + 40){

            stream.y = -150;

            stream.color = COLORS[Math.floor(Math.random()*COLORS.length)];

            stream.text = CODES[Math.floor(Math.random()*CODES.length)];

            stream.font = 13 + Math.random()*5;

        }

    });

    requestAnimationFrame(animateCode);

}

animateCode();
