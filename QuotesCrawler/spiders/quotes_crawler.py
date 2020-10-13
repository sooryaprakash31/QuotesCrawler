import scrapy
from ..items import QuotescrawlerItem

class QuotesCrawler(scrapy.Spider):
    name = "Quotes"
    start_urls=[
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):

        items = QuotescrawlerItem()

        all_quotes = response.css('div.quote') 
        for quote in all_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            yield items