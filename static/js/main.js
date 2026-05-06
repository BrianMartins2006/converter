const modal = document.getElementById("resultModal");
const span = document.getElementsByClassName("close")[0];
const resultText = document.getElementById("resultText");
const modalTitle = document.getElementById("modalTitle");
const modalSubtitle = document.getElementById("modalSubtitle");

// Fechar modal
span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

async function doConvert(fromBase, valueId, targetId) {
    const value = document.getElementById(valueId).value;
    const toBase = document.getElementById(targetId).value;

    if (!value) {
        alert("Por favor, insira um valor.");
        return;
    }

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                value: value,
                from_base: fromBase,
                to_base: toBase
            }),
        });

        const data = await response.json();

        // Tradução para o Modal
        const basesPt = {
            'decimal': 'DECIMAL',
            'binary': 'BINÁRIO',
            'hex': 'HEXADECIMAL',
            'octal': 'OCTAL'
        };

        // Mostrar no Modal
        modalTitle.innerText = `Conversão de ${basesPt[fromBase] || fromBase.toUpperCase()}`;
        modalSubtitle.innerText = `Para ${basesPt[toBase] || toBase.toUpperCase()}`;
        resultText.innerText = data.result;
        modal.style.display = "block";

    } catch (error) {
        console.error('Erro:', error);
        alert("Ocorreu um erro na conversão.");
    }
}
