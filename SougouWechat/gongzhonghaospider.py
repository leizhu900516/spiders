# coding:utf-8
__author__ = 'chenhuachao'
# --------------------------------
# Created by chenhuachao  on 201x/xx/xx.
# ---------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class SpiderMain(object):
    '''搜狗微信号内容爬取'''
    def __init__(self,url):
        self.url = url
    def _sleep(self):
        time.sleep(random.randint(2,5))
    def start(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(30)
        self._sleep()
        driver.find_element_by_id('upquery').send_keys(u'保险')
        driver.find_element_by_class_name('swz2').click()
        driver.implicitly_wait(30)
        self.parser(driver)
        #循环进入下一页
        while 1:
            try:
                WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,'sogou_next')))[0].click()
            except:
                driver.close()
            else:
                self.parser(driver)
        driver.close()
    def parser(self,driver):
        '''内容解析函数'''
        itemslist = driver.find_elements_by_xpath('//div[@class="news-box"]/ul[@class="news-list2"]//li')
        print(itemslist)
        for i in itemslist:
            try:
                wechatid = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME, "label"))).text #获取公众号id
            except:
                wechatid = None
            i.find_element_by_tag_name('a').click()
            windows = driver.window_handles
            driver.switch_to_window(windows[-1])
            url = driver.current_url    #url
            try:
                wechatname = WebDriverWait(driver,10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,'tit'))
                    ).text   #公众号名称
            except:
                wechatname = None
            url_news = driver.find_elements_by_xpath('//div[@class="weui_msg_card_bd"]//h4')
            for i in range(len(url_news)):
                time.sleep(5)
                url_news = driver.find_elements_by_xpath('//div[@class="weui_msg_card_bd"]//h4')
                url_news[i].click()
                title = driver.find_element_by_class_name('rich_media_title').text #获取文章标题
                content = driver.find_element_by_class_name('rich_media_content').get_attribute('innerHTML') #获取文章内容，包括样式
                driver.back()
                print(wechatname,wechatid,url,title,content)  #最终所要爬取的数据。
                time.sleep(2)
            driver.close()
            driver.switch_to_window(windows[0])

if __name__ == '__main__':
    spider = SpiderMain('http://weixin.sogou.com/')
    spider.start()