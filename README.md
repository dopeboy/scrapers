These are two scripts that scrape munchery's and sprig's menus. They make use of scrapy, an open source framework written in python (http://scrapy.org/).

If you want to run them locally: git clone this repo, install mysql with an account of username root and no password, run the code in the sql folder, and then:

```
scrapy crawl munchery -a location=sf
scrapy crawl munchery -a location=seattle
scrapy crawl sprig
```


