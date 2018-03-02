# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import GithubItem

class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    allowed_domains = ['github.com']
    
    @property
    def start_urls(self):
        url = "https://github.com/shiyanlou?page={}&tab=repositories"
        return (url.format(i) for i in range(1, 5)) 
    
    def parse(self, response):
        for repos in response.css('li[class="col-12 d-block width-full py-4 border-bottom public source"]'):
            item = GithubItem()
            item['name'] = repos.css('div[class="d-inline-block mb-1"] h3 a::text').extract_first().strip('\n').strip(),
            item['update_time'] = repos.css('relative-time::attr(datetime)').extract_first()
            repos_url = "https://github.com/shiyanlou/{}".format(item['name'][0])
            print(repos_url)
            request = scrapy.Request(repos_url, callback=self.parse_more)
            request.meta['item'] = item
            yield request

    def parse_more(self, response):
        print("more")
        item = response.meta['item']
        for number in response.css('ul.numbers-summary li'):
            print('li')
            type_text = number.xpath('.//a/text()').re_first('\n\s*(.*)\n')
            number_text = number.xpath('.//span[@class="num text-emphasized"]/text()').re_first('\n\s*(.*)\n')
            if type_text and number_text:
                number_text = number_text.replace(',','') 
                if type_text in ('commit', 'commits'):
                    item['commits'] = int(number_text)
                elif type_text in ('branch', 'branches'):
                    item['branches'] = int(number_text)
                elif type_text in ('release', 'releases'):
                    item['releases'] = int(number_text)
                    print("release = {}".format(item['releases']))
        yield item
