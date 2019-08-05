#python 3.x
#calcula em quantas vezes foi a poupança real em relação a renda líquida
renda = int(input(' Digite sua renda líquida: '))
gastos = int(input(' Digite seus gastos (digite 0 para digitar poupança): '))
#=(renda-gasto ou poupança)/(renda)
if gastos==0: 
	poupanca=int(input(' Digite sua poupança: '))
	preal=(poupanca/renda)
	preal=round(preal, 2)
	print(' Sua poupança real foi de:', preal, 'X de sua renda')

else:
	preal=((renda-gastos)/renda)
	preal=round(preal, 2)
	print(' Sua poupança real foi de:', preal, 'X de sua renda')

#poupanca = input('Digite seus gastos (em branco para digitar poupança): ')