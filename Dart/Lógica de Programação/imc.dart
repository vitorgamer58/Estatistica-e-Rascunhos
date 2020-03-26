import 'dart:io';

main() {
	//função: calcular o Indice de Massa Corporal
	//pegar o peso
	//pegar a altura
	//realizar o calculo
	//retornar o imc

	print("Digite seu peso (sem ponto ou vírgula)");
	var textPeso = stdin.readLineSync();
	var Peso = int.parse(textPeso);

	print("Digite sua altura (utilize um ponto para separar os decimais)");
	var textAltura = stdin.readLineSync();
	var Altura = double.parse(textAltura);

	var Imc = Peso / (Altura * Altura);

	if(Imc < 18.5){
		print("Abaixo do peso");
	} else if(Imc > 18.5 && Imc < 24.9) {
		print("Peso normal");
	} else if(Imc > 25 && Imc < 29.9) {
		print("Acima do peso");
	} else if(Imc > 30 && Imc < 34.9){
		print("Obesidade grau 1");
	} else if(Imc > 35 && Imc < 39.9) {
		print("Obesidade grau 2");
	} else {
		print("Obesidade grau 3");
	}

}
