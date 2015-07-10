__author__ = 'Pedro'

from scrapy import log
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader

from ..items import DesafioarpexItem


class MySpider(BaseSpider):
    name = "cosmeticos"
    allowed_domains = ["www.epocacosmeticos.com.br"]
    start_urls = ["http://www.epocacosmeticos.com.br/perfumes",
                  "http://www.epocacosmeticos.com.br/maquiagem",
                  "http://www.epocacosmeticos.com.br/cabelos",
                  "http://www.epocacosmeticos.com.br/dermocosmeticos",
                  "http://www.epocacosmeticos.com.br/tratamentos",
                  "http://www.epocacosmeticos.com.br/corpo-e-banho"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response) # a HTML selector
        print hxs.select('//div[@class="productImage"]').extract()


        # for product_url in product_urls:
        #     yield Request(product_url, callback=self.parse_talk)

    # def get_talks_urls(self, response):
    #     hxs = HtmlXPathSelector(response)
    #     for path in hxs.select('//td/a/@href').extract():
    #         protocol = 'http://'
    #         domain = self.allowed_domains[0]
    #         yield protocol + domain + path
    #
    # def parse_talk(self, response):
    #     loader = XPathItemLoader(item=DesafioarpexItem(), response=response)
    #     loader.add_xpath('link')
    #     loader.add_xpath('description')
    #     return loader.load_item()
