#import pandas as pd
import csv

lista = []
lista_temp = []
listaTemp2 = []

#Abrindo o arquivo csv com a função open
arq = open('Banco de dados/2015.csv', 'r')
#atribuindo os valores do arquivo à uma lista até achar um \n
lista_temp = arq.read().split("\n")
#passando a lista para string para poder separar os elementos
lista_temp = ','.join(lista_temp)
#Separando os elementos quando se encontra uma vírgula
lista_temp = lista_temp.split(",")
#Fechando o arquivo csv para que a lista possa ser fechada 
arq.close()
j = 0
#k = 1909
for i in range(1909):
    if (j == 11):
        lista.append(listaTemp2)
        #print(lista) 
        listaTemp2.clear()
        j = 0
        #k+=1
    else:
        listaTemp2.append(lista_temp[i]) 
        j+=1
print(lista)

