import { noticias } from "./banco_de_noticias.js";

var conteudo = document.getElementById("noticias");
var destaques = document.getElementById("destaques");
var publicidade = document.getElementById("publicidade");
var contatos = document.getElementById("contatos");

var pagina_contatos = document.getElementById("pagina_contatos");
var pagina_principal = document.getElementById("pagina_principal");

// Paginas

function mostrarcontatos(){
    conteudo.style.display = "none";
    destaques.style.display = "none";
    publicidade.style.display = "none";
    contatos.style.display = "block";
}

function mostrarpaginaprincipal(){
    conteudo.style.display = "block";
    destaques.style.display = "block";
    publicidade.style.display = "block";
    contatos.style.display = "none";
}

pagina_contatos.addEventListener("click", mostrarcontatos);
pagina_principal.addEventListener("click", mostrarpaginaprincipal);

// Noticias

function mostrar_noticias(noticias, quantidade, ultimas){
    var lista_noticias = "";
    if (ultimas===true){
        for (var i = Object.keys(noticias).length - 1; i > (Object.keys(noticias).length - 1 ) - quantidade; i--) {
            lista_noticias += `<article>
                                    <p>
                                        <span>`+noticias[i][0]+` -
                                            <a href="`+noticias[i][2]+`" target="_blank"
                                            class="titulo">`+noticias[i][1]+`</a>
                                        </span><br />
                                        <span class="data"> Data: `+noticias[i][3]+`</span>
                                    </p>
                                    <img src="`+noticias[i][4]+`" alt="Imagem indisponivel!"> </img>
                                </article>`;
        };
    }
    else{
        for (var i = 0; i < quantidade; i++) {
            lista_noticias += `<article>
                                    <p>
                                        <span>`+noticias[i][0]+` -
                                            <a href="`+noticias[i][2]+`" target="_blank"
                                            class="titulo">`+noticias[i][1]+`</a>
                                        </span><br />
                                        <span class="data"> Data: `+noticias[i][3]+`</span>
                                    </p>
                                    <img src="`+noticias[i][4]+`" alt="Imagem indisponivel!"> </img>
                                </article>`;
        };
    }

return lista_noticias;
}

conteudo.innerHTML += mostrar_noticias(noticias, 4, false);
destaques.innerHTML += mostrar_noticias(noticias, 4, true);

// Mudar o tamanho texto da página
var botaoAumentarTamanhoTexto = document.getElementById("aumentarTamanhoTexto");
var botaoDiminuirTamanhoTexto = document.getElementById("diminuirTamanhoTexto");
var tamanho = 16;

function aumentarTamanhoTexto() {
    if (tamanho<26){
    tamanho += 2;
    document.body.style.fontSize = tamanho + "px";
    }
}
function diminuirTamanhoTexto() {
    if (tamanho>16){
        tamanho -= 2;
        document.body.style.fontSize = tamanho + "px";
    
    
}
}

botaoAumentarTamanhoTexto.addEventListener("click", aumentarTamanhoTexto);
botaoDiminuirTamanhoTexto.addEventListener("click", diminuirTamanhoTexto);


// Mudar Cor

var botao = document.getElementById("mudarCor");

function mudarCor() {
    
    if (document.body.style.backgroundColor === 'black') {
        document.body.style.backgroundColor = 'white';
        document.body.style.color = 'black';
        botao.innerHTML = "Dark";
    }
    else {
        document.body.style.backgroundColor = 'black';
        document.body.style.color = 'white';
        botao.innerHTML = "Ligth";
    }
}
botao.addEventListener("click", mudarCor);

