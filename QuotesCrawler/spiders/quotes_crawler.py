import scrapy

class QuotesCrawler(scrapy.Spider):
    name = "Quotes"
    start_urls=[
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):

        all_quotes = response.css('div.quote') 
        for quote in all_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            yield {
                'title': title,
                'author': author,
                'tag':tag
            }