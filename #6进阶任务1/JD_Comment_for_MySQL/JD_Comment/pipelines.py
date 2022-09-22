# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import MySQLdb


class JdCommentPipeline:
    def open_spider(self, spider):
        self.conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            password="wj13685077009",
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute("create database if not exists JD_User_Comments")
        self.cursor.execute("use JD_User_Comments")
        self.cursor.execute(
            "create table if not exists usr_com(usr_num int primary key,usr_name varchar(100) not null,usr_comment text,usr_date datetime)")

    def process_item(self, item, spider):
        query = f"insert into usr_com(usr_num,usr_name,usr_comment,usr_date) values({item.get('num')},'{item.get('nickname')}','{item.get('comment')}','{item.get('date')}')"
        self.cursor.execute(query)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
