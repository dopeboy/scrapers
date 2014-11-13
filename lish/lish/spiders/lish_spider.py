import scrapy
import json
from urlparse import urljoin
from lish.items import LishItem
from scrapy.http import Request

class LishSpider(scrapy.Spider):
	name = "lish"
	allowed_domains = ["lishfood.com"]
	start_urls = [
		"http://www.lishfood.com/menu",	
	]

	# ignore the response
	def parse(self, response):
		links = []
		for sel in response.xpath('//a[@class="product-image-block"]/@href').extract():
			links.append(sel)

		for link in links:
			yield Request(urljoin(response.url, link), meta=None, callback=self.parse_job)

	def parse_job(self, response):
		litem = LishItem()
		litem["description"] = response.xpath('//div[@id="product-description-card"]/p').extract()[0]
		litem["name"] = response.xpath('//div[@id="product-info-container"]//h1/text()').extract()[0]
		litem["price"] = response.xpath('//div[@id="product-info-container"]//span/text()').extract()[0]
		litem["dietary"] = response.xpath('//div[@id="product-info-container"]//h4/text()').extract()[0]
		yield litem

			
