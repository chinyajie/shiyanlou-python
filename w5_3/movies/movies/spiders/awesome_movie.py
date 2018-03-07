# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from movies.items import MovieItem


class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):

    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    linke = LinkExtractor(allow="https://movie.douban.com/subject/.*")

    rules = (
        Rule(link_extractor=linke, callback="parse_page", follow=True),
    )

    def parse_movie_item(self, response):
        item = MovieItem({
                'url': response.url,
                'name': response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first(),
                'summary': response.xpath('//*[@id="link-report"]/span/text()').extract_first(),
                'score': response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
            })
        print(''.join(response.xpath('//text()').extract()))
        return item

    def parse_start_url(self, response):
        yield self.parse_movie_item(response)

    def parse_page(self, response):
        yield self.parse_movie_item(response)
