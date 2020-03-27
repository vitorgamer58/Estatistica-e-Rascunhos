#Python 3.7.X
#Autor: vitorgamer58

#coding: utf-8

print("================ INDICADORES ===============")
print("============== by vitorgamer58 =============")
print("Não deve-se usar vírgulas nem ponto, não usaremos valores decimais")
print("")
print("Vamos começar com os valores do ativo patrimonial")
ativototal = int(input("Digite o ativo total:")) #Solicita os números do usuário e o converte para numero inteiro
ativonaocirculante = int(input("Digite o ativo não circulante:"))
ativocirculante = int(input("Digite o ativo circulante:"))
realizavelalongoprazo = int(input("Digite o realizável a longo prazo:"))
caixa = int(input("Digite o Caixa:"))
bancos = int(input("Digite o valor em bancos:"))
aplicacoesfinanceiras = int(input("Digite o valor em aplicações financeiras:"))
clientes = int(input("Digite o valor à receber de clientes:"))
estoques = int(input("Digite o valor em estoques:"))
ativopermanente = int(input("Digite o imobilizado:"))

print("")
print("Passaremos agora às contas do passivo")
passivocirculante = int(input("Digite o passivo circulante:"))
passivonaocirculante = int(input("Digite o passivo não circulante:"))
fornecedores = int(input("Digite o valor relativo a fornecedores:"))
#salariosapagar = int(input("Digite o valor relativo a obrigações sociais e trabalhistas:"))
#obrigacoesfiscais = int(input("Digite o valor relativo a obrigações fiscais"))

patrimonioliquido = int(input("Digite o patrimônio líquido:"))

print("")
print("Passaremos agora a alguns dados da DRE (Anual)")
receitaoperacionalliquida = int(input("Receita de venda de bens e serviços: "))
lucroconsolidado = int(input("Lucro Consolidado: "))

#Mensuração dos Indicadores
capitaisdeterceiros = passivocirculante + passivonaocirculante
PCT = ((capitaisdeterceiros / patrimonioliquido) * 100) #Participação de Capitais de Terceiros (Endividamento) - PCT %
CE = (passivocirculante / capitaisdeterceiros) * 100 #Composição das Elegibilidades
IPL = ((ativonaocirculante / patrimonioliquido) * 100) # Imobilização do Patrimônio Líquido - IPL %
LG = ((ativocirculante + realizavelalongoprazo) / (passivocirculante + passivonaocirculante)) * 100 #Liquidez Geral (LG) Indice
LC = (ativocirculante / passivocirculante) * 100 #Liquidez Corrente - LC
LS = ((caixa + bancos + aplicacoesfinanceiras + clientes) / passivocirculante) * 100 #Liquidez Seca
GA = (receitaoperacionalliquida / ativototal) * 100 #Giro do ativo
RV = (lucroconsolidado / receitaoperacionalliquida) * 100 #Rentabilidade das Vendas % 
RA = (lucroconsolidado / ativototal) * 100 #Rentabilidade do ativo %
RPL = (lucroconsolidado / patrimonioliquido) * 100 #Rentabilidade do patrimonio líquido %
CCL = ativocirculante - passivocirculante #Capital Circulante Líquido (VALOR)
CGP = patrimonioliquido - ativopermanente - realizavelalongoprazo #Capital de giro próprio
#ACO = estoques + clientes
#PCO = fornecedores + salariosapagar + obrigacoesfiscais
#NCG = 

#Imprimir os resultados na tela
print("A Participação de Capitais de Terceiros é: ", PCT, "%")
print("Composição das Elegibilidades é ", CE, "%")
print("A Imobilização do Patrimônio Líquido é: ", IPL, "%")
print("A Liquidez Geral é: ", LG, "%")
print("A Liquidez Corrente é: ", LC, "%")
print("A Liquidez Seca é: ", LS, "%")
print("O Giro do ativo é: ", GA, "%")
print("A rentabilidade das vendas é: ", RV, "%")
print("A rentabilidade do ativo é: ", RA, "%")
print("A rentabilidade do patrimonio liquido é: ", RPL, "%")

print("")
print("O capital circulante líquido é: ", CCL)
print("O capital de giro próprio é: ", CGP)


