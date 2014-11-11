import scrapy
import json
from sprig.items import SprigItem
from scrapy.http import Request

class SprigSpider(scrapy.Spider):
	name = "sprig"
	allowed_domains = ["sprig.com", "eatsprig.com"]
	start_urls = [
		"https://prod.eatsprig.com/api/customer/menus",
	]

	# ignore the response
	def parse(self, response):
		decoded = json.loads(response.body)
		sitem = SprigItem()

		for section in decoded:
			if section["meal_id"] == 2:
				sitem["type_of_meal"] = "DINNER"
			else:
				sitem["type_of_meal"] = "LUNCH"		
		
			for meal in section["menu_items"]:
				sitem['description'] = meal['details']
				sitem['name'] = meal['title']
				sitem['price'] = float(meal['price'])/100
				sitem['quantity'] = meal['quantity']
				sitem['dietary'] = ""

				if meal["dairy_free"] == True:
					sitem['dietary'] += "dairy_free "
		
				if meal["gluten_free"] == True:
					sitem['dietary'] += "gluten_free "

				if meal["nut_free"] == True:
					sitem['dietary'] += "nut_free "			

				if meal["paleo"] == True:
					sitem['dietary'] += "paleo "		

				if meal["vegan"] == True:
					sitem['dietary'] += "vegan "		

				if meal["vegetarian"] == True:
					sitem['dietary'] += "vegetarian "	

				yield sitem	

