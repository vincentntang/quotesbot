# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    # text, author, tags are all class names, respectively col 1,2,3 in spreadsheet
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract() # there's multiple tags, denormalized in one csv cell
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first() # checks for additional pages
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

