#QUESTÃO 1
"""Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o
dataset?"""

#FUNÇÃO PARA CALCULAR A MEDIA PIB PER CAPITA DA CIDADE DE MANAUS
import time


def calcPib():
    saida = open('./questao1/saida.txt' ,'w')
    lista = []

    with open('./dataset/pib_municipio_2010_a_2018.txt' , 'r' , encoding='utf-8') as data :
        municipios = data.readlines()
    #AQUI ESTOU PASSANDO A VARIAVEL MUNICIPIOS EM UM FOR
    for n in municipios:
        #SE ENCONTRAR MANAUS EM N
        if 'Manaus' in n:
           
            #NA LISTA APOS O FINAL DA LISTA TEM O SINAL \n POR ISSO PASSEI UM FOR SE ENCONTRAR 
            #ELE SERA REMOVIDO E COLOCADO NADA NO SEU LUGAR

            for char in "\n":
                text = n.replace(char, "")
                #NA LISTA APOS O FINAL DA LISTA TEM O SINAL () POR ISSO PASSEI UM FOR SE ENCONTRAR 
                #ELE SERA REMOVIDO E COLOCADO NADA NO SEU LUGAR
                for sinal in '(':
                    t = text.replace(sinal, '')
                    for s in ')':
                        tex = t.replace(s , '')
                txt =  tex.split(";")
                lista.append(txt)

    pib = 0
    '''lista[103][ 11] = '2302'
    lista[124][ 11] = '1472'''
     

    for i in range(len(lista)):
        for x in range(len(lista[1])):
            if x >= 6 and x <=9 :

                value = float(lista[i][x])
                pib += value
                
    valorpib = pib/2219580
    print(f'{valorpib:,.3f}' )
       
    
    saida.write(f'PIB PER CAPITAL DA CIDADE DE MANAUS É\n')
    saida.write(f'R$: {valorpib:,.3f}')
def soma(namber):
    value = 0
    value += namber
    #print(value)


#CHAMADA DA FUNÇÃO CALCPIB
calcPib()