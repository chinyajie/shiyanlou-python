# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from sqlalchemy.orm import sessionmaker
from github.models import engine, Repository
class GithubPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.striptime(item['update_time'],
                '%Y-%m-%dT%H:%M:%SZ')
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spide(self, spider):
        self.session.commit()
        self.session.close()
