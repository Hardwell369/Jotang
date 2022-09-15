# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdCommentItem(scrapy.Item):
    nickname = scrapy.Field()
    comment = scrapy.Field()
    date = scrapy.Field()
    num = scrapy.Field()
