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
    valor1 = 0
    valor2 = 0
    for i in range(len(lista)):
        for x in range(len(lista[1])):
            if x == 9:
                valor1    = int(lista[i][x])
                        
            elif x == 11:
                
                valor2    = int(lista[i][x])
    total = 0
    if valor1 > valor2:
        total = (valor1 - valor2)*100/valor1
    else:
        total = (valor2 - valor1)*100/valor1
    saida.write("VALOR DA PROPORÇÃO ENTRE \n")
    saida.write('\n')
    saida.write(f'{valor1} E {valor2} É IGUAL\n')
    saida.write('\n')
    str(total)
    saida.write(f'{total:.2f}%')
    print(f'{total:.2f}%')



