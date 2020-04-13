from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def trata_html(input):
    return " ".join(html.split()).replace('>  <', '><')
def trata_html2(input):
    return " ".join(html.split()).replace('> <', '><')

if __name__ == '__main__':
    browser = webdriver.Chrome('drivers/chromedriver.exe')
    url = 'https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?'
    browser.get(url)
    sleep(5)
    html = browser.page_source
    sleep(5)
    browser.close()
    html = trata_html(html)
    html = trata_html2(html)
    soup = BeautifulSoup(html, 'html.parser')
    tabela = soup.find('table')
    imoveis = {}

    for imovel in tabela.find_all('tr'):

        imoveis['link'] = imovel.find('a', href=True)
        imoveis['endereco'] = imovel.find_all('td')[1].text.strip()
        imoveis['bairro'] = imovel.find_all('td')[2].text.strip()
        imoveis['descricao'] = imovel.find_all('td')[3].text.strip()
        imoveis['preco'] = imovel.find_all('td')[4].text.strip()
        imoveis['avaliacao'] = imovel.find_all('td')[5].text.strip() 
        imoveis['desconto'] = imovel.find_all('td')[6].text.strip()
        imoveis['modalidade'] = imovel.find_all('td')[7].text.strip()
        imoveis['foto']  = imovel.find_all('td')[8].text.strip()
        imoveis['cidade'] = imovel.find_all('td')[9].text.strip()
        imoveis['estado'] = imovel.find_all('td')[10].text.strip()

print(imoveis)

        
   


