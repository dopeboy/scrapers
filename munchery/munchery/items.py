# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MuncheryItem(scrapy.Item):
	section = scrapy.Field()
	description = scrapy.Field() 
	dietary = scrapy.Field()
	name =  scrapy.Field()
	price = scrapy.Field()
	location = scrapy.Field()
	quantity_remaining = scrapy.Field()
	rating_average = scrapy.Field()
	rating_count = scrapy.Field()		
	pass
