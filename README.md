# wechatSpider

这是爬取微信文章列表页接口的爬虫。

# 数据库配置

数据库配置文件在 pipelines.py 文件中。

此项目的默认数据库配置为：

    * 地址：127.0.0.1
    * 数据库：mydb
    * 用户名：root
    * 密码：123456
    * 表名：wechat_list

数据库初始化脚本：

```mysql
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for wechat_list
-- ----------------------------
DROP TABLE IF EXISTS `wechat_list`;
CREATE TABLE `wechat_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `title` varchar(128) CHARACTER SET utf8 DEFAULT NULL,
  `author` varchar(64) CHARACTER SET utf8 DEFAULT NULL,
  `digest` varchar(128) CHARACTER SET utf8 DEFAULT NULL,
  `image_url` varchar(256) CHARACTER SET utf8 DEFAULT NULL,
  `content_url` varchar(256) CHARACTER SET utf8 DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `idx_article_id` (`article_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=latin1;

SET FOREIGN_KEY_CHECKS = 1;
```

# 运行

直接运行 entrypoint.py 文件，即可运行爬虫。



