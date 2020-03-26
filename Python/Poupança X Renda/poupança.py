# python 3.x
# calcula em quantas vezes foi a poupança real em relação a renda líquida
print(' Calculadora de taxa de poupança')
renda = input(' Digite sua renda líquida: ')
renda = float(renda.replace(",", "."))  # Substitui a vírgula pelo ponto e salva a variavel em float
gastos = input(' Digite seus gastos (digite 0 para digitar poupança): ')
gastos = float(gastos.replace(",", "."))
# =(renda-gasto ou poupança)/(renda)
if gastos == 0:
    poupanca = input(' Digite sua poupança: ')
    poupanca = float(poupanca.replace(",", "."))
    preal = (poupanca / renda)
    preal = round(preal, 2)
    print(' Sua poupança real foi de: {0} X de sua renda'.format(preal))
else:
    preal = ((renda - gastos) / renda)
    preal = round(preal, 2)
    print(' Sua poupança real foi de: {0} X de sua renda'.format(preal))
