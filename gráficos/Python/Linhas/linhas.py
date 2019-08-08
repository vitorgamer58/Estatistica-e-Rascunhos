import matplotlib.pyplot

eixo_x = ['1', '2']
eixo_y = [500, 900]

matplotlib.pyplot.title('Titulo qualquer')
matplotlib.pyplot.plot(eixo_x, eixo_y)
#matplotlib.pyplot.ylim(500, 1000) - mexe nas escalas
matplotlib.pyplot.xlabel('Legenda X')
matplotlib.pyplot.ylabel('Legenda Y')
matplotlib.pyplot.show()
