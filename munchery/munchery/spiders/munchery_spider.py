import scrapy
import json
from munchery.items import MuncheryItem
from scrapy.http import Request

class MuncherySpider(scrapy.Spider):
	name = "munchery"
	allowed_domains = ["munchery.com"]
	start_urls = [
		"https://munchery.com",
	]
	zipcode = None;
	location = None;

	def __init__(self, location, *args, **kwargs):
		super(MuncherySpider, self).__init__(*args, **kwargs)
		self.location = location

		if location == "sf":
			self.zipcode = '94117';
		elif location == "seattle":
			self.zipcode = '98105'

	# This does a redirect to the menu so no need to redirect here
	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			method='POST',
			formdata={'zipcode': self.zipcode},
			callback=self.parse_menu
		)

	def parse_menu(self, response):
		decoded = json.loads(response.xpath('//script[@class="menu-page-data"]/text()').extract()[0])
		
		for section in decoded['menu']['sections']:
			for item in section['items']:
				mitem = MuncheryItem()
				mitem['section'] = item['section']
				mitem['description'] = item['description']
				mitem['name'] = item['name']
				mitem['price'] = float(item['price']['dollars']) + (float(item['price']['cents']) * 0.01)

				if 'qty_remaining' in item:
					mitem['quantity_remaining'] = item['qty_remaining']
				else:
					mitem['quantity_remaining'] = None		
			
				mitem['rating_average'] = item['rating']['avg']
				mitem['rating_count'] = item['rating']['count']
				mitem['location'] = self.location
				mitem['dietary'] = ' '.join(item['dietary_preferences'])

				yield mitem		
