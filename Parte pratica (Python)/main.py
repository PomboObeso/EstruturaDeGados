import pandas as pd
import csv


"""
train_dataset = pd.read_csv('Base de dados/2015.csv')
print(train_dataset.head())
"""
lista = []
lista_temp = []

arq = open('Base de dados/2015.csv', 'r')
lista_temp = arq.read().split("\n")
lista_temp = ','.join(lista_temp)
lista_temp = lista_temp.split(",")

arq.close()

print(lista_temp[0])

