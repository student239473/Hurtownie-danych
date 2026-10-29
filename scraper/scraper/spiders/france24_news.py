import scrapy

from scraper.spiders import RSSNewsSpider


class France24NewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "france24_news"
    source_name = "france24_news"
    allowed_domains = ["www.france24.com"]
    start_urls = ["https://www.france24.com/en/rss"]
