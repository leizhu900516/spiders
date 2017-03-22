# coding:utf-8
__author__ = 'chenhuachao'
# --------------------------------
# Created by chenhuachao  on 201x/xx/xx.
# ---------------------------------
import scrapy
from scrapy import Request
import urllib2
from proxySpider.items import headers,ProxyspiderItem

class ProxySpider(scrapy.Spider):
    name = 'proxyspider'
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/nn/']

    def parse(self, response):
        ipitems = ProxyspiderItem()
        tr_list = response.xpath("//table[@id='ip_list']//tr")
        for tr in tr_list:
            ip = tr.xpath('./td[2]/text()').extract()
            port = tr.xpath('./td[3]/text()').extract()
            ipitems['ip'] = ip[0] if ip else ''
            ipitems['port'] = port[0] if port else ''
            if ipitems['ip'] and ipitems['port']:
                yield ipitems
    def start_requests(self):
        for url in self.start_urls:
            yield  Request(url,callback=self.parse,headers=headers)

 #查看爬到的代理IP是否还能用
def isAlive(self,ip,port):
    proxy={'http':ip+':'+port}
    print proxy

    #使用这个方式是全局方法。
    proxy_support=urllib2.ProxyHandler(proxy)
    opener=urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    #使用代理访问腾讯官网，进行验证代理是否有效
    test_url="http://www.qq.com"
    req=urllib2.Request(test_url,headers=self.header)
    try:
        #timeout 设置为10，如果你不能忍受你的代理延时超过10，就修改timeout的数字
        resp=urllib2.urlopen(req,timeout=10)

        if resp.code==200:
            print "work"
            return True
        else:
            print "not work"
            return False
    except :
        print "Not work"
        return False