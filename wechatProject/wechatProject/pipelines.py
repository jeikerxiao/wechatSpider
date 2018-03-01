# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import datetime

DEBUG = True


class WechatprojectPipeline(object):
    def process_item(self, item, spider):

        return item

if DEBUG:
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'mydb'
    dbhost = '127.0.0.1'
    dbport = '3306'
else:
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'mydb'
    dbhost = '127.0.0.1'
    dbport = '3306'


class MySQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(user=dbuser,
                                    passwd=dbpass,
                                    db=dbname,
                                    host=dbhost,
                                    charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()
        # 清空表：
        # self.cursor.execute("truncate table wechat_list;")
        # self.conn.commit()

    def process_item(self, item, spider):
        curTime = datetime.datetime.now()
        try:
            self.cursor.execute("""INSERT INTO wechat_list (title, author, digest, image_url, content_url, create_time)  
                            VALUES (%s, %s, %s, %s, %s, %s)""",
                                (
                                    item['title'].encode('utf-8'),
                                    item['author'].encode('utf-8'),
                                    item['digest'].encode('utf-8'),
                                    item['image_url'].encode('utf-8'),
                                    item['content_url'].encode('utf-8'),
                                    curTime,
                                )
                                )
            self.conn.commit()
        except Exception as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            pass
        return item