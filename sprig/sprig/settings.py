# -*- coding: utf-8 -*-

# Scrapy settings for sprig project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sprig'

SPIDER_MODULES = ['sprig.spiders']
NEWSPIDER_MODULE = 'sprig.spiders'

DEFAULT_REQUEST_HEADERS = {
"Accept": "application/vnd.eatsprig.v3+json"
}

ITEM_PIPELINES = {
    'sprig.pipelines.DatabasePipeline': 300
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sprig (+http://www.yourdomain.com)'
