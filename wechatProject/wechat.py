import http.client
import json

conn = http.client.HTTPConnection("mp.weixin.qq.com")

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
    'postman-token': "a5415b0d-a0af-20e8-0bb0-a249eb79798b"
    }

for page_num in range(0, 900, 1):
    url = "/mp/profile_ext?action=getmsg&__biz=MzA3NTI4NDYyNw%3D%3D&f=json&f=json&offset=" + str(page_num) + "&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=EvoicShL%2B7oJm87LQE8b%2BLt7UpPnaTfej0DeEmcQXerwO75bCPSWTzhnm8KV8j4W&wxtoken=&appmsg_token=946_Wb1vp5iG1IfjE6yxCqQ7vHlMzdSV53g0mrmObQ~~&x5=1"
    conn.request("GET", url=url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    print(result)
    msg_list = result['general_msg_list']
    msg_list_data = json.loads(msg_list)

    msg_array = msg_list_data['list']
    for item in msg_array:
        title = item['app_msg_ext_info']['title']
        digest = item['app_msg_ext_info']['digest']
        content_url = item['app_msg_ext_info']['content_url']
        image_url = item['app_msg_ext_info']['cover']
        print(title)
        print(digest)
        print(content_url)
        print(image_url)
