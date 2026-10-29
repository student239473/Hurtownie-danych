import scrapy

from scraper.spiders import RSSNewsSpider


class AlJazeeraNewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "al_jazeera_news"
    source_name = "al_jazeera_news"
    allowed_domains = ["www.aljazeera.com"]
    start_urls = ["https://www.aljazeera.com/xml/rss/all.xml"]
