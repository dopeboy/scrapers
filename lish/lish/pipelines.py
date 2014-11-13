import MySQLdb

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DatabasePipeline(object):
    def __init__(self):
			self.conn = MySQLdb.connect (host = "localhost",
									user = "root",
									passwd = "",
									db = "COMPETITORS")
			self.conn.set_character_set('utf8')
			self.cursor = self.conn.cursor ()

    def process_item(self, item, spider):
			self.cursor.execute("INSERT INTO MENU SET SOURCE='LISH', LOCATION='seattle', NAME=%s, DESCRIPTION=%s, PRICE=%s, DIETARY=%s, TYPE_OF_MEAL='DINNER', DATE=NOW()", (item["name"], "a", item["price"][1:],item["dietary"]))
			self.conn.commit()
