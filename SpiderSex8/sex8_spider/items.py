# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field,Item


class Sex8SpiderItem(Item):
    """一级定义的url和标题"""
    url = Field() #一级页面的URL
    title = Field() #一级页面的标题
class SpiderPullPhotoItem(Item):
    '''图片的item'''
    image_urls = Field()
    images = Field()
