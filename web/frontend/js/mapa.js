const user = JSON.parse(localStorage.getItem("campone_user") || "{}");
        const nome = user.nome || "Recruta";
        const nivel = user.nivel || "Recruta";
        document.getElementById("playerStatus").textContent = `${nome} • Nível: ${nivel}`;
