'''3. Qual a proporção do valor adicionado bruto médio do setor de serviços em relação ao valor
adicionado bruto total médio no estado do Amazonas no ano de 2018?'''

def porporcao():

    lista = []
    saida = open('./questao3/saida.txt' ,'w')
    with open('./dataset/pib_municipio_2010_a_2018.txt' , 'r' , encoding='utf-8') as data:
        capita = data.readlines()
        for c in capita:
            if 'Amazonas' in c:
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
    cont = 0
    cont2 = 0
    for i in range(len(lista)):
        for x in range(len(lista[1])):
            if x == 9:
                cont    = int(lista[i][x])
                        
            elif x == 11:
                
                cont2    = int(lista[i][x])
    total = 0
    if cont > cont2:
        total = (cont - cont2)*100/cont
    else:
        total = (cont2 - cont)*100/cont
    saida.write("VALOR DA PROPORÇÃO ENTRE \n")
    saida.write('\n')
    saida.write(f'{cont} E {cont2} É IGUAL\n')
    saida.write('\n')
    str(total)
    saida.write(f'{total:.2f}%')
    print(f'{total:.2f}%')



