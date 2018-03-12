# -*- coding: utf-8 -*-

import re
import redis
import json


class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        """
        TODO: 将 item 结果以 JSON 形式保存到 Redis 数据库的 list 结构中
        """
        item['text'] = re.sub('\s+', ' ', item['text'])

        self.redis.lpush("flask_doc:items", json.dumps(dict(item)))  #dict 很重要
        return item


    def open_spider(self, spider):
        # 连接数据库
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)


    def close_spider(self, spider):
        # 关闭数据库连接
        pass
        #self.redis.close()

