# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy import Request
import pymongo
from scrapy.conf import settings
from scrapy import log
# class SpiderPullPhotoPipeline(ImagesPipeline):
#   def get_media_requests(self,item,info):
#     for image_url in item['image_urls']:
#       yield Request(image_url)
#   def item_completed(self, results, item, info):
#     image_paths = [x['path'] for ok, x in results if ok]
#     if not image_paths:
#       raise DropItem("Item contains no images")
#     item['image_paths'] = image_paths
#     return item

class Sex8SpiderPipeline(object):
    def __init__(self):
        # connection = pymongo.MongoClient('localhost',27017)
        # db = connection[settings['MONGODB_DB']]
        # self.collection = db[settings['MONGODB_COLLECTION']]
        pass
    #用于下载图片的方法
    # def get_media_requests(self,item,info):
    #     for image_url in item['image_urls']:
    #         yield Request(image_url)
    # def item_completed(self,results,item,info):
    #     image_paths = [x['path'] for ok,x in results if ok]
    #     if not image_paths:
    #         raise DropItem("item contains no image")
    #     item['image_paths'] = image_paths
    #     return item
    #end
    def process_item(self, item, spider):
        # valid = True
        # for data in item:
        #
        #     if not data:
        #         valid = False
        #         raise DropItem("Missing {0}!".format(data))
        # if valid:
        #     self.collection.insert(dict(item))
        #     log.msg("Question added to MongoDB database!",
        #             level=log.DEBUG, spider=spider)
        # return item
        pass
