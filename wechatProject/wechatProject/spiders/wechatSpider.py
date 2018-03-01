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
        'host': "mp.weixin.qq.com",
        'connection': "keep-alive",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Linux; Android 5.1; MX5 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.3.1260(0x26060339) NetType/WIFI Language/zh_CN",
        'accept': "*/*",
        'referer': "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MzY3MzcyNg==&scene=124&devicetype=android-22&version=26060339&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=RE6yeFEhr%2BbWKK0CCD5v8dpeVpzN3zvO0264FP%2FifrI%3D&wx_header=1",
        'accept-language': "zh-CN,en-US;q=0.8",
        'q-ua2': "QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.3&TBSVC=43603&CO=BK&COVC=043906&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MX5 &RL=1080*1920&OS=5.1&API=22",
        'q-guid': "4f80e0f5acc87842faec328113b788cb",
        'q-auth': "31045b957cf33acf31e40be2f3e71c5217597676a9729f1b",
        'cache-control': "no-cache",
        'postman-token': "d107059d-fcae-e480-ea7a-b63e0a51469b"
    }

    cookies = {
        'wxuin': '234614489',
        'devicetype': 'android-22',
        'version': '26060339',
        'lang': 'zh_CN',
        'pass_ticket': 'RE6yeFEhr+bWKK0CCD5v8dpeVpzN3zvO0264FP/ifrI=',
        'wap_sid2': 'CNnd728SXGU3TWNEeDFwTGl0UnBKNkUycW80QllwTThkenJMMFp5QXd2Y29MWEpZNlpKdTd6RlRQZnBabm9sSHh6dFJMUTBjenktNlI1SUZaSzZNaFNzVUEzQzk3SURBQUF+MP/e3dQFOA1AlU4='
    }

    # 开始爬取列表页
    def start_requests(self):
        for page_num in range(0, 130, 10):
            url = 'http://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5MzY3MzcyNg==&f=json&offset=' + str(
                page_num) + '&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=RE6yeFEhr%2BbWKK0CCD5v8dpeVpzN3zvO0264FP%2FifrI%3D&wxtoken=&appmsg_token=946_FdVvphhcfMvh%252FZCuvRBaSf5FgN4-DlWYf-py4w~~&x5=1'
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
                    item['content_url'] = json_item['app_msg_ext_info']['content_url']
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
