# /usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy

class GithubSpider(scrapy.Spider):
    name = 'github'

    @property
    def start_urls(self):
        url_tmp = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmp.format(i) for i in range(1,5))

    def parse(self, response):
        for repos in response.css('li[class="col-12 d-block width-full py-4 border-bottom public source"]'):
            # if len(repos.css('div[class="d-inline-block mb-1"] h3 a::text')) == 0:
            #     continue
            # else:
            #     print("哈")

            yield {
                'name': repos.css('div[class="d-inline-block mb-1"] h3 a::text').extract_first().strip('\n').strip(),
                'update_time': repos.css('relative-time::attr(datetime)').extract_first()
            }


