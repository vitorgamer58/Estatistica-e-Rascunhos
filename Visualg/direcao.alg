algoritmo "verificadirecao"
// Fun��o : Verifica se a pessoa est� apta a dirigir
// Autor : vitorgamer58
// Data : 24/03/2020
// Se��o de Declara��es
var
ano_atual, ano_nasc, Idade: Inteiro
inicio
// Se��o de Comandos
Escreval("--------------------------------------")
Escreval("DEPARTAMENTO DE TR�NSITO DO BANANIST�O")
Escreval("======= Gl�ria ao Bananist�o =========")
Escreval("")
Escreva("Digte o ano atual: ")
Leia(ano_atual)
Escreva("Digite o ano de nascimento: ")
Leia(ano_nasc)
Idade <- ano_atual - ano_nasc
Escreval("")
Se idade > 0 entao
   Escreval("--------------------------------------")
   Escreval("============= RESULTADO ==============")
   Escreval("Idade:", Idade, " Anos")
   se idade > 18 entao
      Escreval("Est� apto a dirigir")
   senao
      Escreval("N�o est� apto a dirigir")
   fimse

senao
   Escreval("Idade incorreta, verifique e tente novamente")
fimse

fimalgoritmo
