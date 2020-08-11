import requests
import json
import datetime
import os

def cotaDias(dias):

    arquivo = open('registro.csv', 'w')
    arquivo.write('Data;CotacaoCompra;CotacaoVenda\n')

    hoje = datetime.datetime.now()

    for i in range(dias):

        delta = datetime.timedelta(days=i)
        diaCotado = hoje - delta
        ano = str(diaCotado.year)
        mes = str(diaCotado.month)
        dia = str(diaCotado.day)

        linkCotacaoHoje = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao=\'' + mes + '-' + dia + '-' + ano + '\'&$top=100&$format=json'

        requisicao = requests.get(linkCotacaoHoje)
        cotacao = json.loads(requisicao.text)
        
        if cotacao['value']:
            cotacaoCompra = str(cotacao['value'][0]['cotacaoCompra'])
            cotacaoVenda = str(cotacao['value'][0]['cotacaoVenda'])
            row = '{}/{}/{};'.format(dia, mes, ano) + cotacaoCompra + ';' + cotacaoVenda + '\n'
            arquivo.write(row)
            print('{}/{}/{};'.format(dia, mes, ano))
            print('Cotacao Compra:', cotacaoCompra)
            print('Cotacao Venda', cotacaoVenda, '\n')
        
        #if i % 10 == 0:
        #    os.system('cls')
        #    print('Progresso:', round(((i+1)/dias)*100, 2),'%')
            
    print('Arquivo criado com sucesso')

dias = int(input('Deseja verificar a cotaçao de quantos dias?: '))

cotaDias(dias)

