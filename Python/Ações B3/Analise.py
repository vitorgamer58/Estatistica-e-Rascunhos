# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:43:07 2020

@author: vitor
"""

import numpy as np
import pandas as pd
import pandas_datareader as wb
import matplotlib.pyplot as plt
import math


ticker = 'TRPL4 Historical Data.csv'
tickername = 'TRPL4'

#Lê os dados do CSV e armazena na variável
#ibov = pd.read_csv('Bovespa Historical Data.csv')
ibov = wb.get_data_yahoo('^BVSP', 
                         start = '2015-11-01', 
                         end = '2020-10-29', 
                         interval = 'mo')
ativo = pd.read_csv(ticker)
#ativo = wb.get_data_yahoo('TRPL4.SA', interval = 'mo')



#Elimina possíveis valores em branco
ibov = ibov.dropna()
ativo = ativo.dropna()

#Cria uma coluna com o retorno em relação ao mês anterior
ibov['Retorno']=((ibov['Close']/ibov['Close'].shift(1))-1)
ativo['Retorno']=((ativo['Price']/ativo['Price'].shift(1))-1)

#Calcula a média dos retornos
mean_ibov = np.mean(ibov['Retorno'])
mean_ativo = np.mean(ativo['Retorno'])

print(f'A média do IBOV é de {round(mean_ibov*100,2)}% ao mês')
print(f'A média do Ativo {tickername} é de {round(mean_ativo*100,2)}% ao mês')


#Calcula a Variancia, isto é, os desvios em relação à média
ibov['var_1'] = ((ibov['Retorno']-mean_ibov) ** 2)
sum_var1 = np.sum(ibov.var_1)
variancia_ibov = sum_var1/59
#variancia_ibov = round(variancia_ibov, 2)

ativo['var_1'] = ((ativo['Retorno']-mean_ativo) ** 2)
sum_var2 = np.sum(ativo.var_1)
variancia_ativo = sum_var2/59
#variancia_ativo = (variancia_ativo)

print(f'\n'
      f'A variância do IBOV para o período é de {round(variancia_ibov*100,2)}% \n'
      f'A variância do ativo {tickername} para o período é de {round(variancia_ativo*100,2)}%')

#Calcula o Desvio-Padrão
desvio_ibov = round(math.sqrt(variancia_ibov),2)*100
desvio_ativo = round(math.sqrt(variancia_ativo),2)*100

#calcula as probabilidades

def printdesvio(desvio_ibov, desvio_ativo):
    print(f'\n'
          f'O desvio-padrão do IBOV é de {round(desvio_ibov, 2)}% \n'
          f'isso significa que: \n'
          f'Os retornos do IBOV vão estar entre:\n'
          f'{round(mean_ibov-desvio_ibov, 2)}% e {round(mean_ibov+desvio_ibov,2)}% com 68% de confiança \n'
          f'{round(mean_ibov-(desvio_ibov*1.96), 2)}% e {round(mean_ibov+(desvio_ibov*1.96),2)}% com 95% de confiança \n'
          f'{round(mean_ibov-(desvio_ibov*3), 2)}% e {round(mean_ibov+(desvio_ibov*3),2)}% com 99% de confiança')
    print(f'\n'
          f'O desvio-padrão do ativo {tickername} é de {round(desvio_ativo,2)}% \n'
          f'isso significa que: \n'
          f'Os retornos do {tickername} vão estar entre:\n'
          f'{round(mean_ativo-desvio_ativo, 2)}% e {round(mean_ativo+desvio_ativo,2)}% com 68% de confiança \n'
          f'{round(mean_ativo-(desvio_ativo*1.96), 2)}% e {round(mean_ativo+(desvio_ativo*1.96),2)}% com 95% de confiança \n'
          f'{round(mean_ativo-(desvio_ativo*3), 2)}% e {round(mean_ativo+(desvio_ativo*3),2)}% com 99% de confiança')

printdesvio(desvio_ibov, desvio_ativo)


#Calcula a covariância entre o ativo e o IBOV
co_var = pd.DataFrame()
co_var['Ativo'] = (ativo['Retorno']-mean_ativo).values
co_var['Ibov'] = (ibov['Retorno']-mean_ibov).values
#Multiplica ativo por ibov
co_var['multi'] = co_var['Ativo'] * co_var['Ibov']
#Soma todas as multiplicações e divide por N-1
covariancia = (np.sum(co_var.multi))/59

#CALCULA O BETA DO ATIVO
beta = covariancia / variancia_ibov
print(f'\n'
      f'O BETA do ativo é de {round(beta,2)}')

#Função de gerar histograma
def histograma(dados):
    title = 'Retornos da ação ' + tickername
    plt.title(title)
    plt.ylabel('Quantidade de vezes')
    plt.xlabel('Retorno')
    plt.hist(dados)



    

