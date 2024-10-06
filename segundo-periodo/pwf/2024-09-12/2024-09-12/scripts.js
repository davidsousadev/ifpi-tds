var botaoCorCinza = document.getElementById("mudarCorCinza");

/*
botaoCorCinza.addEventListener("click", () => {
    document.body.style.backgroundColor = 'gray';
});*/

botaoCorCinza.addEventListener("click", mudarCorCinza);
function mudarCorCinza() {
    document.body.style.backgroundColor = 'gray';
}

//mudar cor do texto e do fundo da página
var botao2 = document.getElementById("botao2");
botao2.addEventListener("click", mudarTextoFundo);
function mudarTextoFundo() {
    var corFundo = document.getElementById("corFundo").value;
    var corTexto = document.getElementById("corTexto").value;
    document.body.style.backgroundColor = corFundo;
    document.body.style.color = corTexto;
}

var botao3 = document.getElementById("botao3");
botao3.addEventListener("click", aumentarTexto);
var tamanho = 16;
function aumentarTexto() {
    tamanho = tamanho + 2;
    document.body.style.fontSize = tamanho + "px";
}

var botao4 = document.getElementById('botao4');
botao4.addEventListener('click', carregarLogo);
function carregarLogo() {
    var logo = document.getElementById('logo');
    logo.src = 'https://www.ifpi.edu.br/topo_ifpi.png';
}
