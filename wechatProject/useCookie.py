# coding:utf-8
import requests

url = "http://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5MzY3MzcyNg==&f=json&offset=11&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=RE6yeFEhr%2BbWKK0CCD5v8dpeVpzN3zvO0264FP%2FifrI%3D&wxtoken=&appmsg_token=946_FdVvphhcfMvh%252FZCuvRBaSf5FgN4-DlWYf-py4w~~&x5=1"

headers = {
    'host': "mp.weixin.qq.com",
    'connection': "keep-alive",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Linux; Android 5.1; MX5 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.3.1260(0x26060339) NetType/WIFI Language/zh_CN",
    'accept': "*/*",
    'referer': "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MzY3MzcyNg==&scene=124&devicetype=android-22&version=26060339&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=RE6yeFEhr%2BbWKK0CCD5v8dpeVpzN3zvO0264FP%2FifrI%3D&wx_header=1",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,en-US;q=0.8",
    'cookie': "wxuin=234614489; devicetype=android-22; version=26060339; lang=zh_CN; pass_ticket=RE6yeFEhr+bWKK0CCD5v8dpeVpzN3zvO0264FP/ifrI=; wap_sid2=CNnd728SXGU3TWNEeDFwTGl0UnBKNkUycW80QllwTThkenJMMFp5QXd2Y29MWEpZNlpKdTd6RlRQZnBabm9sSHh6dFJMUTBjenktNlI1SUZaSzZNaFNzVUEzQzk3SURBQUF+MP/e3dQFOA1AlU4=",
    'q-ua2': "QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.3&TBSVC=43603&CO=BK&COVC=043906&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MX5 &RL=1080*1920&OS=5.1&API=22",
    'q-guid': "4f80e0f5acc87842faec328113b788cb",
    'q-auth': "31045b957cf33acf31e40be2f3e71c5217597676a9729f1b",
    'cache-control': "no-cache",
    'postman-token': "440c417a-58b0-507b-dc61-a230bbf28e5e"
    }


# 处理get请求，不传data，则为get请求

# 通过urlopen方法访问拼接好的url
res = requests.get(url, headers=headers)

# read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
res = res.json()
print(res)
