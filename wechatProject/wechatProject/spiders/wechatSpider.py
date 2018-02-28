# -*- coding: utf-8 -*-
import scrapy


class WechatspiderSpider(scrapy.Spider):
    name = 'wechatSpider'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = ['http://mp.weixin.qq.com/']

    def parse(self, response):
        pass
