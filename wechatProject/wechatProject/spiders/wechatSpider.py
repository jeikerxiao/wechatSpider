# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from wechatProject.items import WechatprojectItem


class WechatspiderSpider(scrapy.Spider):
    name = 'wechatSpider'
    allowed_domains = ['mp.weixin.qq.com']
    # start_urls = ['http://mp.weixin.qq.com/']

    headers = {
        'Host': 'mp.weixin.qq.com',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; MX5 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043909 Mobile Safari/537.36 MicroMessenger/6.6.5.1280(0x26060532) NetType/WIFI Language/zh_CN',
        'Accept': '*/*',
        'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MzY3MzcyNg==&scene=124&devicetype=android-22&version=26060533&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=SIVDnvazjSp7TSFheNpG7zkpRL6TSwT32%2By5AyejxXM%3D&wx_header=1',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Q-UA2': 'QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.5&TBSVC=43603&CO=BK&COVC=043909&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MX5 &RL=1080*1920&OS=5.1&API=22',
        'Q-GUID': '4f80e0f5acc87842faec328113b788cb',
        'Q-Auth': '31045b957cf33acf31e40be2f3e71c5217597676a9729f1b'
    }

    cookies = {
        'wxuin': '234614489',
        'devicetype': 'android-22',
        'version': '26060533',
        'lang': 'zh_CN',
        'pass_ticket': 'SIVDnvazjSp7TSFheNpG7zkpRL6TSwT32+y5AyejxXM=',
        'wap_sid2': 'CNnd728SXHRiWkxmZjRkSHhOZTJVQ0YyVERyV25fYWV2a2dyWXUyY3NDTDZMb25HbHNGRkJtNHdNdkt0TUozNDB5Wk5pa19UeGxFUm9oVUdjal9nVDVrWnMwWV9yUURBQUF+MNrIrNUFOA1AlU4='
    }

    # 开始爬取列表页
    def start_requests(self):
        for page_num in range(0, 200, 10):
            url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5MzY3MzcyNg==&f=json&offset=' + str(
                page_num) + '&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=SIVDnvazjSp7TSFheNpG7zkpRL6TSwT32%2By5AyejxXM%3D&wxtoken=&appmsg_token=948_QoJP%252FojZDF4XOmDtbUC3TYR-yT6qqliKHqNQHg~~&x5=1'
            yield Request(url, headers=self.headers, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.body_as_unicode())
        print(result)
        if result['ret'] == 0:
            msg_list = result['general_msg_list']
            msg_list_data = json.loads(msg_list)

            msg_array = msg_list_data['list']
            for json_item in msg_array:
                item = WechatprojectItem()
                item['id'] = json_item['comm_msg_info']['id']
                try:
                    item['title'] = json_item['app_msg_ext_info']['title']
                    item['digest'] = json_item['app_msg_ext_info']['digest']
                    item['content_url'] = json_item['app_msg_ext_info']['content_url'].replace('&amp;', '&')
                    item['image_url'] = json_item['app_msg_ext_info']['cover']
                    item['author'] = json_item['app_msg_ext_info']['author']
                    if item['title'] != '':
                        yield item
                except KeyError as e:
                    self.log('id：%s no content' % (item['id']))
                    pass
        else:
            self.log(result)
        pass
