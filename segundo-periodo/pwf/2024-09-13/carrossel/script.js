
let indiceAtual = 0;
const imagens = [
  document.getElementById('imagem1'),
  document.getElementById('imagem2'),
  document.getElementById('imagem3'),
  document.getElementById('imagem4')
];

const totalImagens = imagens.length;

const btnAnterior = document.getElementById('btn-anterior');
const btnProximo = document.getElementById('btn-proximo');
// Adicionando eventos de clique aos botões
btnProximo.addEventListener('click', proximaImagem);
btnAnterior.addEventListener('click', imagemAnterior);

function mostrarImagem(indice) {
  const carrossel = document.getElementById('carrossel');
  const largura = imagens[0].clientWidth;
  carrossel.style.transform = `translateX(${-indice * largura}px)`;
}

function proximaImagem() {
  indiceAtual = (indiceAtual + 1) % totalImagens;
  mostrarImagem(indiceAtual);
}

function imagemAnterior() {
  indiceAtual = (indiceAtual - 1 + totalImagens) % totalImagens;
  mostrarImagem(indiceAtual);
}


