import scrapy

from scraper.spiders import RSSNewsSpider


class NPRNewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "npr_news"
    source_name = "npr_news"
    allowed_domains = ["feeds.npr.org"]
    start_urls = ["https://feeds.npr.org/1001/rss.xml"]
