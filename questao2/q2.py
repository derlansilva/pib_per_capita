#QUESTÃO 2
'''
Qual o ranking de estados por média de PIB per capita no ano de 2010? 3. Qual a
proporção do valor adicionado bruto médio do setor de serviços em relação ao valor
adicionado bruto total médio no estado do Amazonas no ano de 2018?
'''
def rankinPib():
    lista = []
    saida = open('./questao2/saida.txt' ,'w')
    with open('./dataset/pib_municipio_2010_a_2018.txt' , 'r' , encoding='utf-8') as data:
        capita = data.readlines()
        for c in capita:
            if '2018' in c:
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
    
    for i in range(len(lista)):
        cont = 0
        for x in range(len(lista[1])):
            if lista[i][0] == '2018' and lista[i][3] == lista[i][4] and lista[i][5] == 'Metrópole':
                if x >= 13:  
                    value = float(lista[i][x])
                    cont += value

        ranking.append([cont , lista[i][3]])
    
    ranking.sort(reverse=True)

    saida.write("RANKING PIB PER CAPITA DO ANO 2010\n")
    saida.write('\n')
    
    for i in range(10):
        saida.write(f'{i+1}º {ranking[i][1]}  {ranking[i][0]} \n')
        print(f'{ranking[i][1] } { ranking[i][0]}')

