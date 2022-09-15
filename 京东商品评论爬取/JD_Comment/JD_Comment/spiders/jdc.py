import scrapy
from JD_Comment.items import JdCommentItem
import json
import time


class JdcSpider(scrapy.Spider):
    name = 'jdc'
    allowed_domains = ['club.jd.com']
    start_urls = ["https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1"]
    page = 0
    num = 1
    base_url_p1 = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page="
    base_url_p2 = "&pageSize=10&isShadowSku=0&rid=0&fold=1"

    def parse(self, response):
        jd_json = response.text.replace('fetchJSON_comment98', '')
        jd_json = jd_json.strip('(')
        jd_json = jd_json.strip(';')
        jd_json = jd_json.strip(')')
        jdt = json.loads(jd_json)

        comment_list = jdt.get("comments")

        for i in comment_list:
            nickname = i.get('nickname')
            comment = i.get('content')
            date = i.get('creationTime')
            user_comment = JdCommentItem(
                nickname=nickname, comment=comment, date=date, num=self.num)
            self.num += 1
            yield user_comment

        if self.page < 52:
            self.page += 1
            url = self.base_url_p1 + str(self.page) + self.base_url_p2
            time.sleep(5)
            yield scrapy.Request(url=url, callback=self.parse)
