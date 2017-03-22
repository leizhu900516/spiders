# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from settings import mongodb_conf
import json
class ProxyspiderPipeline(object):
    def process_item(self, item, spider):
        '''
        写入mongodb中
        '''
        import time
        time.sleep(10)
        conn = pymongo.MongoClient(host=mongodb_conf.get('MONGODB_SERVER'),port=mongodb_conf.get('MONGODB_PORT'))
        database = conn[mongodb_conf.get('MONGODB_DB')]
        collection = database[mongodb_conf.get('MONGODB_COLLECTION')]
        collection.insert(dict(item))
        return item
