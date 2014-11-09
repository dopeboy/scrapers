#!/bin/bash

cd /root/public_html/scrapers/munchery/
scrapy crawl munchery -a location=seattle
