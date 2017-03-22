# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()


headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Cache-Control":"max-age=0",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Connection":"keep-alive",
    "Host":"www.xicidaili.com",
    "Referer":"http://www.xicidaili.com/",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}
