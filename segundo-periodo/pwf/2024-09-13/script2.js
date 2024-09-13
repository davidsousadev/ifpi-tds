document.getElementById("texto").innerHTML = "Texto alterado com JavaScript";
document.getElementById("paragrafo").style.color = "blue";
function mostrarTexto() {
    var texto = document.getElementById("entrada").value;
    document.getElementById("resultado").innerHTML = "Você digitou: " +
    texto.toUpperCase();
}
var frutas = ["Maçã", "Banana", "Laranja"];
document.write("Frutas: " + frutas.join(", ") + "<br>");

var carro = {modelo: "Civic", ano: 2020};
document.write("Modelo: " + carro.modelo + "<br>");
document.write("Ano: " + carro.ano);