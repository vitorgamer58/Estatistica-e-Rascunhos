algoritmo "verificadirecao"
// Função : Verifica se a pessoa está apta a dirigir
// Autor : vitorgamer58
// Data : 24/03/2020
// Seção de Declarações
var
ano_atual, ano_nasc, Idade: Inteiro
inicio
// Seção de Comandos
Escreval("--------------------------------------")
Escreval("DEPARTAMENTO DE TRÂNSITO DO BANANISTÃO")
Escreval("======= Glória ao Bananistão =========")
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
      Escreval("Está apto a dirigir")
   senao
      Escreval("Não está apto a dirigir")
   fimse

senao
   Escreval("Idade incorreta, verifique e tente novamente")
fimse

fimalgoritmo
