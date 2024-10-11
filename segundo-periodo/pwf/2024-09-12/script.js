var botao = document.getElementById("mudarCor");
var cor = document.getElementById("cor");
// Mudar cor de fundo

function mudarCor() {
    document.body.style.backgroundColor = 'gray'
    if (document.body.style.backgroundColor === 'gray') {
        document.body.style.backgroundColor = 'white'
        cor.innerHTML = "white";
        botao.innerHTML = "Mudar para gray";
    }
    else {
        document.body.style.backgroundColor = 'gray'
        cor.innerHTML = "gray";
        botao.innerHTML = "Mudar para white";
    }
}
botao.addEventListener("click", mudarCor);
// Mudar cor do texto
var botaomudarCorInput = document.getElementById("mudarCorInput");
var botaomudarFundoInput = document.getElementById("mudarFundoInput");
var botaomudarCorFundoInput = document.getElementById("mudarCorFundoInput");
function mudarCorFundoInput() {
    document.body.style.backgroundColor = botaomudarFundoInput.value;
    document.body.style.color = botaomudarCorInput.value;
}
botaomudarCorFundoInput.addEventListener("click", mudarCorFundoInput);

// Mudar o tamanho texto da página
var botaoAumentarTamanhoTexto = document.getElementById("aumentarTamanhoTexto");
var botaoDiminuirTamanhoTexto = document.getElementById("diminuirTamanhoTexto");
var tamanho = 16;
function aumentarTamanhoTexto() {
    tamanho = tamanho + 2;
    document.body.style.fontSize = tamanho + "px";
    console.log(document.body.style.fontSize)
}

function diminuirTamanhoTexto() {
    tamanho = tamanho - 2;
    document.body.style.fontSize = tamanho + "px";
    console.log(document.body.style.fontSize)
}

botaoAumentarTamanhoTexto.addEventListener("click", aumentarTamanhoTexto);
botaoDiminuirTamanhoTexto.addEventListener("click", diminuirTamanhoTexto);