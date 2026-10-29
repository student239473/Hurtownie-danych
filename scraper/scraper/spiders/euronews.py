import scrapy

from scraper.spiders import RSSNewsSpider


class EuronewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "euronews"
    source_name = "euronews"
    allowed_domains = ["www.euronews.com"]
    start_urls = ["https://www.euronews.com/rss?level=theme&name=news"]
