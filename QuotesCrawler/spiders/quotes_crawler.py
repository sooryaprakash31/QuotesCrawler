import scrapy

class QuotesCrawler(scrapy.Spider):
    name = "Quotes"
    start_urls=[
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        
        all_quotes = response.css('div.quote') 
        for quote in all_quotes:
            author = quote.css('.author::text').extract()
            yield {
                'author': author
            }