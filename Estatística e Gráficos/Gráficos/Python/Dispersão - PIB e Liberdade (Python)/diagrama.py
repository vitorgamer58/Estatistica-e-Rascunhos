#python3
#Correlação entre Liberdade Econômica e PIB per Capita

# carrega bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# plot grafico de dispersao
plt.scatter(pd.read_csv('index2.csv'), pd.read_csv('pib.csv'))
plt.xlabel('Escore de Liberdade Econômica')
plt.ylabel('PIB per capita (2017, US$)')

plt.show()
