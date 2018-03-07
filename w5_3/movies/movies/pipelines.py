# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import redis

class MoviesPipeline(object):

    def process_item(self, item, spider):
        """
        TODO: 将 item 结果以 JSON 形式保存到 Redis 数据库的 list 结构中
        """

        self.redis.lpush("douban_movie:items", json.dumps(dict(item)))
        return item

    def open_spider(self, spider):
        # 连接数据库
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def close_spider(self, spider):
        # 关闭数据库连接
        pass
        #self.redis.close()


