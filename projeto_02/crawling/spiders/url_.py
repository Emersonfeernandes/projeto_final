from scrapy.crawler import CrawlerProcess
#from crawling.items import Url_Busca
from main.forms import UserForm
import scrapy
import csv
from scrapy.spiders import CrawlSpider
from scrapy.crawler import CrawlerProcess

lista = []
lin = UserForm()
class Extrair_Spider(CrawlSpider):
    x = lin.var()
    name = 'Eminem_Spider'
    start_urls = [x] 
    #[views.home.URL]

    def parse(self, response):
        links = response.xpath('//div/p/a["href"]').extract()

        for link in links:
            yield {
                'link' : response.urljoin(link)
            }
            lista.append(link)
            arquivo = open('escrever.csv', 'w', encoding='utf-8')
            escr = csv.writer(arquivo)
            escr.writerow(link)


    def parse_titulos(self, response):
        pass

    def chama(self):
        y = True

        if y == True:
            if __name__ == '__main__':
                process = CrawlerProcess()
                process.crawl(Extrair_Spider)
                process.start()
        print(lista)

