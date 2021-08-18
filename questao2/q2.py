#QUESTÃO 2
'''
Qual o ranking de estados por média de PIB per capita no ano de 2010? 3. Qual a
proporção do valor adicionado bruto médio do setor de serviços em relação ao valor
adicionado bruto total médio no estado do Amazonas no ano de 2018?
'''
def rankinPin():
    lista = []

    with open('./dataset/pib_municipio_2010_a_2018.txt' , 'r' , encoding='utf-8') as data:
        capita = data.readlines()
        for c in capita:
            if '2010' in c:
                #RESOLVER OS SINAIS E SIMBOLOS DA BASE DE DADOS
                for char in "\n":
                    text = c.replace(char, "")
                    for sinal in '(':
                        t = text.replace(sinal, '')
                        for s in ')':
                            textfinal = t.replace(s , '')

                txt =  textfinal.split(";")
                lista.append(txt)
    ranking = []
    cidade ={}
    cont = 0
    for i in range(len(lista)):
        for x in range(len(lista[1])):
            if x >=13:
                value = float(lista[i][x])
                cont += value
            cidade ={
                'cidade' : lista[i][3],
                'pib' : cont
            }
            ranking.append(cidade)
        
                    
            #ranking.append(cidade)
   
    for x in range(len(ranking)):
        
        print(ranking[x])

            #print(lista[i][x] ,  end=" ")

rankinPin()
