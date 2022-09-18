# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JdCommentPipeline:
    def open_spider(self, spider):
        self.fp = open('Comments.txt', 'w')

    def process_item(self, item, spider):
        c = f"{item.get('num')}\n用户名称：{item.get('nickname')}\n{item.get('comment')}\n评论时间：{item.get('date')}\n\n"
        self.fp.write(c)
        return item

    def close_spider(self, spider):
        self.fp.close()
