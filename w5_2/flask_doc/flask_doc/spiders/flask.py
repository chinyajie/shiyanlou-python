# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem
import re

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ["http://flask.pocoo.org/docs/0.12/"]

    linke = LinkExtractor(allow=("http://flask.pocoo.org/docs/0.12/.*"))

    rules = (
        Rule(link_extractor=linke, callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        raw = ''.join(response.xpath('//text()').extract())
        # response.xpath('/html/body/div[1]/div[2]/div[1]/div/div/text()').extract_first()
        # re.sub(re.compile(r'<[^>]+>'), "", raw)
        # re.sub(re.compile('\s+'), "\s", raw)

        item = PageItem({
            'url': response.url,
            'text': raw,
        })
        yield item
