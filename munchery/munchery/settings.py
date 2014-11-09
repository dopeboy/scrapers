# -*- coding: utf-8 -*-

# Scrapy settings for munchery project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'munchery'

SPIDER_MODULES = ['munchery.spiders']
NEWSPIDER_MODULE = 'munchery.spiders'

ITEM_PIPELINES = {
    'munchery.pipelines.DatabasePipeline': 300
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'munchery (+http://www.yourdomain.com)'
