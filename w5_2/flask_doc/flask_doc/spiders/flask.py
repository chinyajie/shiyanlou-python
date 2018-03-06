# -*- coding: utf-8 -*-
import scrapy


class FlaskSpider(scrapy.Spider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/']

    def parse(self, response):
        pass
