# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json


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
        'referer': "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA3NTI4NDYyNw==&scene=124&devicetype=android-22&version=26060339&lang=zh_CN&nettype=WIFI&a8scene=7&session_us=gh_4664c99f66c4&pass_ticket=EvoicShL%2B7oJm87LQE8b%2BLt7UpPnaTfej0DeEmcQXerwO75bCPSWTzhnm8KV8j4W&wx_header=1",
        'accept-language': "zh-CN,en-US;q=0.8",
        'cookie': "wxuin=288838823; devicetype=android-22; version=26060339; lang=zh_CN; pass_ticket=EvoicShL+7oJm87LQE8b+Lt7UpPnaTfej0DeEmcQXerwO75bCPSWTzhnm8KV8j4W; wap_sid2=CKep3YkBElxGTlVFek53VUtfYUZkSEtSWEVDcVdPTnoyTEpXcHJfTWFaVElTRmxYaHhvOU84d19PUGprdU9QekpEVGVjUUpmWE1jYWpERmNralpaci1XLVVxZUxfYklEQUFBfjDNs9nUBTgNQJVO",
        'q-ua2': "QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.3&TBSVC=43603&CO=BK&COVC=043906&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MX5 &RL=1080*1920&OS=5.1&API=22",
        'cache-control': "no-cache",
        'postman-token': "77ef4aae-95bb-df62-2a66-bb229341cfa2"
    }

    cookies = {
        'cookie': "wxuin=288838823; devicetype=android-22; version=26060339; lang=zh_CN; pass_ticket=EvoicShL+7oJm87LQE8b+Lt7UpPnaTfej0DeEmcQXerwO75bCPSWTzhnm8KV8j4W; wap_sid2=CKep3YkBElxGTlVFek53VUtfYUZkSEtSWEVDcVdPTnoyTEpXcHJfTWFaVElTRmxYaHhvOU84d19PUGprdU9QekpEVGVjUUpmWE1jYWpERmNralpaci1XLVVxZUxfYklEQUFBfjDNs9nUBTgNQJVO",
    }

    # 开始爬取列表页
    def start_requests(self):
        for page_num in range(0, 1, 1):
            url = 'http://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA3NTI4NDYyNw==&f=json&offset=10&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=EvoicShL%2B7oJm87LQE8b%2BLt7UpPnaTfej0DeEmcQXerwO75bCPSWTzhnm8KV8j4W&wxtoken=&appmsg_token=946_Wb1vp5iG1IfjE6yxCqQ7vHlMzdSV53g0mrmObQ~~&x5=1&f=json'
            # yield Request(url, headers=self.headers, cookies=self.cookies, callback=self.parse)
            yield Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        sites = json.loads(response.body_as_unicode())
        print(sites['errmsg'])
        # for site in sites:
        #     print(site['errmsg'])
        pass
