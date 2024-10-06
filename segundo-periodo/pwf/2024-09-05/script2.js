document.addEventListener("DOMContentLoaded", (event) => {
    var botao =
        document.getElementById('botaoCopiarTexto');
    botao.addEventListener('click', copiarTexto);

    var botaoLimpar = document.getElementById('botaoLimpar');  
    botaoLimpar.addEventListener('click', limpar);      

    function copiarTexto() {
        var texto = document.getElementById('texto');
        var resultado1 = document.getElementById('resultado1');
        resultado1.innerHTML = resultado1.innerHTML + '<br>' +
                               texto.value;
    }

    function limpar() {
        document.getElementById('resultado1').innerHTML = '';
    }
});



