// ATIVIDADE DART

//import 'dart:ffi';
import 'dart:io';

void main() {
  var resultado1 = questao_1();
  var soma = resultado1[0];
  var maior = resultado1[1];
  var resultado2 = questao_2();
  var resultado3 = questao_3();
  var resultado4 = questao_4();
  
  print(soma);
  print(maior);
  print(resultado2);
  print(resultado3);
  print(resultado4);
}

// 1) Escreva um algoritmo que possua dois números inteiros e exiba o valor soma seguido pelo maior deles.
List<int> questao_1() {
  print("Digite um número inteiro num1:");
  String? input = stdin.readLineSync();
  var num1 = int.parse('$input');

  print("Digite um número inteiro num2:");
  String? input2 = stdin.readLineSync();
  var num2 = int.parse('$input2');

  var soma = num1 + num2;
  var maior = num1 > num2 ? num1 : num2;

  return [soma, maior];
}

// 2) Faça um algoritmo que converta Celsius para Fahrenheit. Formula: (0 °C × 9/5) + 32 = 32 °F
double questao_2() {
  print("Digite a temperatura em Celcius:");
  String? input = stdin.readLineSync();
  var celcius = double.parse('$input');
  return  (celcius * 1.8 + 32);
}

// 3) Desenvolver um algoritmo que leia um número inteiro e verifique se o número é divisível por 5 e por 3 ao mesmo tempo.
String questao_3() {
  print("Digite um número inteiro:");
  String? input = stdin.readLineSync();
  var numero_inteiro = int.parse('$input');
  if (numero_inteiro % 5==0 && numero_inteiro % 3==0){
    return 'é';
  }
  else{
    return 'não é';
  }
}

// 4) Dados quatro números distintos, desenvolver um algoritmo que determine e imprima a soma dos três menores. Não deve aceitar números iguais.
int questao_4() {
  List<int> numeros = [];

  while (numeros.length < 4) {
    print("Digite um número inteiro distinto:");
    String? input = stdin.readLineSync();
    int numero = int.parse('$input');

    if (numeros.contains(numero)) {
      print("Número já inserido! Digite um número diferente.");
    } else {
      numeros.add(numero);
    }
  }

  numeros.sort();

  int somaMenores = numeros[0] + numeros[1] + numeros[2];

  return somaMenores;
}
