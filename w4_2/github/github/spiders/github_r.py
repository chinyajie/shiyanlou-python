# -*- coding: utf-8 -*-
import scrapy


class GithubRSpider(scrapy.Spider):
    name = 'github_r'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    def parse(self, response):
        pass
