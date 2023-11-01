import scrapy

class MeuSiteSpider(scrapy.Spider):
    name = 'meusite'
    start_urls = ['http://www.meusite.com']

    def parse(self, response):
        title = response.css('title::text').get()
        self.log(f'Título: {title}')
