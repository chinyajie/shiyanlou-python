# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem


class GithubRSpider(scrapy.Spider):
    name = 'github_r'
    allowed_domains = ['github.com']

    @property
    def start_urls(slef):
        url = "https://github.com/shiyanlou?page={}&tab=repositories"
        return (url.format(i) for i in range(1, 5)) 

    def parse(self, response):
        for repos in response.css('li[class="col-12 d-block width-full py-4 border-bottom public source"]'):
            item = GithubItem({
                'name': repos.css('div[class="d-inline-block mb-1"] h3 a::text').extract_first().strip('\n').strip(),
                'update_time': repos.css('relative-time::attr(datetime)').extract_first()
            })
            yield item
