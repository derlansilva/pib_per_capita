#QUESTÃO 1
"""Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o
dataset?"""

#FUNÇÃO PARA CALCULAR A MEDIA PIB PER CAPITA DA CIDADE DE MANAUS

def pinPerCapita():
    lista = []

    with open('./dataset/pib_municipio_2010_a_2018.txt' , 'r' , encoding='utf-8') as data :
        municipios = data.readlines()
   
    for n in municipios:
        if 'Manaus' in n:
    
            for char in "\n":
                text = n.replace(char, "")
                for sinal in '(':
                    t = text.replace(sinal, '')
                    for s in ')':
                        textfinal = t.replace(s , '')

                txt =  textfinal.split(";")
                lista.append(txt)

    pib = 0

    for i in range(len(lista)):
        for x in range(len(lista[1])):
            if x >= 13:
                if lista[i][3] == 'Manaus':
                    value = float(lista[i][x])
                    pib += value

    mediapib = pib /len(lista)
    print(f'{mediapib:.2f}' )
    readTxt(mediapib)
    
def readTxt(pib):
    saida = open('./questao1/saida.txt' ,'w')

    saida.write(f'MÉDIA PIB PER CAPITAL DA CIDADE DE MANAUS\n')
    saida.write('\n')
    saida.write(f'ENTRE OS ANOS 2010 E 2018\n')
    saida.write('\n')
    saida.write(f'R$: {pib:.2f}')
