# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LishItem(scrapy.Item):
	description = scrapy.Field() 
	name =  scrapy.Field()
	dietary = scrapy.Field()
	price = scrapy.Field()
	pass
