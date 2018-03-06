# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem
import re

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = "http://flask.pocoo.org/docs/0.12/"

    linke = LinkExtractor(allow=(), deny=(), allow_domains=("http://flask.pocoo.org/docs/0.12/\.+", ),
                                  deny_domains=(),deny_extensions=None, restrict_xpaths=(), restrict_css=(),
                                  tags=('a', ), attrs=('href', ), canonicalize=True, unique=True, process_value=None)

    rules = (
        Rule(link_extractor=linke, callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        raw = response.xpath('/html/body/div[1]/div[2]/div[1]/div/div/text()').extract_first()
        re.sub(re.compile(r'<[^>]+>'), "", raw)
        re.sub(re.compile('\s+'), "\s", raw)

        item = PageItem({
            'url': str(response.url),
            'text': raw,
        })
        yield item