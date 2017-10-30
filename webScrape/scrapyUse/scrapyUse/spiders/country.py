# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyUse.items import ScrapyuseItem

class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['exmaple.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/index/'), follow=True),
        Rule(LinkExtractor(allow=r'/view/'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = ScrapyuseItem()
        item['name'] = response.css('tr#places_country__row td.w2p_fw::text').extract()
        item['population'] = response.css('tr#places_population__row td.w2p_fw::text').extract()
        return item

