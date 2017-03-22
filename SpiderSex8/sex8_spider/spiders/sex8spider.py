# encoding: utf-8
"""
@author: chenhuachao
@license: Apache Licence 
@file: sex8spider.py
@time: 2016/9/17 12:06
屌丝福利，抓取性吧的所有福利。
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy import Spider,Selector
from sex8_spider.items import Sex8SpiderItem,SpiderPullPhotoItem
from scrapy.http  import Request
import urllib
import os
import random
import time

class SexSpider(Spider):
    name = "sex8_spider"
    allowed_domains = ['sex8.com']
    start_urls = [
        "http://alise163.com/forum.php"
    ]
    comman_url = "http://alise163.com/"
    #*_type是要抓取的数据类型页面
    photo_type = [79,80,81,82,83,84,85] #图片
    torrent_type = [108,109]#种子
    def level_tow_parse_photo(self,response):
        '''视频种子列表二级页面的的url和标题提取函数'''
        print ">>>>>>>>>>>,进入二级处理页面"
        content = Selector(response)
        # items = response.meta['items']
        torrent_code = content.xpath('//th[@class="new"]/a[2]')
        for i in torrent_code:
            torrent_url ="{0}{1}".format(self.comman_url,i.xpath("@href").extract()[0])
            torrent_title = i.xpath("text()").extract()[0]
            yield Request(torrent_url,callback=self.photo_download_parse,dont_filter=True)
            time.sleep(2)
        #剩余问题：
            '''二级页面的分页的提取'''
    def level_tow_parse_torrent(self,response):
        '''视频种子列表二级页面的的url和标题提取函数'''
        print ">>>>>>>>>>>,进入二级处理页面"
        content = Selector(response)
        # items = response.meta['items']
        torrent_code = content.xpath('//th[@class="new"]/a[2]')
        for i in torrent_code:
            torrent_url ="{0}{1}".format(self.comman_url,i.xpath("@href").extract()[0])
            torrent_title = i.xpath("text()").extract()[0]
            yield Request(torrent_url,callback=self.photo_download_parse,dont_filter=True)
            time.sleep(2)
        #剩余问题：
            '''二级页面的分页的提取'''
    def torrent_download_parse(self,response):
        '''电影种子的下载函数'''
        content = Selector(response)
        items = response.meta['items']
        torrent_address = "{0}{1}".format(self.comman_url,content.xpath('//p[@class="attnm"]/a/@href').extract()[0])
        torrent_file_name = content.xpath('//p[@class="attnm"]/a/text()').extract()[0]
        urllib.urlretrieve(torrent_address,filename="{0}".format(torrent_file_name)) #下载电影种子，保存文件
        yield items
    def photo_download_parse(self,response):
        '''下载图片的专用函数,两种方式'''
        print ">>>>>>>>>>>>>>>>>>>>>,进入三级下载页面"
        content = Selector(response)
        # items = response.meta['items']
        #第一种方式：利用urllib库直接下载
        photo_list_selector = content.xpath('//img[@class="zoom"]')
        if not os.path.exists("/photo"):
            os.mkdir('/photo')
        for photo_address in photo_list_selector:
            photo_url = photo_address.xpath('@src').extract()[0]
            urllib.urlretrieve(photo_url,os.path.join("/photo",str(random.randint(10000,20000))+".jpg"))
            print "下载图片成功"
        #第二中方式，利用scrapy自带的ImagePipeline
        # list_imgs = response.xpath('//img[@class="zoom"]/@src').extract()
        # print "xxxxxx",list_imgs
        # if list_imgs:
        #   item = SpiderPullPhotoItem()
        #   item['image_urls'] = list_imgs
        #   yield item

    def parse(self, response):
        content = Selector(response)
        photo_area = content.xpath('//td[@class="fl_g"]/div')
        torrent_url_list = []
        photo_url_list = []
        #***************根据枚举数字决定要抓取的数据
        # n=1
        # for i in photo_area:
        #     print n,i.xpath('a/img/@alt').extract()[0]
        #     n+=1
        #*******************************************
        for num in self.photo_type:
            items = Sex8SpiderItem()
            url_level1 = "{0}{1}".format(self.comman_url,photo_area[num].xpath('a/@href').extract()[0])
            items['url'] = url_level1
            items['title'] = photo_area[num].xpath('a/img/@alt').extract()[0]
            # print url_level1,items['title']
            photo_url_list.append(url_level1)
        for num in self.torrent_type:
            items = Sex8SpiderItem()
            url_level1 = "{0}{1}".format(self.comman_url,photo_area[num].xpath('a/@href').extract()[0])
            items['url'] = url_level1
            items['title'] = photo_area[num].xpath('a/img/@alt').extract()[0]
            torrent_url_list.append(url_level1)
        # print photo_url_list,torrent_url_list
        for url in photo_url_list:
            #进入二级页面，取出图片的帖子UTL
            yield Request(url,callback=self.level_tow_parse_photo,dont_filter=True)
            time.sleep(2)
        for url in torrent_url_list:
            # 进入二级页面，取出种子的帖子UTL
            yield Request(url,callback=self.level_tow_parse_torrent,dont_filter=True)
            time.sleep(2)

            # if items['url'] and items['title']:
            #     yield items
            #     items_list.append(items)
            #     yield Request(url_level1,callback="level_tow_parse",meta={"items":items})
        # for link in photo_area:
        #     items = Sex8SpiderItem()
        #     url_level1 = "http://alise163.com/{0}".format(link.xpath('a/@href').extract()[0])
        #     items['url'] =  url_level1
        #     items['title'] = link.xpath('a/img/@alt').extract()[0]
        #     if items['url'] and items['title']:
        #         yield items
        #         items_list.append(items)
        # for url in items_list:
        #     yield Request(url=url['url'],callback=self.other_parse)
